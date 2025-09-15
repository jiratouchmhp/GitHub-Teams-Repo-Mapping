#!/usr/bin/env python3
"""
🚀 GitHub Team-Repository Mapping - Quick Start

This is the main entry point for the GitHub Team-Repository Mapping tool.
Choose from simple menu options to get started quickly!
"""

import os
import sys
from typing import Optional

# Add current directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from github_team_repo_mapper import GitHubTeamRepoMapper


def print_banner():
    """Print welcome banner"""
    print("=" * 70)
    print("🚀 GitHub Team-Repository Mapping Tool")
    print("=" * 70)
    print("Welcome! This tool helps you manage GitHub team permissions.")
    print("Let's get you started with a few simple steps.\n")


def check_prerequisites() -> tuple[Optional[str], Optional[str]]:
    """Check if GitHub token and org are configured"""
    token = os.getenv('GITHUB_TOKEN')
    org = os.getenv('GITHUB_ORG')
    
    if not token:
        print("⚠️  GitHub Token Required")
        print("   Please set your GitHub Personal Access Token:")
        print("   export GITHUB_TOKEN=your_token_here")
        print("   Or create a .env file with GITHUB_TOKEN=your_token_here\n")
    
    if not org:
        print("⚠️  Organization Required") 
        print("   Please set your GitHub organization:")
        print("   export GITHUB_ORG=your_org_name")
        print("   Or create a .env file with GITHUB_ORG=your_org_name\n")
    
    if not token or not org:
        print("💡 Need help getting a GitHub token?")
        print("   Visit: https://github.com/settings/tokens")
        print("   Required permissions: read:org, repo, admin:org\n")
        return None, None
    
    return token, org


def quick_overview():
    """Show a quick overview of current team-repo mappings"""
    print("🔍 Quick Overview - Current Team & Repository Mappings")
    print("-" * 70)
    
    token, org = check_prerequisites()
    if not token or not org:
        return
    
    try:
        mapper = GitHubTeamRepoMapper(token, org)
        
        print(f"📊 Analyzing organization: {org}")
        print("This may take a moment...\n")
        
        # Get basic info
        repos = mapper.list_organization_repositories()
        teams = mapper.list_organization_teams()
        
        print(f"✅ Found {len(repos)} repositories")
        print(f"✅ Found {len(teams)} teams\n")
        
        # Show first few repos and teams
        print("📁 Repositories (showing first 5):")
        for i, repo in enumerate(repos[:5]):
            privacy = "🔒 Private" if repo.private else "🔓 Public"
            print(f"   {i+1}. {privacy} {repo.name}")
        if len(repos) > 5:
            print(f"   ... and {len(repos) - 5} more")
        
        print(f"\n👥 Teams (showing first 5):")
        for i, team in enumerate(teams[:5]):
            print(f"   {i+1}. {team.name} ({team.members_count} members)")
        if len(teams) > 5:
            print(f"   ... and {len(teams) - 5} more")
        
        print(f"\n💡 Use option 2 to generate a complete mapping!")
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Please check your GitHub token and organization name.")


def generate_full_mapping():
    """Generate complete team-repository mapping"""
    print("📊 Complete Team-Repository Mapping")
    print("-" * 70)
    
    token, org = check_prerequisites()
    if not token or not org:
        return
    
    try:
        mapper = GitHubTeamRepoMapper(token, org)
        
        print(f"🔍 Generating complete mapping for {org}...")
        print("This will check all team-repository combinations. Please wait...\n")
        
        mapping = mapper.generate_complete_team_repo_mapping()
        
        # Print summary
        mapper.print_summary_report(mapping)
        
        # Save to files
        json_file = f"team_repo_mapping_{org}.json"
        mapper.export_mapping_to_json(mapping, json_file)
        print(f"💾 Saved detailed mapping to: {json_file}")
        print("💡 You can open this JSON file to see the detailed mapping")
        
    except Exception as e:
        print(f"❌ Error: {e}")


