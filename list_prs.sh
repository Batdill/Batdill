#!/bin/bash
# Script to list the latest open pull requests for a GitHub repository
# Requires: GitHub CLI (gh) to be installed and authenticated

set -e

# Check if required arguments are provided
if [ $# -ne 2 ]; then
    echo "Usage: $0 <owner> <repo>"
    echo "Example: $0 Batdill Batdill"
    exit 1
fi

OWNER=$1
REPO=$2

echo "Fetching open pull requests for $OWNER/$REPO..."
echo ""

# Use GitHub CLI to list open PRs
gh pr list \
    --repo "$OWNER/$REPO" \
    --state open \
    --json number,title,author,createdAt,updatedAt \
    --template '{{range .}}{{printf "#%-5d %-50s %-20s %s\n" .number .title .author.login (.updatedAt | timeago)}}{{end}}'

echo ""
echo "Done!"
