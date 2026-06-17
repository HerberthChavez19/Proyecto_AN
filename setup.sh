#!/usr/bin/env bash

set -euo pipefail

# Create a local virtual environment for the project.
python3 -m venv .venv

# Activate the environment for the current shell session.
source .venv/bin/activate

# Keep packaging tools up to date before installing dependencies.
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

echo "Entorno virtual listo en .venv"

