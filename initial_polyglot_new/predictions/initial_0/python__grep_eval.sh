#!/bin/bash
set -uxo pipefail
pytest -rA --tb=long
