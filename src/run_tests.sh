#!/bin/zsh

echo '---------->>> RUNNING PYTEST'
pytest

echo '---------->>> RUNNING FLAKE8'
flake8
