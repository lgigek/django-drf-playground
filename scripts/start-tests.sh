#!/usr/bin/env bash
python -m pytest tests -n auto -vv --cov=. --doctest-modules --junitxml=junit/test-results.xml --cov-report=xml --cov-report=html --cov-report=term --cov-append