#!/usr/bin/env bash
set -e 

. /var/lib/jenkins/.virtualenvs/testproject/bin/activate

PYTHONPATH=. py.test --junitxml=python_tests.xml
PYTHONPATH=. py.test --cov-report xml --cov=../testproject
PYTHONPATH=. py.test --cov-report html --cov=../testproject
