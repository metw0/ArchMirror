#!/bin/bash
echo "Installing ArchMirror dependencies..."
python -m venv .venv
./.venv/bin/pip install tomli tomli-w
echo "Installation complete !"