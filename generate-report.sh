#!/bin/bash

cd "$(dirname "$0")"

set -euo pipefail

if [[ "${DEBUG:-}" ]]; then
  set -x
fi

if [[ ! -d work ]]; then
  mkdir work
fi

LAST_SHA=$(cat last-commit.sha)
ORG=MicrosoftDocs
REPO=azure-ai-docs
pipenv run python src/main.py fetch-commit "${ORG}" "${REPO}" main work/head.json
HEAD_SHA=$(jq -r '.sha' work/head.json)
MONTH=$(date +%Y%m)

if [ "$LAST_SHA" != "$HEAD_SHA" ]; then
  pipenv run python src/main.py generate-report \
    "${ORG}" "${REPO}" "${LAST_SHA}" "${HEAD_SHA}" \
    site/posts/%Y%m/report-%Y%m%d-{category}.md
  echo "HEAD_SHA: $HEAD_SHA"
  echo $HEAD_SHA > last-commit.sha
fi

