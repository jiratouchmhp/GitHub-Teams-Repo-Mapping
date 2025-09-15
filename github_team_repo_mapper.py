#!/usr/bin/env python3
"""
GitHub Team-Repository Mapping Script

This script demonstrates how to use the GitHub API to create a comprehensive mapping
of teams and repositories within an organization, including permission analysis
and assignment management.

API Endpoints used:
1. List organization repositories: GET /orgs/{org}/repos
2. List teams: GET /orgs/{org}/teams  
3. Check team permissions for repository: GET /orgs/{org}/teams/{team_slug}/repos/{owner}/{repo}
4. Add/update team repository permissions: PUT /orgs/{org}/teams/{team_slug}/repos/{owner}/{repo}

Author: GitHub API Demo
Date: 2024
"""

import requests
import json
import sys
from typing import Dict, List, Optional, Set
from dataclasses import dataclass
from datetime import datetime
import time


@dataclass
class Repository:
    """Repository information"""
    id: int
    name: str
    full_name: str
    private: bool
    description: Optional[str]
    default_branch: str
    created_at: str
    updated_at: str
    owner: str


@dataclass  
class Team:
    """Team information"""
    id: int
    name: str
    slug: str
    description: Optional[str]
    privacy: str
    permission: str
    members_count: int
    repos_count: int
    created_at: str
    updated_at: str


@dataclass
class TeamRepoPermission:
    """Team repository permission mapping"""
    team_slug: str
    team_name: str
    repo_name: str
    repo_full_name: str
    permission_level: str
    role_name: str
    has_admin: bool
    has_maintain: bool  
    has_push: bool
    has_triage: bool
    has_pull: bool


