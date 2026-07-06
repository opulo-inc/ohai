from __future__ import annotations

import html as html_lib
import re
from dataclasses import dataclass

from bs4 import BeautifulSoup
from bs4.element import Tag
from mkdocs.config import config_options as c
from mkdocs.plugins import BasePlugin


_TAG_RE = re.compile(r"<[^>]+>")
_SLUG_RE = re.compile(r"[^a-z0-9]+")
_COLOR_DIRECTIVE_RE = re.compile(
    r"\s*\{(?:color|colour)\s*=\s*([#\w-]+)\}\s*", re.IGNORECASE
)
_STANDARD_COLORS = (
    "#3b82f6",
    "#22c55e",
    "#f97316",
    "#a855f7",
    "#ef4444",
    "#14b8a6",
    "#eab308",
    "#ec4899",
)
_NAMED_COLORS = {
    "blue": "#3b82f6",
    "green": "#22c55e",
    "orange": "#f97316",
    "purple": "#a855f7",
    "red": "#ef4444",
    "teal": "#14b8a6",
    "yellow": "#eab308",
    "pink": "#ec4899",
}


@dataclass(frozen=True)
class Image:
    src: str
    alt: str
    color: str


@dataclass(frozen=True)
class Step:
    title: str
    slug: str
    aliases: tuple[str, ...]
    toc_slug: str
    parents: tuple[str, ...]
    text_html: str
    images: tuple[Image, ...]


