#!/usr/bin/env python3
"""
Script to list the latest open pull requests for a GitHub repository.
"""

import json
import subprocess
import sys
import os

def list_open_prs(owner, repo):
    """
    List open pull requests using the GitHub API.
    
    Args:
        owner: Repository owner (username or organization)
        repo: Repository name
    """
    try:
        # Use curl to fetch open PRs from GitHub API
        api_url = f"https://api.github.com/repos/{owner}/{repo}/pulls?state=open&sort=updated&direction=desc"
        
        # Check if GH_TOKEN or GITHUB_TOKEN is available for authentication
        token = os.environ.get('GH_TOKEN') or os.environ.get('GITHUB_TOKEN')
        
        if token:
            # Use stdin to pass the header to avoid token exposure in process list
            cmd = ["curl", "-s", "-H", "@-", api_url]
            header = f"Authorization: token {token}"
            result = subprocess.run(cmd, input=header, capture_output=True, text=True, check=True)
        else:
            cmd = ["curl", "-s", api_url]
            result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        
        prs = json.loads(result.stdout)
        
        # Check if we got an error message from GitHub API
        if isinstance(prs, dict) and 'message' in prs:
            print(f"Error from GitHub API: {prs['message']}", file=sys.stderr)
            sys.exit(1)
        
        if not prs:
            print(f"No open pull requests found in {owner}/{repo}")
            return
        
        print(f"Open Pull Requests in {owner}/{repo}:\n")
        print(f"{'#':<6} {'Title':<50} {'Author':<20} {'Updated':<20}")
        print("-" * 96)
        
        for pr in prs:
            number = pr['number']
            title = pr['title'][:47] + "..." if len(pr['title']) > 50 else pr['title']
            author = pr['user']['login']
            updated = pr['updated_at'][:10]  # Just the date part
            
            print(f"{number:<6} {title:<50} {author:<20} {updated:<20}")
        
        print(f"\nTotal: {len(prs)} open pull request(s)")
        
    except subprocess.CalledProcessError as e:
        print(f"Error: Failed to fetch pull requests from GitHub API.", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"Error: Failed to parse GitHub API response. {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

def main():
    """Main entry point."""
    if len(sys.argv) != 3:
        print("Usage: python list_open_prs.py <owner> <repo>")
        print("Example: python list_open_prs.py Batdill Batdill")
        sys.exit(1)
    
    owner = sys.argv[1]
    repo = sys.argv[2]
    
    list_open_prs(owner, repo)

if __name__ == "__main__":
    main()
