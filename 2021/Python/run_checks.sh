#!/bin/bash
CURRENT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
echo "--- Running pylint..."
poetry run pylint "$CURRENT_DIR" --rcfile "$CURRENT_DIR/../../.pylintrc"
echo "--- Running mypy..."
poetry run mypy "$CURRENT_DIR"
echo "--- Running pytest..."
poetry run pytest --doctest-modules "$CURRENT_DIR"
