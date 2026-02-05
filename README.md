# ohai
Open Hardware Assembly Instructions for Opulo machines

## Install

OHAI uses mkdocs with the mkdocs-material theme. This guide assumes you're running on a Mac.

1. [Install Homebrew](https://brew.sh/) if you have not already.

2. Install `uv` using `brew install uv`.

3. Open Terminal and `cd` into the ohai directory. 

    `cd ~/path/to/ohai`

4. Create a virtual environment with uv.

    `uv venv`

5. Install dependencies with uv:

    `uv sync`

## Running Locally

1. While in the ohai directory, activate the virtual environment.

    `source .venv/bin/activate`

2. Run mkdocs locally.

    `mkdocs serve`

3. OHAI is now being hosted locally at localhost:8000. You can `CTRL+C` to cancel.