# zoduki

MkDocs plugin that turns assembly guides into step-by-step pages. Works with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) with no theme overrides required.

Each step shows one action at a time: images and thumbnails on the left, instructions on the right, with Previous/Next navigation pinned to the bottom of the viewport.

## Setup

Add zoduki to `mkdocs.yml`:

```yaml
plugins:
  - search
  - zoduki:
      enabled_by_default: true
      step_heading_level: 3
```

Install the package (editable install from this repo):

```bash
uv sync
```

## Writing a guide

Structure your Markdown like this:

- The page title (`#` or Setext) is the guide name shown in the breadcrumb bar.
- `##` headings group steps into subsections in the left nav.
- `###` headings each become one step. Everything under a `###` (bullets, images, text) stays in that step.

```markdown
# X Gantry Assembly

## Prepare back plate

### Install fasteners

* Insert 4x `m5-hex-lock-nut` into the pockets shown.

    ![Nut pockets](images/nuts.webp)

* Add a drop of `blue-loctite` to each pocket.

### Inspect alignment

* Verify the plate sits flush against the datum surface.
```

### Images

Put images under the bullet they illustrate (indented under the list item). Images are moved to the left-side gallery for that step. The **Next** button cycles through all images in the current step before advancing to the next step.

### Bullet colors

Bullets that contain an image get a colored box and matching image border automatically. Override with an inline directive:

```markdown
* Install the bracket {color=blue}

    ![Bracket](images/bracket.webp)

* Text-only note with no image gets a neutral box.

* Disable coloring explicitly {color=none}
```

Named colors: `blue`, `green`, `orange`, `purple`, `red`, `teal`, `yellow`, `pink`. Hex values like `#3b82f6` also work.

## Per-page control

Disable zoduki on a specific page with front matter:

```yaml
---
zoduki: false
---
```

Or leave `enabled_by_default: false` in the plugin config and opt in per page:

```yaml
---
zoduki: true
---
```

## Options

| Option | Default | Description |
|--------|---------|-------------|
| `enabled_by_default` | `false` | Apply zoduki to every page unless overridden |
| `page_meta_key` | `zoduki` | Front matter key for per-page enable/disable |
| `step_heading_level` | `3` | Heading level that starts a new step (`###`) |
| `min_steps` | `2` | Minimum steps required before transforming a page |

## Deep links

Each step gets a stable URL hash from its heading, e.g. `#install-fasteners`. The left nav links directly to steps and stays in sync with Previous/Next navigation.
