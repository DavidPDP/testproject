#!/usr/bin/env bash
set -e 

. /var/lib/jenkins/.virtualenvs/testproject/bin/activate

PYTHONPATH=. py.test --junitxml=python_tests.xml
