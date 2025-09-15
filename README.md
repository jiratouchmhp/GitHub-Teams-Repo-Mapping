# GitHub Team-Repository Mapping Tool

**Simple tool for managing GitHub team permissions at scale**

Map teams to repositories, analyze permissions, and bulk assign access across your GitHub organization.

## What This Tool Does

- **Discover**: List all teams and repositories in your organization
- **Analyze**: Generate detailed permission mappings
- **Manage**: Bulk assign permissions using CSV files
- **Export**: Save results in JSON format

## Quick Start Guide

### Step 1: Install Dependencies

```bash
pip3 install requests
```

### Step 2: Get GitHub Token

1. Go to [GitHub Settings → Personal Access Tokens](https://github.com/settings/tokens)
2. Click "Generate new token (classic)"
3. Name it (e.g., "Team Repo Mapper")
4. Select these permissions:
   - `read:org` - Read organization data
   - `repo` - Repository access
   - `admin:org` - Manage teams and permissions
5. Copy the generated token

### Step 3: Run the Tool

```bash
python3 quick_start.py
```

Enter your token and organization name when prompted.

## Menu Options

**Option 1: Quick Overview**
- Safe read-only exploration
- Shows teams and repositories summary

**Option 2: Complete Mapping**
- Generates full permission mapping
- Exports detailed JSON report

**Option 3: Bulk Assignment**
- Upload CSV file with permission changes
- Validates before applying

**Option 4: Generate Templates**
- Creates CSV template files
- Example formats included

## Bulk Permission Management

### Create CSV File

1. Generate template:
   ```bash
   python3 quick_start.py  # Choose Option 4
   ```

2. Copy and edit:
   ```bash
   cp templates/bulk_assignments_template.csv my_permissions.csv
   ```

### CSV Format

```csv
team_slug,repo_owner,repo_name,permission
developers,myorg,frontend-app,push
qa-team,myorg,frontend-app,pull
devops,myorg,infrastructure,admin
```

### Permission Levels

| Level | Access |
|-------|--------|
| `pull` | Read only |
| `triage` | Read + manage issues |
| `push` | Read + write code |
| `maintain` | Push + settings |
| `admin` | Full access |

## Project Structure

```
github-team-repo-mapping/
├── quick_start.py                      # Main entry point
├── github_team_repo_mapper.py          # Core functionality
├── requirements.txt                    # Dependencies
└── templates/
    ├── bulk_assignments_template.csv   # CSV template
    └── .env_template                   # Environment template
```

## Authentication

### Interactive (Recommended)
```bash
python3 quick_start.py
# Enter credentials when prompted
```

### Environment Variables
```bash
export GITHUB_TOKEN="your_token"
export GITHUB_ORG="your_org"
python3 quick_start.py
```

### .env File
```bash
cp templates/.env_template .env
# Edit .env with your credentials
```

## Troubleshooting

| Error | Solution |
|-------|----------|
| 401 Authentication | Check token validity |
| 403 Forbidden | Verify organization access |
| 404 Not Found | Confirm org/repo names |
| Rate Limiting | Tool handles automatically |

## Security Notes

- Never commit tokens to git
- Use minimal required permissions
- Rotate tokens regularly
- Test with small changes first

## Usage Examples

### Explore Organization
```bash
python3 quick_start.py  # Option 1
```

### Generate Report
```bash
python3 quick_start.py  # Option 2
```

### Bulk Update Permissions
```bash
# 1. Create CSV
cp templates/bulk_assignments_template.csv permissions.csv
# Edit permissions.csv

# 2. Apply changes
python3 quick_start.py  # Option 3
```

## Support

- [GitHub API Documentation](https://docs.github.com/en/rest)
- [Token Creation Guide](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)

---

**Ready to start?** Run `python3 quick_start.py` and choose Option 1!
