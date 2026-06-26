#! /bin/bash

set -e

cd "$(dirname "$0")"

rm -rf build/ dist/ diagnosticism.egg-info/

python3 -m build
python3 -m twine check dist/*