class GitHubTeamRepoMapper:
    """GitHub Team-Repository Mapping Tool"""
    
    def __init__(self, token: str, org: str):
        """
        Initialize the mapper with GitHub token and organization
        
        Args:
            token: GitHub personal access token with proper scopes
            org: Organization name
        """
        self.token = token
        self.org = org
        self.headers = {
            'Authorization': f'Bearer {token}',
            'Accept': 'application/vnd.github+json',
            'X-GitHub-Api-Version': '2022-11-28'
        }
        self.base_url = 'https://api.github.com'
        
    def _make_request(self, url: str, method: str = 'GET', data: Optional[Dict] = None) -> requests.Response:
        """Make authenticated GitHub API request with error handling"""
        try:
            if method == 'GET':
                response = requests.get(url, headers=self.headers)
            elif method == 'PUT':
                response = requests.put(url, headers=self.headers, json=data)
            elif method == 'POST':
                response = requests.post(url, headers=self.headers, json=data)
            elif method == 'DELETE':
                response = requests.delete(url, headers=self.headers)
                
            # Handle rate limiting
            if response.status_code == 403 and 'rate limit' in response.text.lower():
                reset_time = int(response.headers.get('X-RateLimit-Reset', time.time() + 3600))
                wait_time = reset_time - int(time.time()) + 1
                print(f"Rate limit exceeded. Waiting {wait_time} seconds...")
                time.sleep(wait_time)
                return self._make_request(url, method, data)
                
            response.raise_for_status()
            return response
            
        except requests.exceptions.RequestException as e:
            print(f"API request failed: {e}")
            if hasattr(e, 'response') and e.response is not None:
                print(f"Response status: {e.response.status_code}")
                print(f"Response body: {e.response.text}")
            sys.exit(1)

    def _paginate_results(self, url: str) -> List[Dict]:
        """Handle paginated API responses"""
        all_results = []
        page = 1
        
        while True:
            paginated_url = f"{url}{'&' if '?' in url else '?'}page={page}&per_page=100"
            response = self._make_request(paginated_url)
            results = response.json()
            
            if not results:  # Empty response means no more pages
                break
                
            all_results.extend(results)
            page += 1
            
            # Check if we've reached the last page
            if len(results) < 100:
                break
                
        return all_results

    def list_organization_repositories(self) -> List[Repository]:
        """
        List all repositories in the organization
        
        Uses: GET /orgs/{org}/repos
        Required permissions: read:org scope for OAuth tokens
        """
        print(f"📚 Fetching repositories for organization: {self.org}")
        
        url = f"{self.base_url}/orgs/{self.org}/repos"
        repo_data = self._paginate_results(url)
        
        repositories = []
        for repo in repo_data:
            repositories.append(Repository(
                id=repo['id'],
                name=repo['name'],
                full_name=repo['full_name'],
                private=repo['private'],
                description=repo.get('description'),
                default_branch=repo['default_branch'],
                created_at=repo['created_at'],
                updated_at=repo['updated_at'],
                owner=repo['owner']['login']
            ))
            
        print(f"✅ Found {len(repositories)} repositories")
        return repositories

    def list_organization_teams(self) -> List[Team]:
        """
        List all teams in the organization
        
        Uses: GET /orgs/{org}/teams
        Required permissions: Members organization permissions (read)
        """
        print(f"👥 Fetching teams for organization: {self.org}")
        
        url = f"{self.base_url}/orgs/{self.org}/teams"
        team_data = self._paginate_results(url)
        
        teams = []
        for team in team_data:
            teams.append(Team(
                id=team['id'],
                name=team['name'],
                slug=team['slug'],
                description=team.get('description'),
                privacy=team['privacy'],
                permission=team.get('permission', 'pull'),
                members_count=team['members_count'],
                repos_count=team['repos_count'],
                created_at=team['created_at'],
                updated_at=team['updated_at']
            ))
            
        print(f"✅ Found {len(teams)} teams")
        return teams

    def check_team_repository_permissions(self, team_slug: str, owner: str, repo: str) -> Optional[TeamRepoPermission]:
        """
        Check team permissions for a specific repository
        
        Uses: GET /orgs/{org}/teams/{team_slug}/repos/{owner}/{repo}
        Required permissions: Members org permissions (read) + Metadata repo permissions (read)
        
        Returns:
            TeamRepoPermission object if team has access, None if no access
        """
        url = f"{self.base_url}/orgs/{self.org}/teams/{team_slug}/repos/{owner}/{repo}"
        
        try:
            response = self._make_request(url)
            
            if response.status_code == 200:
                # Team has access with detailed repository information
                data = response.json()
                permissions = data.get('permissions', {})
                
                return TeamRepoPermission(
                    team_slug=team_slug,
                    team_name=team_slug.replace('-', ' ').title(),  # Approximate team name from slug
                    repo_name=repo,
                    repo_full_name=data['full_name'],
                    permission_level='detailed',
                    role_name=data.get('role_name', 'unknown'),
                    has_admin=permissions.get('admin', False),
                    has_maintain=permissions.get('maintain', False),
                    has_push=permissions.get('push', False),
                    has_triage=permissions.get('triage', False),
                    has_pull=permissions.get('pull', False)
                )
            elif response.status_code == 204:
                # Team has basic permission (no detailed info available)
                return TeamRepoPermission(
                    team_slug=team_slug,
                    team_name=team_slug.replace('-', ' ').title(),
                    repo_name=repo,
                    repo_full_name=f"{owner}/{repo}",
                    permission_level='basic',
                    role_name='unknown',
                    has_admin=False,
                    has_maintain=False,
                    has_push=False,
                    has_triage=False,
                    has_pull=True  # Assume at least pull access
                )
                
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 404:
                # Team does not have access to repository
                return None
            raise
            
        return None

    def add_or_update_team_repository_permissions(self, team_slug: str, owner: str, repo: str, 
                                                permission: str) -> bool:
        """
        Add or update team repository permissions
        
        Uses: PUT /orgs/{org}/teams/{team_slug}/repos/{owner}/{repo}
        Required permissions: Administration repo permissions (write) + Members org permissions (read) + Metadata repo permissions (read)
        
        Args:
            team_slug: Team slug
            owner: Repository owner
            repo: Repository name  
            permission: Permission level (pull, triage, push, maintain, admin)
            
        Returns:
            True if successful, False otherwise
        """
        url = f"{self.base_url}/orgs/{self.org}/teams/{team_slug}/repos/{owner}/{repo}"
        data = {"permission": permission}
        
        try:
            response = self._make_request(url, method='PUT', data=data)
            if response.status_code == 204:
                print(f"✅ Updated {team_slug} permissions for {owner}/{repo} to {permission}")
                return True
        except requests.exceptions.HTTPError as e:
            print(f"❌ Failed to update {team_slug} permissions for {owner}/{repo}: {e}")
            return False
            
        return False

    def generate_complete_team_repo_mapping(self) -> Dict:
        """
        Generate complete mapping of teams to repositories with permissions
        
        This is the main function that combines all API endpoints to create
        a comprehensive view of team-repository relationships
        """
        print("🔍 Starting comprehensive team-repository mapping...")
        
        # Step 1: Get all repositories
        repositories = self.list_organization_repositories()
        
        # Step 2: Get all teams
        teams = self.list_organization_teams()
        
        # Step 3: Check each team's permissions for each repository
        print(f"🔄 Checking permissions for {len(teams)} teams across {len(repositories)} repositories...")
        
        mapping = {
            'organization': self.org,
            'generated_at': datetime.now().isoformat(),
            'summary': {
                'total_repositories': len(repositories),
                'total_teams': len(teams),
                'total_permissions_checked': 0,
                'total_access_granted': 0
            },
            'repositories': {},
            'teams': {},
            'permissions_matrix': []
        }
        
        # Initialize repository data
        for repo in repositories:
            mapping['repositories'][repo.name] = {
                'id': repo.id,
                'full_name': repo.full_name,
                'private': repo.private,
                'description': repo.description,
                'default_branch': repo.default_branch,
                'teams_with_access': []
            }
            
        # Initialize team data  
        for team in teams:
            mapping['teams'][team.slug] = {
                'id': team.id,
                'name': team.name,
                'slug': team.slug,
                'description': team.description,
                'privacy': team.privacy,
                'default_permission': team.permission,
                'members_count': team.members_count,
                'repos_count': team.repos_count,
                'repositories_with_access': []
            }
        
        # Check permissions matrix
        for team in teams:
            for repo in repositories:
                print(f"  🔍 Checking {team.slug} access to {repo.name}...")
                
                permission = self.check_team_repository_permissions(
                    team.slug, repo.owner, repo.name
                )
                
                mapping['summary']['total_permissions_checked'] += 1
                
                if permission:
                    mapping['summary']['total_access_granted'] += 1
                    
                    # Add to permissions matrix
                    mapping['permissions_matrix'].append({
                        'team_slug': permission.team_slug,
                        'team_name': permission.team_name,
                        'repo_name': permission.repo_name,
                        'repo_full_name': permission.repo_full_name,
                        'permission_level': permission.permission_level,
                        'role_name': permission.role_name,
                        'permissions': {
                            'admin': permission.has_admin,
                            'maintain': permission.has_maintain,
                            'push': permission.has_push,
                            'triage': permission.has_triage,
                            'pull': permission.has_pull
                        }
                    })
                    
                    # Update repository teams list
                    mapping['repositories'][repo.name]['teams_with_access'].append({
                        'team_slug': team.slug,
                        'team_name': team.name,
                        'role_name': permission.role_name,
                        'permissions': {
                            'admin': permission.has_admin,
                            'maintain': permission.has_maintain,
                            'push': permission.has_push,
                            'triage': permission.has_triage,
                            'pull': permission.has_pull
                        }
                    })
                    
                    # Update team repositories list
                    mapping['teams'][team.slug]['repositories_with_access'].append({
                        'repo_name': repo.name,
                        'repo_full_name': repo.full_name,
                        'role_name': permission.role_name,
                        'permissions': {
                            'admin': permission.has_admin,
                            'maintain': permission.has_maintain,
                            'push': permission.has_push,
                            'triage': permission.has_triage,
                            'pull': permission.has_pull
                        }
                    })
                    
                # Small delay to be respectful of rate limits
                time.sleep(0.1)
                
        print(f"✅ Mapping completed!")
        print(f"   📊 {mapping['summary']['total_access_granted']} access grants found")
        print(f"   📊 {mapping['summary']['total_permissions_checked']} permissions checked")
        
        return mapping

    def export_mapping_to_json(self, mapping: Dict, filename: str = None):
        """Export mapping to JSON file"""
        if filename is None:
            filename = f"{self.org}_team_repo_mapping_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
            
        with open(filename, 'w') as f:
            json.dump(mapping, f, indent=2, ensure_ascii=False)
            
        print(f"📄 Mapping exported to {filename}")

    def print_summary_report(self, mapping: Dict):
        """Print a human-readable summary report"""
        print("\n" + "="*80)
        print(f"TEAM-REPOSITORY MAPPING REPORT")
        print(f"Organization: {mapping['organization']}")
        print(f"Generated: {mapping['generated_at']}")
        print("="*80)
        
        summary = mapping['summary']
        print(f"\n📊 SUMMARY:")
        print(f"   Total Repositories: {summary['total_repositories']}")
        print(f"   Total Teams: {summary['total_teams']}")
        print(f"   Total Permissions Checked: {summary['total_permissions_checked']}")
        print(f"   Total Access Grants: {summary['total_access_granted']}")
        
        print(f"\n👥 TEAMS:")
        for team_slug, team_data in mapping['teams'].items():
            repos_count = len(team_data['repositories_with_access'])
            print(f"   {team_data['name']} ({team_slug})")
            print(f"      Members: {team_data['members_count']}")
            print(f"      Repositories with access: {repos_count}")
            print(f"      Privacy: {team_data['privacy']}")
            print(f"      Default permission: {team_data['default_permission']}")
        
        print(f"\n📚 REPOSITORIES:")
        for repo_name, repo_data in mapping['repositories'].items():
            teams_count = len(repo_data['teams_with_access'])
            privacy = "🔒 Private" if repo_data['private'] else "🔓 Public"
            print(f"   {repo_data['full_name']} {privacy}")
            print(f"      Teams with access: {teams_count}")
            print(f"      Default branch: {repo_data['default_branch']}")
            
        print(f"\n🔐 PERMISSION DETAILS:")
        for perm in mapping['permissions_matrix']:
            permissions_list = [k for k, v in perm['permissions'].items() if v]
            print(f"   {perm['team_name']} → {perm['repo_name']}")
            print(f"      Role: {perm['role_name']}")
            print(f"      Permissions: {', '.join(permissions_list)}")

    def bulk_assign_permissions(self, assignments: List[Dict]) -> Dict:
        """
        Bulk assign repository permissions to teams
        
        Args:
            assignments: List of dictionaries with keys:
                - team_slug: Team slug
                - repo_owner: Repository owner  
                - repo_name: Repository name
                - permission: Permission level (pull, triage, push, maintain, admin)
                
        Returns:
            Dictionary with success/failure results
        """
        print(f"🔄 Starting bulk permission assignment for {len(assignments)} assignments...")
        
        results = {
            'total': len(assignments),
            'successful': 0,
            'failed': 0,
            'details': []
        }
        
        for assignment in assignments:
            team_slug = assignment['team_slug']
            repo_owner = assignment['repo_owner']
            repo_name = assignment['repo_name']
            permission = assignment['permission']
            
            print(f"  🔄 Assigning {permission} permission to {team_slug} for {repo_owner}/{repo_name}...")
            
            success = self.add_or_update_team_repository_permissions(
                team_slug, repo_owner, repo_name, permission
            )
            
            result_detail = {
                'team_slug': team_slug,
                'repo_owner': repo_owner,
                'repo_name': repo_name,
                'permission': permission,
                'success': success
            }
            
            results['details'].append(result_detail)
            
            if success:
                results['successful'] += 1
            else:
                results['failed'] += 1
                
            # Small delay to be respectful of rate limits
            time.sleep(0.2)
            
        print(f"✅ Bulk assignment completed!")
        print(f"   📊 {results['successful']} successful")
        print(f"   📊 {results['failed']} failed")
        
        return results


