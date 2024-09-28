#!/bin/bash

cd "$(dirname "$0")"

set -euo pipefail

if [[ "${DEBUG:-}" ]]; then
  set -x
fi

ORG=MicrosoftDocs
REPO=azure-ai-docs

while IFS= read -r line; do
  DATE=$(echo "$line" | awk '{print $1}')
  BASE_SHA=$(echo "$line" | awk '{print $2}')
  HEAD_SHA=$(echo "$line" | awk '{print $3}')
  
  TODAY=$DATE pipenv run python src/main.py generate-report "$ORG" "$REPO" "$BASE_SHA" "$HEAD_SHA" \
    site/posts/%Y%m/report-%Y%m%d-{category}.md
done < daily-commits.sha


