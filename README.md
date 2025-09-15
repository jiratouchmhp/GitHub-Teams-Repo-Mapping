# 🚀 GitHub Team-Repository Mapping Tool 🚀 # 



**Simple, powerful tool for managing GitHub team permissions at scale**



Easily map teams to repositories, analyze permissions, and bulk assign access across your GitHub organization.



## ✨ What This Tool DoesEasily map teams to repositories, analyze permissions, and bulk assign access across your GitHub organization. ##



- 🔍 **Discover**: See all teams and repositories in your organization

- 📊 **Analyze**: Generate detailed permission mappings  

- 📋 **Manage**: Bulk assign permissions using CSV files

- 📄 **Export**: Save results in JSON format



## 🚀 Quick Start (2 Steps!)

- 🔍 **Discover**: See all teams and repositories in your organizationEasily map teams to repositories, analyze permissions, and bulk assign access across your GitHub organization.

### 1. Install Python Dependency

- 📊 **Analyze**: Generate detailed permission mappings  

```bash

pip3 install requests- 📋 **Manage**: Bulk assign permissions using CSV files

```

- 📄 **Export**: Save results in JSON format

### 2. Run the Tool

## ✨ What This Tool Does

```bash

python3 quick_start.py## 🚀 Quick Start (2 Steps!)

```



**That's it!** The tool will ask for your GitHub token and organization name when you run it.

### 1. Install Python Dependency

### What You'll See:

```bash- 🔍 **Discover**: See all teams and repositories in your organizationEasily map teams to repositories, analyze permissions, and bulk assign access across your GitHub organization.Easily map teams to repositories, analyze permissions, and bulk assign access across your GitHub organization.

- **Option 1**: Quick overview of teams & repos (safe to explore)

- **Option 2**: Generate complete mapping pip3 install requests

- **Option 3**: Bulk assign permissions from CSV

- **Option 4**: Create template files```- 📊 **Analyze**: Generate detailed permission mappings  



### 🤔 Need a GitHub Token?



**No problem!** Here's how to get one in 2 minutes:### 2. Run the Tool- 📋 **Manage**: Bulk assign permissions using CSV files