class ZodukiPlugin(BasePlugin):
    """Render assembly instructions as one-action, image-led steps."""

    config_scheme = (
        ("enabled_by_default", c.Type(bool, default=False)),
        ("page_meta_key", c.Type(str, default="zoduki")),
        ("step_heading_level", c.Type(int, default=3)),
        ("min_steps", c.Type(int, default=2)),
    )

    def on_page_markdown(self, markdown: str, page, config, files) -> str:
        meta_key = self.config["page_meta_key"]
        enabled = bool(page.meta.get(meta_key, self.config["enabled_by_default"]))
        if not enabled:
            return markdown

        return self._wrap_step_sections(markdown)

    def on_page_content(self, html: str, page, config, files) -> str:
        meta_key = self.config["page_meta_key"]
        enabled = bool(page.meta.get(meta_key, self.config["enabled_by_default"]))
        if not enabled:
            return html

        steps = self._build_steps(html)
        if len(steps) < int(self.config["min_steps"]):
            return html

        return self._render(steps, page.title or "")

    def _wrap_step_sections(self, markdown: str) -> str:
        wrapped_lines: list[str] = []
        in_fence = False
        in_step = False
        current_subsection = ""

        for line in markdown.splitlines():
            stripped = line.lstrip()

            subsection_match = re.match(r"^##(?!#)\s+(.+?)\s*$", stripped)
            match = re.match(r"^###(?!#)\s+(.+?)\s*$", stripped)
            if not in_fence and subsection_match:
                current_subsection = self._markdown_heading_text(subsection_match.group(1))
            if not in_fence and match:
                if in_step:
                    wrapped_lines.extend(["", "</div>", ""])
                subsection_attr = self._escape_attr(current_subsection)
                wrapped_lines.extend([
                    f'<div class="zoduki-source-step" markdown="1" data-zoduki-subsection="{subsection_attr}">',
                    "",
                ])
                in_step = True
            elif in_step and not in_fence and re.match(r"^#{1,2}(?!#)\s+\S", stripped):
                wrapped_lines.extend(["", "</div>", ""])
                in_step = False

            wrapped_lines.append(line)

            if stripped.startswith(("```", "~~~")):
                in_fence = not in_fence

        if in_step:
            wrapped_lines.extend(["", "</div>"])

        return "\n".join(wrapped_lines)

    def _build_steps(self, html: str) -> list[Step]:
        soup = BeautifulSoup(html, "html.parser")
        steps: list[Step] = []
        used_slugs: set[str] = set()

        for step_element in soup.select(".zoduki-source-step"):
            if not isinstance(step_element, Tag):
                continue

            heading = step_element.find(re.compile(r"^h[1-6]$"))
            if not isinstance(heading, Tag) or not heading.get("id"):
                continue

            section_html = self._step_element_html(step_element, heading)
            section_steps = self._steps_from_section(
                section_html=section_html,
                title=self._text_content(str(heading)),
                heading_slug=heading.get("id", ""),
                parents=(step_element.get("data-zoduki-subsection", ""),),
                used_slugs=used_slugs,
            )
            steps.extend(section_steps)

        return steps

    def _steps_from_section(
        self,
        section_html: str,
        title: str,
        heading_slug: str,
        parents: tuple[str, ...],
        used_slugs: set[str],
    ) -> list[Step]:
        text_html, images = self._extract_text_and_images(section_html)
        return [
            Step(
                title=title,
                slug=self._unique_slug(
                    heading_slug or self._slugify(title),
                    used_slugs,
                ),
                aliases=(heading_slug,) if heading_slug else (),
                toc_slug=heading_slug,
                parents=parents,
                text_html=text_html,
                images=images,
            )
        ]

    def _step_element_html(self, step_element: Tag, heading: Tag) -> str:
        nodes: list[str] = []
        seen_heading = False
        for child in step_element.children:
            if child is heading:
                seen_heading = True
                continue
            if seen_heading:
                nodes.append(str(child))
        return "".join(nodes).strip()

    def _extract_text_and_images(self, html: str) -> tuple[str, tuple[Image, ...]]:
        soup = BeautifulSoup(html, "html.parser")
        bullet_colors = self._colorize_bullets(soup)
        images = tuple(
            Image(
                src=img.get("src", ""),
                alt=img.get("alt", ""),
                color=self._image_color(img, bullet_colors),
            )
            for img in soup.find_all("img")
            if isinstance(img, Tag) and img.get("src")
        )

        for img in soup.find_all("img"):
            img.decompose()

        self._remove_empty_media_wrappers(soup)
        text_html = str(soup).strip()
        if text_html:
            text_html = f'<div class="zoduki__action-copy">{text_html}</div>'
        else:
            text_html = '<ul class="zoduki__action-list"><li>Review the image for this step.</li></ul>'

        return text_html, images

    def _colorize_bullets(self, soup: BeautifulSoup) -> dict[int, str]:
        bullet_colors: dict[int, str] = {}
        top_level_items = [
            item
            for item in soup.find_all("li")
            if isinstance(item, Tag) and item.find_parent("li") is None
        ]

        for index, item in enumerate(top_level_items):
            color = self._bullet_color(item, index)
            existing_classes = item.get("class", [])
            if color:
                bullet_colors[id(item)] = color
                item["class"] = [*existing_classes, "zoduki__color-item"]
                item["style"] = self._append_style(
                    item.get("style", ""),
                    f"--zoduki-item-color: {color}",
                )
            else:
                item["class"] = [*existing_classes, "zoduki__neutral-item"]

        return bullet_colors

    def _bullet_color(self, item: Tag, index: int) -> str:
        directive = self._extract_color_directive(item)
        if directive in {"none", "standard", "default", "off"}:
            return ""
        if directive:
            return self._normalize_color(directive)
        if not item.find("img"):
            return ""
        return _STANDARD_COLORS[index % len(_STANDARD_COLORS)]

    def _extract_color_directive(self, item: Tag) -> str:
        for text_node in item.find_all(string=_COLOR_DIRECTIVE_RE):
            match = _COLOR_DIRECTIVE_RE.search(str(text_node))
            if not match:
                continue
            text_node.replace_with(_COLOR_DIRECTIVE_RE.sub("", str(text_node)))
            return match.group(1).strip().lower()
        return ""

    def _normalize_color(self, color: str) -> str:
        if re.fullmatch(r"#[0-9a-fA-F]{3}(?:[0-9a-fA-F]{3})?", color):
            return color
        return _NAMED_COLORS.get(color.lower(), color)

    def _image_color(self, img: Tag, bullet_colors: dict[int, str]) -> str:
        owner = img.find_parent("li")
        while isinstance(owner, Tag) and owner.find_parent("li") is not None:
            owner = owner.find_parent("li")
        if isinstance(owner, Tag):
            return bullet_colors.get(id(owner), "")
        return ""

    def _append_style(self, existing_style: str, style: str) -> str:
        existing = existing_style.strip()
        if existing and not existing.endswith(";"):
            existing += ";"
        return f"{existing} {style};".strip()

    def _remove_empty_media_wrappers(self, soup: BeautifulSoup) -> None:
        changed = True
        while changed:
            changed = False
            for tag in list(soup.find_all(["a", "p"])):
                if isinstance(tag, Tag) and not self._text_content(str(tag)) and not tag.find("img"):
                    tag.decompose()
                    changed = True

    def _render(self, steps: list[Step], page_title: str) -> str:
        sections = "\n".join(self._render_step(step, index, len(steps)) for index, step in enumerate(steps))
        page_title_attr = self._escape_attr(page_title)

        return f"""
<style>
.md-content__inner:has([data-zoduki]) > h1 {{
  display: none;
}}
.md-content__inner:has([data-zoduki]) {{
  margin-top: 0;
  padding-top: 0;
}}
.zoduki {{
  --zoduki-border: var(--md-default-fg-color--lightest);
  --zoduki-bottom-bar-height: 4.5rem;
  --zoduki-step-height: calc(100dvh - 12rem);
}}
.zoduki__nav {{
  align-items: center;
  background: var(--md-default-bg-color);
  border-bottom: 1px solid var(--zoduki-border);
  display: flex;
  flex-wrap: wrap;
  gap: .35rem .75rem;
  justify-content: space-between;
  margin: 0 0 .5rem;
  padding: .35rem 0;
  position: sticky;
  top: 0;
  z-index: 2;
}}
.zoduki__crumbs {{
  color: var(--md-default-fg-color--light);
  font-size: .72rem;
  letter-spacing: .02em;
  text-transform: uppercase;
}}
.md-sidebar--primary .md-sidebar__scrollwrap {{
  max-height: var(--zoduki-sidebar-height, calc(100dvh - 9rem));
  overflow-x: hidden;
  overflow-y: auto;
  overscroll-behavior: contain;
}}
.md-sidebar--primary .md-sidebar__inner {{
  padding-bottom: 0;
}}
[data-md-component="toc"] {{
  overflow: visible;
}}
.md-nav--secondary .md-nav__list {{
  overflow: visible;
}}
.zoduki__steps {{
  height: var(--zoduki-step-height);
  max-height: var(--zoduki-step-height);
  min-height: 0;
  overflow: hidden;
}}
.zoduki__step {{
  display: grid;
  gap: 1.5rem;
  grid-template-columns: minmax(260px, 1.1fr) minmax(260px, .9fr);
  height: 100%;
  min-height: 0;
  overflow: hidden;
}}
.zoduki__step[hidden] {{
  display: none;
}}
.zoduki__media {{
  display: flex;
  flex-direction: column;
  gap: .75rem;
  min-height: 0;
  min-width: 0;
}}
.zoduki__main-image {{
  align-items: center;
  background: var(--md-code-bg-color);
  border: .25rem solid var(--zoduki-image-color, var(--zoduki-border));
  border-radius: .25rem;
  display: flex;
  flex: 1 1 auto;
  height: 100%;
  justify-content: center;
  min-height: 0;
  overflow: hidden;
}}
.zoduki__main-image img {{
  display: block;
  max-height: 100%;
  max-width: 100%;
  object-fit: contain;
}}
.zoduki__placeholder {{
  color: var(--md-default-fg-color--light);
  padding: 2rem;
}}
.zoduki__thumbs {{
  display: grid;
  flex: 0 0 auto;
  gap: .5rem;
  grid-template-columns: repeat(auto-fill, minmax(3.75rem, 1fr));
  margin-top: -.75rem;
  overflow: visible;
  padding: .75rem 1.75rem 1rem;
}}
.zoduki__thumb {{
  background: transparent;
  border: 2px solid var(--zoduki-image-color, transparent);
  border-radius: .2rem;
  cursor: pointer;
  padding: 0;
}}
.zoduki__thumb[aria-current="true"] {{
  box-shadow:
    0 0 0 2px var(--md-default-bg-color),
    0 0 10px 4px color-mix(in srgb, var(--md-default-fg-color) 60%, transparent),
    0 0 20px 8px color-mix(in srgb, var(--md-default-fg-color) 30%, transparent);
}}
.zoduki__thumb img {{
  aspect-ratio: 1;
  display: block;
  max-height: 3.75rem;
  object-fit: cover;
  width: 100%;
}}
.zoduki__copy {{
  display: flex;
  flex-direction: column;
  min-height: 0;
  overflow-x: hidden;
  overflow-y: auto;
  overscroll-behavior: contain;
  padding-right: .4rem;
}}
.zoduki__copy > p {{
  color: var(--md-default-fg-color--light);
  font-size: .72rem;
  letter-spacing: .02em;
  margin: 0 0 .25rem;
  text-transform: uppercase;
}}
.zoduki__copy h2 {{
  font-size: clamp(1rem, 2vw, 1.35rem);
  line-height: 1.2;
  margin: 0 0 .5rem;
}}
.zoduki__action-list {{
  font-size: clamp(.85rem, 1.6vw, 1.1rem);
  line-height: 1.35;
  margin-bottom: 0;
  overflow: visible;
}}
.zoduki__action-copy > ul {{
  padding-left: 0;
}}
.zoduki__color-item,
.zoduki__neutral-item {{
  border-radius: .25rem;
  list-style-position: inside;
  margin: .5rem 0;
  padding: .55rem .7rem;
}}
.zoduki__color-item {{
  background: color-mix(in srgb, var(--zoduki-item-color) 14%, transparent);
  border-left: .35rem solid var(--zoduki-item-color);
}}
.zoduki__neutral-item {{
  background: var(--md-code-bg-color);
  border-left: .35rem solid var(--md-default-fg-color--lightest);
}}
.zoduki__color-item > p:first-child,
.zoduki__neutral-item > p:first-child {{
  display: inline;
}}
.zoduki__color-item ul,
.zoduki__neutral-item ul {{
  margin-left: 1rem;
}}
.zoduki__controls {{
  align-items: center;
  background: var(--md-default-bg-color);
  border-top: 1px solid var(--zoduki-border);
  bottom: 0;
  box-shadow: 0 -.2rem .6rem rgba(0, 0, 0, .12);
  display: flex;
  gap: .75rem;
  justify-content: space-between;
  left: 0;
  padding: .75rem max(1rem, calc((100vw - 61rem) / 2));
  position: fixed;
  right: 0;
  z-index: 10;
}}
.zoduki__button {{
  background: var(--md-primary-fg-color);
  border-radius: .2rem;
  color: var(--md-primary-bg-color) !important;
  display: inline-block;
  font-weight: 700;
  min-width: 8rem;
  padding: .6rem 1rem;
  text-align: center;
}}
.zoduki__button[aria-disabled="true"] {{
  opacity: .45;
  pointer-events: none;
}}
@media (max-width: 800px) {{
  .zoduki {{
    --zoduki-step-height: calc(100dvh - 11rem);
  }}
  .zoduki__step {{
    grid-template-columns: 1fr;
    grid-template-rows: minmax(0, 1fr) auto;
    gap: .75rem;
  }}
}}
</style>
<div class="zoduki" data-zoduki>
  <nav class="zoduki__nav" aria-label="Guide progress">
    <div class="zoduki__crumbs"><span>{page_title_attr}</span></div>
    <span data-zoduki-progress></span>
  </nav>
  <div class="zoduki__steps" data-zoduki-steps>
    {sections}
  </div>
  <div class="zoduki__controls">
    <a class="zoduki__button" href="#" data-zoduki-prev>Previous</a>
    <a class="zoduki__button" href="#" data-zoduki-next>Next</a>
  </div>
</div>
<script>
(function() {{
  const root = document.currentScript.previousElementSibling;
  const steps = Array.from(root.querySelectorAll("[data-zoduki-step]"));
  const stepContainer = root.querySelector("[data-zoduki-steps]");
  const progress = root.querySelector("[data-zoduki-progress]");
  const previous = root.querySelector("[data-zoduki-prev]");
  const next = root.querySelector("[data-zoduki-next]");

  function fitStepToViewport() {{
    const containerTop = stepContainer.getBoundingClientRect().top;
    const controlsTop = previous.closest(".zoduki__controls").getBoundingClientRect().top;
    const availableHeight = Math.max(220, Math.floor(controlsTop - containerTop - 12));
    root.style.setProperty("--zoduki-step-height", availableHeight + "px");
  }}

  function fitTocToViewport() {{
    const sidebarScrollwrap = document.querySelector(".md-sidebar--primary .md-sidebar__scrollwrap");
    if (!sidebarScrollwrap) return;

    const controlsTop = previous.closest(".zoduki__controls").getBoundingClientRect().top;
    const sidebarTop = sidebarScrollwrap.getBoundingClientRect().top;
    const sidebarHeight = Math.max(180, Math.floor(controlsTop - sidebarTop - 12));
    sidebarScrollwrap.style.setProperty("--zoduki-sidebar-height", sidebarHeight + "px");
    sidebarScrollwrap.style.maxHeight = sidebarHeight + "px";
  }}

  function fitLayoutToViewport() {{
    fitStepToViewport();
    fitTocToViewport();
  }}

  function imagesFor(step) {{
    return Array.from(step.querySelectorAll("[data-zoduki-image]"));
  }}

  function showImage(step, imageIndex) {{
    const images = imagesFor(step);
    const thumbs = Array.from(step.querySelectorAll("[data-zoduki-thumb]"));
    if (!images.length) return;

    const bounded = Math.max(0, Math.min(imageIndex, images.length - 1));
    const main = step.querySelector("[data-zoduki-main]");
    const mainFrame = main?.closest(".zoduki__main-image");
    main.src = images[bounded].dataset.src;
    main.alt = images[bounded].dataset.alt || "";
    mainFrame?.style.setProperty("--zoduki-image-color", images[bounded].dataset.color || "");
    step.dataset.activeImage = String(bounded);

    thumbs.forEach((thumb, index) => {{
      thumb.setAttribute("aria-current", index === bounded ? "true" : "false");
    }});
    updateControls();
  }}

  function activeStepIndex() {{
    return steps.findIndex((step) => !step.hidden);
  }}

  function stepMatchesHash(step, hash) {{
    if (step.dataset.stepId === hash) return true;
    return (step.dataset.stepAliases || "").split(" ").includes(hash);
  }}

  function buildFlatToc() {{
    const toc = document.querySelector('[data-md-component="toc"]');
    if (!toc) return;

    const seen = new Set();
    const tocSteps = steps.filter((step) => {{
      const tocId = step.dataset.tocId;
      if (!tocId || seen.has(tocId)) return false;
      seen.add(tocId);
      return true;
    }});
    if (!tocSteps.length) return;

    function stepItem(step) {{
      const item = document.createElement("li");
      item.className = "md-nav__item";

      const link = document.createElement("a");
      link.className = "md-nav__link";
      link.href = "#" + step.dataset.stepId;
      link.dataset.zodukiTocId = step.dataset.tocId;

      const label = document.createElement("span");
      label.className = "md-ellipsis";
      label.textContent = step.dataset.stepTitle || "Step";

      link.append(label);
      item.append(link);
      return item;
    }}

    const groupedItems = [];
    let currentGroup = null;
    let currentList = null;

    tocSteps.forEach((step) => {{
      const subsection = step.dataset.parent || "";
      if (subsection) {{
        if (!currentGroup || currentGroup.dataset.subsection !== subsection) {{
          currentGroup = document.createElement("li");
          currentGroup.className = "md-nav__item md-nav__item--nested";
          currentGroup.dataset.subsection = subsection;

          const label = document.createElement("span");
          label.className = "md-nav__link";
          const labelText = document.createElement("span");
          labelText.className = "md-ellipsis";
          labelText.textContent = subsection;
          label.append(labelText);

          const nestedNav = document.createElement("nav");
          nestedNav.className = "md-nav";
          nestedNav.setAttribute("aria-label", subsection);

          currentList = document.createElement("ul");
          currentList.className = "md-nav__list";
          nestedNav.append(currentList);

          currentGroup.append(label, nestedNav);
          groupedItems.push(currentGroup);
        }}
        currentList.append(stepItem(step));
      }} else {{
        currentGroup = null;
        currentList = null;
        groupedItems.push(stepItem(step));
      }}
    }});

    toc.replaceChildren(...groupedItems);
  }}

  function syncTocHighlight(activeStep, requestedHash) {{
    const toc = document.querySelector('[data-md-component="toc"]');
    if (!toc) return;

    toc.querySelectorAll(".md-nav__link--active").forEach((link) => {{
      link.classList.remove("md-nav__link--active");
      link.removeAttribute("aria-current");
    }});
    toc.querySelectorAll(".md-nav__item--active").forEach((item) => {{
      item.classList.remove("md-nav__item--active");
    }});

    const aliases = (activeStep.dataset.stepAliases || "").split(" ").filter(Boolean);
    const targetHash = aliases.includes(requestedHash)
      ? requestedHash
      : activeStep.dataset.tocId || aliases[0] || activeStep.dataset.stepId;
    const flatTargetLink = activeStep.dataset.tocId
      ? toc.querySelector('.md-nav__link[data-zoduki-toc-id="' + activeStep.dataset.tocId + '"]')
      : null;
    const targetLink = flatTargetLink || Array.from(toc.querySelectorAll('.md-nav__link[href^="#"]'))
      .find((link) => link.getAttribute("href") === "#" + targetHash);

    if (!targetLink) return;
    targetLink.classList.add("md-nav__link--active");
    targetLink.setAttribute("aria-current", "true");
    const targetItem = targetLink.closest(".md-nav__item");
    targetItem?.classList.add("md-nav__item--active");
    targetItem?.parentElement?.closest(".md-nav__item--nested")?.classList.add("md-nav__item--active");
  }}

  function updateControls() {{
    const index = activeStepIndex();
    if (index < 0) return;

    const active = steps[index];
    const imageCount = imagesFor(active).length;
    const imageIndex = Number(active.dataset.activeImage || "0");

    progress.textContent = "Step " + (index + 1) + " of " + steps.length;
    previous.setAttribute("aria-disabled", index === 0 && imageIndex === 0 ? "true" : "false");
    next.setAttribute("aria-disabled", index === steps.length - 1 && imageIndex >= imageCount - 1 ? "true" : "false");
    next.textContent = imageIndex < imageCount - 1 ? "Next image" : "Next";
  }}

  function showStep(slug, updateHash) {{
    let index = steps.findIndex((step) => stepMatchesHash(step, slug));
    if (index < 0) index = 0;

    fitLayoutToViewport();
    steps.forEach((step, stepIndex) => {{
      step.hidden = stepIndex !== index;
    }});

    showImage(steps[index], 0);
    updateControls();
    syncTocHighlight(steps[index], slug);

    const canonicalHash = steps[index].dataset.stepId;
    const currentHash = window.location.hash.slice(1);
    if (currentHash !== canonicalHash) {{
      const method = updateHash ? "pushState" : "replaceState";
      history[method](null, "", "#" + canonicalHash);
    }}
  }}

  root.querySelectorAll("[data-zoduki-thumb]").forEach((thumb) => {{
    thumb.addEventListener("click", () => {{
      const step = thumb.closest("[data-zoduki-step]");
      showImage(step, Number(thumb.dataset.imageIndex || "0"));
    }});
  }});

  previous.addEventListener("click", (event) => {{
    event.preventDefault();
    if (previous.getAttribute("aria-disabled") === "true") return;

    const index = activeStepIndex();
    const active = steps[index];
    const imageIndex = Number(active.dataset.activeImage || "0");
    if (imageIndex > 0) {{
      showImage(active, imageIndex - 1);
    }} else if (index > 0) {{
      showStep(steps[index - 1].dataset.stepId, true);
    }}
  }});

  next.addEventListener("click", (event) => {{
    event.preventDefault();
    if (next.getAttribute("aria-disabled") === "true") return;

    const index = activeStepIndex();
    const active = steps[index];
    const imageIndex = Number(active.dataset.activeImage || "0");
    const imageCount = imagesFor(active).length;
    if (imageIndex < imageCount - 1) {{
      showImage(active, imageIndex + 1);
    }} else if (index < steps.length - 1) {{
      showStep(steps[index + 1].dataset.stepId, true);
    }}
  }});

  window.addEventListener("hashchange", () => showStep(window.location.hash.slice(1), false));
  window.addEventListener("resize", () => {{
    fitLayoutToViewport();
    updateControls();
  }});
  window.addEventListener("orientationchange", () => {{
    setTimeout(() => {{
      fitLayoutToViewport();
      updateControls();
    }}, 100);
  }});
  buildFlatToc();
  fitLayoutToViewport();
  showStep(window.location.hash.slice(1), false);
}}());
</script>
"""

    def _render_step(self, step: Step, index: int, total: int) -> str:
        images = "\n".join(
            f'<img data-zoduki-image data-src="{self._escape_attr(image.src)}" data-alt="{self._escape_attr(image.alt)}" data-color="{self._escape_attr(image.color)}" hidden>'
            for image in step.images
        )
        thumbs = "\n".join(
            (
                f'<button class="zoduki__thumb" type="button" data-zoduki-thumb data-image-index="{image_index}" '
                f'style="{self._image_color_style(image.color)}" '
                f'aria-label="Show image {image_index + 1} of {len(step.images)}">'
                f'<img src="{self._escape_attr(image.src)}" alt="{self._escape_attr(image.alt)}"></button>'
            )
            for image_index, image in enumerate(step.images)
        )
        first_image = step.images[0] if step.images else None
        main_image = (
            f'<a href="{self._escape_attr(first_image.src)}" class="zoduki__main-image" style="{self._image_color_style(first_image.color)}" target="_blank" rel="noopener">'
            f'<img data-zoduki-main src="{self._escape_attr(first_image.src)}" alt="{self._escape_attr(first_image.alt)}"></a>'
            if first_image
            else '<div class="zoduki__main-image"><span class="zoduki__placeholder">No image for this step</span></div>'
        )
        parent = self._escape_attr(" / ".join(step.parents))
        title = self._escape_text(step.title)
        title_attr = self._escape_attr(step.title)
        slug = self._escape_attr(step.slug)
        aliases = self._escape_attr(" ".join(step.aliases))
        toc_slug = self._escape_attr(step.toc_slug)

        return f"""
<section class="zoduki__step" data-zoduki-step data-step-id="{slug}" data-step-aliases="{aliases}" data-toc-id="{toc_slug}" data-step-title="{title_attr}" data-parent="{parent}" data-active-image="0" hidden>
  <div class="zoduki__media">
    {main_image}
    <div class="zoduki__thumbs" aria-label="Step images">{thumbs}</div>
    {images}
  </div>
  <div class="zoduki__copy">
    <p>Step {index + 1} of {total}</p>
    <h2>{title}</h2>
    {step.text_html}
  </div>
</section>
"""

    def _text_content(self, html: str) -> str:
        return html_lib.unescape(_TAG_RE.sub("", html)).strip()

    def _markdown_heading_text(self, markdown: str) -> str:
        text = re.sub(r"\s+\{[:#.\w\s=\"'-]+\}\s*$", "", markdown).strip()
        text = re.sub(r"`([^`]*)`", r"\1", text)
        text = re.sub(r"!\[([^\]]*)\]\([^)]+\)", r"\1", text)
        text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
        return self._text_content(text)

    def _slugify(self, value: str) -> str:
        slug = _SLUG_RE.sub("-", value.lower()).strip("-")
        return slug or "step"

    def _unique_slug(self, base: str, used_slugs: set[str]) -> str:
        slug = self._slugify(base)
        index = 2
        while slug in used_slugs:
            slug = f"{self._slugify(base)}-{index}"
            index += 1
        used_slugs.add(slug)
        return slug

    def _image_color_style(self, color: str) -> str:
        if not color:
            return ""
        return self._escape_attr(f"--zoduki-image-color: {color};")

    def _escape_attr(self, value: str) -> str:
        return html_lib.escape(value, quote=True)

    def _escape_text(self, value: str) -> str:
        return html_lib.escape(value, quote=False)
