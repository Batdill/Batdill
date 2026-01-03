#!/usr/bin/env python3
"""
Demo: List open pull requests for Batdill/Batdill repository
This is a demonstration showing the current open PRs.
"""

print("Open Pull Requests in Batdill/Batdill:")
print()
print(f"{'#':<6} {'Title':<50} {'Author':<20} {'Updated':<20}")
print("-" * 96)
print(f"{1:<6} {'[WIP] List latest open pull requests':<50} {'Copilot':<20} {'2026-01-03':<20}")
print()
print("Total: 1 open pull request(s)")
print()
print("Note: This is a demo output. To see live data, use:")
print("  ./list_prs.sh Batdill Batdill")
print("or")
print("  python3 list_open_prs.py Batdill Batdill")
print()
print("Make sure GitHub CLI is authenticated first!")
