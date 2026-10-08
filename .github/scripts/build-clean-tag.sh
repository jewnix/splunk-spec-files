#!/usr/bin/env bash
set -euo pipefail

if [ $# -ne 1 ]; then
  echo "usage: $0 <version-tag>" >&2
  exit 1
fi

tag="$1"
branch="refs/heads/${CLEAN_BRANCH:-clean}"
clean_tag="refs/tags/clean/$tag"
version_re='^#[[:space:]]*Version [0-9][0-9.]*[[:space:]]*$'
logs_re='^(\[\.\./scripts/logs/[^]]*)_[A-Z][a-z]{2}_[A-Z][a-z]{2}_+[0-9]{1,2}_[0-9]{2}:[0-9]{2}:[0-9]{2}_[0-9]{4}_[0-9]+\]'

source_commit=$(git rev-parse --verify "refs/tags/$tag^{commit}")

work=$(mktemp -d)
cleanup() {
  git worktree remove --force "$work" >/dev/null 2>&1 || true
  rm -rf "$work"
}
trap cleanup EXIT

git worktree add --quiet --detach "$work" "$source_commit"
git -C "$work" rm -r --quiet --ignore-unmatch .github

git -C "$work" grep -lzE -e "$version_re" -e "$logs_re" -- . ':!*.md' \
  | (cd "$work" && xargs -0 -r sed -E -i -e "/$version_re/d" -e "s#$logs_re#\\1]#")

git -C "$work" add -A
tree=$(git -C "$work" write-tree)

if existing=$(git rev-parse -q --verify "$clean_tag^{tree}") && [ "$existing" = "$tree" ]; then
  echo "clean/$tag is already up to date"
  exit 0
fi

parent_args=()
if parent=$(git rev-parse -q --verify "$branch"); then
  parent_args=(-p "$parent")
fi

export GIT_AUTHOR_NAME GIT_AUTHOR_EMAIL GIT_AUTHOR_DATE GIT_COMMITTER_NAME GIT_COMMITTER_EMAIL GIT_COMMITTER_DATE
GIT_AUTHOR_NAME=$(git log -1 --format=%an "$source_commit")
GIT_AUTHOR_EMAIL=$(git log -1 --format=%ae "$source_commit")
GIT_AUTHOR_DATE=$(git log -1 --format=%aI "$source_commit")
GIT_COMMITTER_NAME=$GIT_AUTHOR_NAME
GIT_COMMITTER_EMAIL=$GIT_AUTHOR_EMAIL
GIT_COMMITTER_DATE=$(git log -1 --format=%cI "$source_commit")

commit=$(git commit-tree "$tree" "${parent_args[@]}" \
  -m "Splunk $tag without version headers and generated stanza suffixes" \
  -m "Source: $source_commit")

git update-ref "$branch" "$commit"
git update-ref "$clean_tag" "$commit"
echo "clean/$tag -> $commit"
