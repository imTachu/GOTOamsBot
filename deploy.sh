#!/usr/bin/env bash

set -e -u -o pipefail

cd "$(dirname "${0}")"

# Claim a non-existent temporary file.
ARTIFACT="$(mktemp)"
rm -f "$ARTIFACT"
trap 'rm -f -- "$ARTIFACT"' INT TERM HUP EXIT

# Package the code.
zip -r "${ARTIFACT}" botcontrol.py resources/talks.py resources/speakers.py resources/__init__.py

# Deploy the code.
aws lambda update-function-code \
  --region us-east-1 \
  --function-name arn:aws:lambda:us-east-1:547437659712:function:botcontrol \
  --zip-file "fileb://${ARTIFACT}"
