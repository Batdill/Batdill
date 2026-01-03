# List Open Pull Requests

This repository contains scripts to list the latest open pull requests for a GitHub repository.

## Prerequisites

- [GitHub CLI (gh)](https://cli.github.com/) installed and authenticated

## Usage

### Using the Bash Script

```bash
./list_prs.sh <owner> <repo>
```

Example:
```bash
./list_prs.sh Batdill Batdill
```

### Using the Python Script

```bash
python3 list_open_prs.py <owner> <repo>
```

Example:
```bash
python3 list_open_prs.py Batdill Batdill
```

## Authentication

Make sure you have the GitHub CLI authenticated before running these scripts:

```bash
gh auth login
```

Or set the `GH_TOKEN` environment variable with a GitHub personal access token:

```bash
export GH_TOKEN=your_github_token
```

## Output

The scripts will display a formatted list of open pull requests including:
- PR number
- Title
- Author
- Last updated date

## Example Output

```
Open Pull Requests in Batdill/Batdill:

#      Title                                              Author               Updated             
------------------------------------------------------------------------------------------------
1      [WIP] List latest open pull requests              Copilot              2026-01-03          

Total: 1 open pull request(s)
```