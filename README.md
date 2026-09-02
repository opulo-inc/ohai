# ohai
Open Hardware Assembly Instructions for Opulo machines

## Install

OHAI uses mkdocs with the mkdocs-material theme. This guide assumes you're running on a Mac.

1. [Install Homebrew](https://brew.sh/) if you have not already.

2. Install `uv` using `brew install uv`.

3. Install [Git LFS](https://git-lfs.com/) if you have not already, e.g. `brew install git-lfs`. This repo stores images and 3D files (`.jpg`, `.png`, `.webp`, `.step`, `.stl`) via LFS, so without it these files will only download as small text pointers and images won't show up.

4. Open Terminal and `cd` into the ohai directory. 

    `cd ~/path/to/ohai`

5. If you already had the repo cloned before installing Git LFS, or if images aren't showing up, pull the LFS files:

    `git lfs install`

    `git lfs pull`

6. Create a virtual environment with uv.

    `uv venv`

7. Install dependencies with uv:

    `uv sync`

## Running Locally

1. While in the ohai directory, activate the virtual environment.

    `source .venv/bin/activate`

2. Run mkdocs locally.

    `mkdocs serve`

3. OHAI is now being hosted locally at localhost:8000. You can `CTRL+C` to cancel.