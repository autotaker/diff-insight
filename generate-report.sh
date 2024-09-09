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
TODAY=$(date +%Y%m%d)

if [ "$LAST_SHA" != "$HEAD_SHA" ]; then
  pipenv run python src/main.py generate-report "${ORG}" "${REPO}" "${LAST_SHA}" "${HEAD_SHA}" work/report.md
  pandoc -i work/report.md -o work/report.html -f markdown+hard_line_breaks --template template.html
  mv work/report.html "docs/report-${TODAY}.html"
  echo "HEAD_SHA: $HEAD_SHA"
  echo $HEAD_SHA > last-commit.sha
fi