def bulk_assign_from_csv():
    """Load assignments from CSV and apply them"""
    print("📋 Bulk Permission Assignment from CSV")
    print("-" * 70)
    
    token, org = check_prerequisites()
    if not token or not org:
        return
    
    # Check for CSV file
    csv_files = [f for f in os.listdir('.') if f.endswith('.csv')]
    template_files = [f for f in os.listdir('templates') if f.endswith('.csv')]
    
    if not csv_files:
        print("❌ No CSV files found in current directory")
        print("\n💡 Quick solution:")
        print("   Create a CSV file using option 4 (Create Templates)")
        if template_files:
            print(f"   cp templates/{template_files[0]} my_assignments.csv")
        return
    
    print("📁 Found CSV files:")
    for i, csv_file in enumerate(csv_files, 1):
        print(f"   {i}. {csv_file}")
    
    try:
        choice = int(input(f"\nSelect CSV file (1-{len(csv_files)}): "))
        if choice < 1 or choice > len(csv_files):
            print("❌ Invalid choice")
            return
        
        selected_file = csv_files[choice - 1]
        print(f"📄 Loading assignments from {selected_file}...")
        
        # Simple CSV loading without external utilities
        import csv
        assignments = []
        try:
            with open(selected_file, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    if all(key in row for key in ['team_slug', 'repo_owner', 'repo_name', 'permission']):
                        assignments.append(row)
                    else:
                        print(f"❌ Invalid row format: {row}")
                        return
        except Exception as e:
            print(f"❌ Error reading CSV: {e}")
            return
        
        if not assignments:
            print("❌ No valid assignments found in CSV")
            return
        
        print(f"✅ Loaded {len(assignments)} assignments")
        
        # Simple validation
        valid_permissions = ['pull', 'triage', 'push', 'maintain', 'admin']
        invalid_count = 0
        for assignment in assignments:
            if assignment['permission'] not in valid_permissions:
                print(f"❌ Invalid permission '{assignment['permission']}' for team '{assignment['team_slug']}'")
                invalid_count += 1
        
        if invalid_count > 0:
            print(f"❌ Found {invalid_count} invalid assignments. Fix and try again.")
            return
        
        
        # Confirm before applying
        print(f"\n⚠️  WARNING: This will modify permissions for {len(assignments)} team-repository combinations!")
        confirm = input("Do you want to continue? (yes/no): ").lower().strip()
        
        if confirm not in ['yes', 'y']:
            print("Operation cancelled.")
            return
        
        # Apply assignments
        mapper = GitHubTeamRepoMapper(token, org)
        results = mapper.bulk_assign_permissions(assignments)
        
        print(f"\n✅ Bulk assignment completed!")
        print(f"   📊 Total: {results['total']}")
        print(f"   ✅ Successful: {results['successful']}")
        print(f"   ❌ Failed: {results['failed']}")
        
        if results['failed'] > 0:
            print(f"\n❌ Failed assignments:")
            for detail in results['details']:
                if not detail['success']:
                    print(f"   • {detail['team_slug']} → {detail['repo_name']}")
    
    except ValueError:
        print("❌ Please enter a valid number")
    except ImportError:
        print("❌ CSV utilities not found. Please ensure utils/csv_utils.py exists.")
    except Exception as e:
        print(f"❌ Error: {e}")


def create_templates():
    """Create template CSV files for users"""
    print("📝 Create Template Files")
    print("-" * 70)
    
    # Create simple bulk assignment template
    template_content = """team_slug,repo_owner,repo_name,permission
# Replace with your actual values:
# team_slug: Your team's slug (e.g., 'developers', 'qa-team')
# repo_owner: Your organization name
# repo_name: Repository name
# permission: pull, triage, push, maintain, admin

developers,YOUR_ORG,frontend-app,push
qa-team,YOUR_ORG,frontend-app,pull
devops,YOUR_ORG,infrastructure,admin"""

    template_file = "templates/bulk_assignments_template.csv"
    
    with open(template_file, 'w') as f:
        f.write(template_content)
    
    print(f"✅ Created template: {template_file}")
    print(f"\n📝 Edit this file with your actual:")
    print(f"   • Team slugs (lowercase, with hyphens)")
    print(f"   • Organization name") 
    print(f"   • Repository names")
    print(f"   • Permission levels (pull, triage, push, maintain, admin)")
    print(f"\n💡 After editing, copy it to the main directory:")
    print(f"   cp {template_file} my_assignments.csv")
    
    # Also create a simple config template
    config_template = """# GitHub Team-Repository Mapping Configuration
# Copy this to .env in the main directory

GITHUB_TOKEN=your_personal_access_token_here
GITHUB_ORG=your_organization_name_here

# Get your token from: https://github.com/settings/tokens
# Required permissions: read:org, repo, admin:org"""

    config_file = "templates/.env_template"
    with open(config_file, 'w') as f:
        f.write(config_template)
    
    print(f"✅ Created config template: {config_file}")
    print(f"💡 Copy and edit for your credentials:")
    print(f"   cp {config_file} .env")


def show_samples():
    """Show available sample files"""
    print("📁 Sample Files and Documentation")
    print("-" * 70)
    
    samples_dir = "samples"
    if os.path.exists(samples_dir):
        files = os.listdir(samples_dir)
        csv_files = [f for f in files if f.endswith('.csv')]
        doc_files = [f for f in files if f.endswith('.md')]
        
        if csv_files:
            print("📋 Sample CSV files:")
        print("📁 Templates created successfully!")
        print("💡 Edit the template files and run the tool again.")
    else:
        print("❌ Templates directory not found")


def main():
    """Main menu"""
    print_banner()
    
    while True:
        print("\n" + "=" * 70)
        print("Choose an option:")
        print("1. 🔍 Quick Overview (see teams & repositories)")
        print("2. 📊 Generate Complete Mapping (full analysis)")
        print("3. 📋 Bulk Assign from CSV (modify permissions)")
        print("4. 📝 Create Template Files (get started)")
        print("5. 📁 View Sample Files (examples)")
        print("6. ❌ Exit")
        print("=" * 70)
        
        try:
            choice = input("Enter your choice (1-6): ").strip()
            
            if choice == '1':
                quick_overview()
            elif choice == '2':
                generate_full_mapping()
            elif choice == '3':
                bulk_assign_from_csv()
            elif choice == '4':
                create_templates()
            elif choice == '5':
                show_samples()
            elif choice == '6':
                print("👋 Thank you for using GitHub Team-Repository Mapping!")
                break
            else:
                print("❌ Please choose a number between 1-6")
                
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ An error occurred: {e}")
            print("Please try again or check your configuration.")


if __name__ == "__main__":
    main()