def main():
    """Main execution function with example usage"""
    # Configuration - Replace with your actual values
    GITHUB_TOKEN = "your_github_token_here"  # Replace with your token
    ORGANIZATION = "your_org_name_here"      # Replace with your org name
    
    if GITHUB_TOKEN == "your_github_token_here" or ORGANIZATION == "your_org_name_here":
        print("❌ Please configure GITHUB_TOKEN and ORGANIZATION variables")
        print("   Set your GitHub personal access token and organization name")
        sys.exit(1)
    
    # Initialize the mapper
    mapper = GitHubTeamRepoMapper(GITHUB_TOKEN, ORGANIZATION)
    
    try:
        # Generate complete mapping
        mapping = mapper.generate_complete_team_repo_mapping()
        
        # Print summary report
        mapper.print_summary_report(mapping)
        
        # Export to JSON
        mapper.export_mapping_to_json(mapping)
        
        # Example: Bulk assign permissions
        # Uncomment and modify these example assignments as needed
        """
        example_assignments = [
            {
                'team_slug': 'developers',
                'repo_owner': 'your_org_name_here',
                'repo_name': 'example-repo-1',
                'permission': 'push'
            },
            {
                'team_slug': 'admin-team', 
                'repo_owner': 'your_org_name_here',
                'repo_name': 'example-repo-2',
                'permission': 'admin'
            }
        ]
        
        assignment_results = mapper.bulk_assign_permissions(example_assignments)
        print(f"\\n📊 Assignment Results: {assignment_results}")
        """
        
        print("\n🎉 Team-repository mapping completed successfully!")
        
    except KeyboardInterrupt:
        print("\n⚠️  Operation cancelled by user")
        sys.exit(0)
    except Exception as e:
        print(f"❌ An error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()