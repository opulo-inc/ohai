# zoduki

MkDocs plugin that turns assembly guides into Dozuki-style step-by-step pages. Works with [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) with no theme overrides required.

Each step shows one action at a time: images and thumbnails on the left, instructions on the right, with Previous/Next navigation pinned to the bottom of the viewport.

## Install

In your MkDocs project:

```bash
uv add mkdocs-zoduki mkdocs-material
```

Add to `mkdocs.yml`:

```yaml
plugins:
  - search
  - zoduki:
      enabled_by_default: true
      step_heading_level: 3
```

Run the site:

```bash
uv run mkdocs serve
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

---

## Development

Clone the repo and install everything with [uv](https://docs.astral.sh/uv/):

```bash
git clone https://github.com/sphawes/zoduki.git
cd zoduki
uv sync
```

Run tests against a local MkDocs project (or the included example):

```bash
uv run mkdocs build
uv run mkdocs serve
```

## Publishing to PyPI

This project uses **uv only** for building and publishing. No `pip`, `build`, `twine`, or `setuptools` needed.

### One-time setup

1. Install uv if you haven't: https://docs.astral.sh/uv/getting-started/installation/
2. Create a PyPI API token at https://pypi.org/manage/account/token/
3. Store it locally (optional, avoids re-pasting):

```bash
export UV_PUBLISH_TOKEN="pypi-..."
```

### Build

```bash
uv build
```

Artifacts land in `dist/` (wheel + sdist).

### Test on TestPyPI first (recommended)

Add a TestPyPI index to `pyproject.toml`:

```toml
[[tool.uv.index]]
name = "testpypi"
url = "https://test.pypi.org/simple/"
publish-url = "https://test.pypi.org/legacy/"
explicit = true
```

Publish:

```bash
export UV_PUBLISH_TOKEN="pypi-..."   # TestPyPI token
uv publish --index testpypi
```

Verify in another project:

```bash
uv add --index https://test.pypi.org/simple/ mkdocs-zoduki
```

### Publish to PyPI

Bump `version` in `pyproject.toml`, then:

```bash
uv build
uv publish
```

If `UV_PUBLISH_TOKEN` is set, no other credentials are needed.

### GitHub Actions (optional)

Create `.github/workflows/publish.yml`:

```yaml
name: Publish

on:
  push:
    tags:
      - "v*"

jobs:
  publish:
    runs-on: ubuntu-latest
    environment:
      name: pypi
      url: https://pypi.org/p/mkdocs-zoduki
    permissions:
      id-token: write
      contents: read
    steps:
      - uses: actions/checkout@v4
      - uses: astral-sh/setup-uv@v5
      - run: uv build
      - run: uv publish
```

Set up [PyPI trusted publishing](https://docs.pypi.org/trusted-publishers/) for `sphawes/zoduki` so no API token secret is required in CI.

Release workflow:

```bash
# bump version in pyproject.toml first
git commit -am "Release 0.1.1"
git tag v0.1.1
git push && git push --tags
```

The workflow builds and publishes automatically.

## Standalone `pyproject.toml`

When splitting this out of another repo, the package root should look like:

```
zoduki/
├── LICENSE
├── README.md
├── pyproject.toml
└── src/
    └── zoduki/
        ├── __init__.py
        └── plugin.py
```

Minimal `pyproject.toml`:

```toml
[project]
name = "mkdocs-zoduki"
version = "0.1.0"
description = "MkDocs plugin for Dozuki-style step-by-step assembly guides"
readme = "README.md"
license = "MIT"
requires-python = ">=3.10"
dependencies = [
    "mkdocs>=1.6",
    "beautifulsoup4>=4.12",
]

[project.urls]
Homepage = "https://github.com/sphawes/zoduki"
Repository = "https://github.com/sphawes/zoduki"

[project.entry-points."mkdocs.plugins"]
zoduki = "zoduki:ZodukiPlugin"

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["src/zoduki"]
```

Consumers install with `uv add mkdocs-zoduki`. The plugin name in `mkdocs.yml` remains `zoduki`.
