#! /bin/bash

set -e

cd "$(dirname "$0")"

if [ ! -d .venv ]; then
    uv venv
fi

rm -rf build/ dist/ diagnosticism.egg-info/

uv pip install build twine
uv run python -m build
uv run twine check dist/*