1. Go to [GitHub Settings > Developer Settings > Personal Access Tokens](https://github.com/settings/tokens)```bash

2. Click "Generate new token (classic)"

3. Give it a name like "Team Repo Mapper"python3 quick_start.py- 📄 **Export**: Save results in JSON and CSV formats

4. Select these permissions:

   - `read:org` (read organization data)```

   - `repo` (repository access)

   - `admin:org` (manage teams and permissions)## ✨ What This Tool Does## ✨ What This Tool Does

5. Click "Generate token" and copy it

**That's it!** The tool will ask for your GitHub token and organization name when you run it.

**Keep your token safe!** You'll paste it when the tool asks.

## 🚀 Quick Start (2 Steps!)

## 📋 Bulk Permissions Made Easy

### What You'll See:

### Create Your CSV File

- **Option 1**: Quick overview of teams & repos (safe to explore)

```bash

# Copy the template- **Option 2**: Generate complete mapping 

cp templates/bulk_assignments_template.csv my_permissions.csv

- **Option 3**: Bulk assign permissions from CSV### 1. Install Python Dependency

# Edit with your teams and repositories

```- **Option 4**: Create template files



### Example CSV Format```bash- 🔍 **Discover**: See all teams and repositories in your organization- 🔍 **Discover**: See all teams and repositories in your organization



```csv### 🤔 Need a GitHub Token?

team_slug,repo_owner,repo_name,permission

developers,myorg,frontend-app,push**No problem!** Here's how to get one in 2 minutes:pip3 install requests

qa-team,myorg,frontend-app,pull

devops,myorg,infrastructure,admin

```

1. Go to [GitHub Settings > Developer Settings > Personal Access Tokens](https://github.com/settings/tokens)```- 📊 **Analyze**: Generate detailed permission mappings  - 📊 **Analyze**: Generate detailed permission mappings  

### Apply the Changes

2. Click "Generate new token (classic)"

```bash

python3 quick_start.py3. Give it a name like "Team Repo Mapper"

# Choose option 3, select your CSV file

```4. Select these permissions:



The tool validates your CSV and shows you exactly what will change before applying.   - `read:org` (read organization data)### 2. Run the Tool- 📋 **Manage**: Bulk assign permissions using CSV files- 📋 **Manage**: Bulk assign permissions using CSV files



## 🎯 Common Use Cases   - `repo` (repository access)



| Task | Steps |   - `admin:org` (manage teams and permissions)```bash

|------|-------|

| **See what I have** | Run quick_start.py → Option 1 |5. Click "Generate token" and copy it

| **Full analysis** | Run quick_start.py → Option 2 |

| **Bulk assign permissions** | Create CSV → Run quick_start.py → Option 3 |python3 quick_start.py- 📄 **Export**: Save results in JSON and CSV formats- 📄 **Export**: Save results in JSON and CSV formats

| **Get templates** | Run quick_start.py → Option 4 |

**Keep your token safe!** You'll paste it when the tool asks.

## 🔒 Permission Levels

```

| Level | Access |

|-------|--------|## 📋 Bulk Permissions Made Easy

| `pull` | Read only |

| `triage` | Read + manage issues/PRs |

| `push` | Triage + push code |

| `maintain` | Push + repository settings |### Create Your CSV File

| `admin` | Full access |

```bash**That's it!** The tool will ask for your GitHub token and organization name when you run it.

## 📁 Project Structure

# Copy the template

```

github-team-repo-mapping/cp templates/bulk_assignments_template.csv my_permissions.csv## 🚀 Quick Start (3 Steps)## 🚀 Quick Start (3 Steps)

├── quick_start.py                      # 🚀 Main entry point - START HERE

├── github_team_repo_mapper.py          # Core functionality# Edit with your teams and repositories

├── requirements.txt                    # Python dependencies

├── README.md                           # This guide```### What You'll See:

└── templates/                          # 📝 Ready-to-use templates

    ├── bulk_assignments_template.csv   # CSV template for bulk assignments

    └── .env_template                   # Environment configuration template

```### Example CSV Format- **Option 1**: Quick overview of teams & repos (safe to explore)



## 💡 Pro Tips```csv



- ✅ **Start small**: Test with a few assignments firstteam_slug,repo_owner,repo_name,permission- **Option 2**: Generate complete mapping 

- ✅ **Validate first**: The tool checks your CSV before applying

- ✅ **Backup current state**: Generate a mapping before making changesdevelopers,myorg,frontend-app,push

- ✅ **Use team slugs**: Lowercase with hyphens (e.g., `frontend-team`)

qa-team,myorg,frontend-app,pull- **Option 3**: Bulk assign permissions from CSV### 1. Setup Credentials### 1. Setup Credentials

## 🔐 Authentication Options

devops,myorg,infrastructure,admin

### Option 1: Interactive (Recommended)

Run `python3 quick_start.py` and enter your token when prompted.```- **Option 4**: Create template files



### Option 2: Environment Variables

```bash

export GITHUB_TOKEN="your_token_here"### Apply the Changes```bash```bash

export GITHUB_ORG="your_org_here"

python3 quick_start.py```bash

```

python3 quick_start.py### 🤔 Don't Have a GitHub Token Yet?

### Option 3: .env File

```bash# Choose option 3, select your CSV file

# Copy template and edit

cp templates/.env_template .env```**No problem!** See [`WHAT_YOU_NEED.md`](WHAT_YOU_NEED.md) for a 5-minute setup guide.# Copy the template and add your details# Copy the template and add your details

# Add your token and org name to .env file

```



## 🆘 Need Help?The tool validates your CSV and shows you exactly what will change before applying.



- **New to this?** Just run `python3 quick_start.py` and choose Option 1 to explore safely

- **Just want to explore?** Run `python3 quick_start.py` → Option 1

- **Need templates?** Run `python3 quick_start.py` → Option 4## 🎯 Common Use Cases## 📋 Bulk Permissions Made Easycp templates/.env_template .envcp templates/.env_template .env



## 📚 Output Formats



### JSON Export| Task | Steps |

The tool exports comprehensive mappings in JSON format with:

- Organization summary|------|-------|

- Repository details with team access

- Team information with repository permissions| **See what I have** | Run quick_start.py → Option 1 |### Create Your CSV File# Edit .env with your GitHub token and organization name# Edit .env with your GitHub token and organization name

- Complete permission matrix

| **Full analysis** | Run quick_start.py → Option 2 |

### Console Output

Clean, formatted reports showing:| **Bulk assign permissions** | Create CSV → Run quick_start.py → Option 3 |```bash

- Summary statistics

- Team listings with member counts| **Get templates** | Run quick_start.py → Option 4 |

- Repository access details

- Permission breakdowns# Copy the template``````



## 🔧 Technical Details## 🔒 Permission Levels



### Requirementscp templates/bulk_assignments_template.csv my_permissions.csv

- Python 3.6+

- `requests` library| Level | Access |

- GitHub Personal Access Token

|-------|--------|# Edit with your teams and repositories

### Rate Limiting

The tool automatically handles GitHub API rate limits and includes respectful delays between requests.| `pull` | Read only |



### Error Handling| `triage` | Read + manage issues/PRs |```

Comprehensive error handling for:

- Network issues| `push` | Triage + push code |

- Authentication failures

- Permission errors| `maintain` | Push + repository settings |### 2. Run the Tool### 2. Run the Tool

- Invalid repository/team names

| `admin` | Full access |

## 🚨 Security Notes

### Example CSV Format

⚠️ **Important Security Considerations:**

## 📁 Project Structure

1. **Token Security**: Never commit tokens to version control

2. **Minimum Permissions**: Use tokens with minimal required permissions```csv```bash```bash

3. **Token Rotation**: Regularly rotate your access tokens

4. **Environment Variables**: Store tokens securely using environment variables```



## 🐛 Troubleshootinggithub-team-repo-mapping/team_slug,repo_owner,repo_name,permission



### Common Issues├── quick_start.py                      # 🚀 Main entry point - START HERE



1. **Authentication Error (401)**├── github_team_repo_mapper.py          # Core functionalitydevelopers,myorg,frontend-app,pushpython quick_start.pypython quick_start.py

   - Verify your token is valid and not expired

   - Ensure token has required permissions├── requirements.txt                    # Python dependencies



2. **Forbidden Error (403)**├── README.md                           # This guideqa-team,myorg,frontend-app,pull

   - Check if you have access to the organization

   - May indicate rate limiting (handled automatically)└── templates/                          # 📝 Ready-to-use templates



3. **Not Found Error (404)**    ├── bulk_assignments_template.csv   # CSV template for bulk assignmentsdevops,myorg,infrastructure,admin``````

   - Verify organization name is correct

   - Ensure repositories/teams exist and you have access    └── .env_template                   # Environment configuration template



## 📝 License``````



This project is provided as-is for educational and demonstration purposes. Please review GitHub's Terms of Service and API guidelines when using this script in production environments.



---## 💡 Pro Tips



**Ready to get started?** Run `python3 quick_start.py` now! 🚀

- ✅ **Start small**: Test with a few assignments first### Apply the Changes

- ✅ **Validate first**: The tool checks your CSV before applying

- ✅ **Backup current state**: Generate a mapping before making changes```bash### 3. Choose Your Task### 3. Choose Your Task

- ✅ **Use team slugs**: Lowercase with hyphens (e.g., `frontend-team`)

python3 quick_start.py

## 🆘 Need Help?

# Choose option 3, select your CSV file- **Option 1**: Quick overview of teams & repos- **Option 1**: Quick overview of teams & repos

- **New to this?** Just run `python3 quick_start.py` and choose Option 1 to explore safely

- **Just want to explore?** Run `python3 quick_start.py` → Option 1```

- **Need templates?** Run `python3 quick_start.py` → Option 4

- **Option 2**: Generate complete mapping - **Option 2**: Generate complete mapping 

---

The tool validates your CSV and shows you exactly what will change before applying.

**Ready to get started?** Run `python3 quick_start.py` now! 🚀
- **Option 3**: Bulk assign permissions from CSV- **Option 3**: Bulk assign permissions from CSV

## 🎯 Common Use Cases

- **Option 4**: Create template files- **Option 4**: Create template files

| Task | Steps |

|------|-------|

| **See what I have** | Run quick_start.py → Option 1 |

| **Full analysis** | Run quick_start.py → Option 2 |That's it! The interactive menu guides you through everything.That's it! The interactive menu guides you through everything.

| **Bulk assign permissions** | Create CSV → Run quick_start.py → Option 3 |

| **Get templates** | Run quick_start.py → Option 4 |



## 🔒 Permission Levels## 📋 Bulk Permissions Made Easy## 📋 Bulk Permissions Made Easy



| Level | Access |

|-------|--------|

| `pull` | Read only |### Create Your CSV File### Create Your CSV File

| `triage` | Read + manage issues/PRs |

| `push` | Triage + push code |```bash```bash

| `maintain` | Push + repository settings |

| `admin` | Full access |# Copy the template# Copy the template



## 📁 Project Structurecp templates/bulk_assignments_template.csv my_permissions.csvcp templates/bulk_assignments_template.csv my_permissions.csv



```# Edit with your teams and repositories# Edit with your teams and repositories

github-team-repo-mapping/

├── quick_start.py              # 🚀 Main entry point - START HERE``````

├── github_team_repo_mapper.py  # Core functionality

├── WHAT_YOU_NEED.md            # 📝 What you need before starting

├── templates/                  # 📝 Ready-to-use templates

│   ├── bulk_assignments_template.csv### Example CSV Format### Example CSV Format

│   ├── .env_template

│   └── README.md```csv```csv

├── samples/                    # 📁 Example files and docs

│   ├── sample_bulk_assignments.csvteam_slug,repo_owner,repo_name,permissionteam_slug,repo_owner,repo_name,permission

│   ├── sample_team_config.csv

│   └── sample_csv_files.mddevelopers,myorg,frontend-app,pushdevelopers,myorg,frontend-app,push

└── utils/                     # 🛠️ Advanced utilities

    ├── csv_utils.pyqa-team,myorg,frontend-app,pullqa-team,myorg,frontend-app,pull

    ├── advanced_utils.py

    └── csv_integration_example.pydevops,myorg,infrastructure,admindevops,myorg,infrastructure,admin

```

``````

## 💡 Pro Tips



- ✅ **Start small**: Test with a few assignments first

- ✅ **Validate first**: The tool checks your CSV before applying### Apply the Changes### Apply the Changes

- ✅ **Backup current state**: Generate a mapping before making changes

- ✅ **Use team slugs**: Lowercase with hyphens (e.g., `frontend-team`)```bash```bash



## 🆘 Need Help?python quick_start.pypython quick_start.py



- **New to this?** Read [`WHAT_YOU_NEED.md`](WHAT_YOU_NEED.md) first# Choose option 3, select your CSV file# Choose option 3, select your CSV file

- **Just want to explore?** Run `python3 quick_start.py` → Option 1

- **Need examples?** Check the `samples/` directory``````

- **Want advanced features?** Explore the `utils/` directory



## 📚 Advanced Features

The tool validates your CSV and shows you exactly what will change before applying.The tool validates your CSV and shows you exactly what will change before applying.

If you need more control, explore the `utils/` directory:



- `csv_utils.py` - CSV validation and conversion tools

- `advanced_utils.py` - Security reports and advanced exports  ## 🔑 GitHub Token Setup## 🔑 GitHub Token Setup

- `csv_integration_example.py` - Detailed CSV workflow examples



---

1. Go to [GitHub Settings > Tokens](https://github.com/settings/tokens)1. Go to [GitHub Settings > Tokens](https://github.com/settings/tokens)

**Ready to get started?** Run `python3 quick_start.py` now! 🚀
2. Create a Personal Access Token with these permissions:2. Create a Personal Access Token with these permissions:

   - `read:org` - Read organization data   - `read:org` - Read organization data

   - `repo` - Repository access   - `repo` - Repository access

   - `admin:org` - Organization administration   - `admin:org` - Organization administration



## 📁 Project Structure## 📁 Project Structure



``````

github-team-repo-mapping/github-team-repo-mapping/

├── quick_start.py              # 🚀 Main entry point - START HERE├── quick_start.py              # 🚀 Main entry point - START HERE

├── github_team_repo_mapper.py  # Core functionality├── github_team_repo_mapper.py  # Core functionality

├── templates/                  # 📝 Get started templates├── templates/                  # 📝 Get started templates

│   ├── bulk_assignments_template.csv│   ├── bulk_assignments_template.csv

│   ├── .env_template│   ├── .env_template

│   └── README.md│   └── README.md

├── samples/                    # 📁 Example files and docs├── samples/                    # 📁 Example files and docs

│   ├── sample_bulk_assignments.csv│   ├── sample_bulk_assignments.csv

│   ├── sample_team_config.csv│   ├── sample_team_config.csv

│   └── sample_csv_files.md│   └── sample_csv_files.md

└── utils/                     # 🛠️ Advanced utilities└── utils/                     # 🛠️ Advanced utilities

    ├── csv_utils.py    ├── csv_utils.py

    ├── advanced_utils.py    ├── advanced_utils.py

    └── csv_integration_example.py    └── csv_integration_example.py

``````



## 🎯 Common Use Cases## 🎯 Common Use Cases



| Task | Steps || Task | Steps |

|------|-------||------|-------|

| **See what I have** | Run quick_start.py → Option 1 || **See what I have** | Run quick_start.py → Option 1 |

| **Full analysis** | Run quick_start.py → Option 2 || **Full analysis** | Run quick_start.py → Option 2 |

| **Bulk assign permissions** | Create CSV → Run quick_start.py → Option 3 || **Bulk assign permissions** | Create CSV → Run quick_start.py → Option 3 |

| **Get templates** | Run quick_start.py → Option 4 || **Get templates** | Run quick_start.py → Option 4 |



## 🔒 Permission Levels## 🔒 Permission Levels



| Level | Access || Level | Access |

|-------|--------||-------|--------|

| `pull` | Read only || `pull` | Read only |

| `triage` | Read + manage issues/PRs || `triage` | Read + manage issues/PRs |

| `push` | Triage + push code || `push` | Triage + push code |

| `maintain` | Push + repository settings || `maintain` | Push + repository settings |

| `admin` | Full access || `admin` | Full access |



## 💡 Pro Tips ## 



- ✅ **Start small**: Test with a few assignments first

- ✅ **Validate first**: The tool checks your CSV before applying

- ✅ **Backup current state**: Generate a mapping before making changes

- ✅ **Use team slugs**: Lowercase with hyphens (e.g., `frontend-team`)


## 🆘 Need Help? ##



**For beginners**: Just run `python quick_start.py` and follow the menu!**



**For advanced users**: Check out the `utils/` directory for additional tools.**



**For examples**: Look in the `samples/` directory for detailed examples.**



## 📚 Advanced Features ## 



If you need more control, explore the `utils/` directory:


- `csv_utils.py` - CSV validation and conversion tools.

- `advanced_utils.py` - Security reports and advanced exports.

- `csv_integration_example.py` - Detailed CSV workflow examples.



## 🤝 Support## 



- 📖 **Documentation**: Check `samples/sample_csv_files.md` for detailed CSV format docs.

- 🐛 **Issues**: Open an issue on GitHub.  

- 💡 **Feature requests**: We'd love to hear your ideas!.



------


**Ready to get started?** Run `python quick_start.py` now!**
```

## Output Format

### JSON Export

The script generates a comprehensive JSON file with the following structure:

```json
{
  "organization": "your_org",
  "generated_at": "2024-01-15T10:30:00",
  "summary": {
    "total_repositories": 25,
    "total_teams": 8,
    "total_permissions_checked": 200,
    "total_access_granted": 45
  },
  "repositories": {
    "repo-name": {
      "id": 123456,
      "full_name": "org/repo-name",
      "private": true,
      "description": "Repository description",
      "default_branch": "main",
      "teams_with_access": [
        {
          "team_slug": "developers",
          "team_name": "Developers",
          "role_name": "write",
          "permissions": {
            "admin": false,
            "maintain": false,
            "push": true,
            "triage": true,
            "pull": true
          }
        }
      ]
    }
  },
  "teams": {
    "developers": {
      "id": 789012,
      "name": "Developers",
      "slug": "developers",
      "description": "Development team",
      "privacy": "closed",
      "default_permission": "push",
      "members_count": 12,
      "repos_count": 8,
      "repositories_with_access": [...]
    }
  },
  "permissions_matrix": [
    {
      "team_slug": "developers",
      "team_name": "Developers", 
      "repo_name": "frontend-app",
      "repo_full_name": "org/frontend-app",
      "permission_level": "detailed",
      "role_name": "write",
      "permissions": {
        "admin": false,
        "maintain": false,
        "push": true,
        "triage": true,
        "pull": true
      }
    }
  ]
}
```

### Console Output

```
================================================================================
TEAM-REPOSITORY MAPPING REPORT
Organization: your_org
Generated: 2024-01-15T10:30:00.123456
================================================================================

📊 SUMMARY:
   Total Repositories: 25
   Total Teams: 8
   Total Permissions Checked: 200
   Total Access Grants: 45

👥 TEAMS:
   Developers (developers)
      Members: 12
      Repositories with access: 8
      Privacy: closed
      Default permission: push

📚 REPOSITORIES:
   org/frontend-app 🔓 Public
      Teams with access: 3
      Default branch: main

🔐 PERMISSION DETAILS:
   Developers → frontend-app
      Role: write
      Permissions: push, triage, pull
```

## Permission Levels

GitHub repository permissions from lowest to highest:

- **pull** (read): Can read and clone the repository
- **triage**: Can read and manage issues and pull requests
- **push** (write): Can read, clone, and push to the repository
- **maintain**: Can read, clone, push, and manage some repository settings
- **admin**: Full access including repository settings, collaborators, and team assignments

## Rate Limiting

The script automatically handles GitHub API rate limits:
- Detects rate limit errors (HTTP 403)
- Waits for rate limit reset automatically
- Includes small delays between requests to be respectful

GitHub API rate limits:
- Personal Access Tokens: 5,000 requests/hour
- GitHub Apps: 5,000 requests/hour per installation

## Error Handling

The script includes comprehensive error handling:
- Network timeouts and connection errors
- Authentication failures
- Permission denied errors
- Repository or team not found errors
- Rate limit exceeded handling

## Security Notes

⚠️ **Important Security Considerations:**

1. **Token Security**: Never commit tokens to version control
2. **Minimum Permissions**: Use tokens with minimal required permissions
3. **Token Rotation**: Regularly rotate your access tokens
4. **Audit Logging**: Monitor token usage in GitHub's audit logs
5. **Environment Variables**: Consider using environment variables for tokens:

```bash
export GITHUB_TOKEN="your_token_here"
export GITHUB_ORG="your_org_here"
```

```python
import os
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
ORGANIZATION = os.getenv('GITHUB_ORG')
```

## Troubleshooting

### Common Issues

1. **Authentication Error (401)**
   - Verify your token is valid and not expired
   - Ensure token has required permissions

2. **Forbidden Error (403)**
   - Check if you have access to the organization
   - Verify token permissions match requirements
   - May indicate rate limiting (script handles this automatically)

3. **Not Found Error (404)**
   - Verify organization name is correct
   - Ensure repositories/teams exist
   - Check if resources are private and token has access

4. **Permission Errors**
   - Ensure token has admin access to repositories for permission management
   - Verify organization membership and permissions

### Debug Mode

To enable verbose output, modify the script to include debugging:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## CSV Integration

### CSV File Formats

The tool supports CSV files for bulk operations and data management:

#### 1. Bulk Assignment CSV Format
```csv
team_slug,repo_owner,repo_name,permission
developers,myorg,frontend-app,push
qa-team,myorg,frontend-app,pull
devops,myorg,infrastructure,admin
```

#### 2. Export CSV Format
The tool exports current mappings with detailed permission information:
```csv
team_name,team_slug,team_privacy,team_members_count,repo_name,repo_full_name,repo_private,repo_description,role_name,admin,maintain,push,triage,pull
Frontend Developers,developers,closed,8,frontend-app,myorg/frontend-app,true,Main web application,write,false,false,true,true,true
```

### CSV Utilities

Use the included CSV utilities for validation and management:

```bash
# Validate a CSV file before applying changes
python csv_utils.py validate sample_bulk_assignments.csv

# Create template CSV files
python csv_utils.py create-samples

# Convert JSON export to CSV format
python csv_utils.py json-to-csv mapping.json output.csv

# Load and display CSV content
python csv_utils.py load assignments.csv
```

### CSV Integration Examples

```python
# Load assignments from CSV and apply them
from csv_utils import load_bulk_assignments, validate_bulk_assignments

# Load and validate CSV data
assignments = load_bulk_assignments('bulk_assignments.csv')
validation_results = validate_bulk_assignments(assignments)

if validation_results['summary']['invalid_count'] == 0:
    # Apply the assignments
    results = mapper.bulk_assign_permissions(assignments)
    print(f"Applied {results['successful']} assignments")

# Export current mapping to CSV
from advanced_utils import export_to_csv
mapping = mapper.generate_complete_team_repo_mapping()
export_to_csv(mapping, 'current_permissions.csv')
```

## Sample Files Included

The repository includes several sample CSV files:

- `sample_bulk_assignments.csv` - Example bulk permission assignments
- `sample_team_config.csv` - Team configuration tracking
- `sample_repository_catalog.csv` - Repository documentation
- `sample_output_format.csv` - Example of exported permission data
- `sample_csv_files.md` - Detailed documentation of CSV formats

## Examples

### Example 1: Basic Mapping
```python
mapper = GitHubTeamRepoMapper("token", "myorg")
mapping = mapper.generate_complete_team_repo_mapping()
mapper.print_summary_report(mapping)
```

### Example 2: Check Specific Permission
```python
permission = mapper.check_team_repository_permissions("developers", "myorg", "myrepo")
if permission:
    print(f"Team has {permission.role_name} access")
else:
    print("Team has no access")
```

### Example 3: Bulk Permission Assignment with CSV
```python
# Load assignments from CSV file
from csv_utils import load_bulk_assignments

assignments = load_bulk_assignments('permissions.csv')
results = mapper.bulk_assign_permissions(assignments)
print(f"Successfully updated {results['successful']} permissions")
```

### Example 4: Export and Analysis
```python
# Generate mapping and export to multiple formats
mapping = mapper.generate_complete_team_repo_mapping()

# Export to JSON
mapper.export_mapping_to_json(mapping, 'team_repo_mapping.json')

# Export to CSV
from advanced_utils import export_to_csv
export_to_csv(mapping, 'team_repo_mapping.csv')
```

## Interactive CSV Tool

Run the interactive CSV integration tool:

```bash
python csv_integration_example.py
```

This provides a menu-driven interface to:
1. Create template CSV files
2. Validate CSV files
3. Run bulk assignments from CSV
4. Export current mapping to CSV

## License

This project is provided as-is for educational and demonstration purposes. Please review GitHub's Terms of Service and API guidelines when using this script in production environments.

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve this tool.

## Support

For GitHub API questions, refer to the official [GitHub REST API documentation](https://docs.github.com/en/rest).

For script-specific questions, please open an issue in the repository.