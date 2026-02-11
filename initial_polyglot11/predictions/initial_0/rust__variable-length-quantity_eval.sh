#!/bin/bash
set -uxo pipefail
cargo test -- --include-ignored
