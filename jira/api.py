import requests


class JiraAPI:
    """
    A class that wraps the JIRA REST API and provides helper functions to interact with JIRA.
    """

    def __init__(self, url: str, username: str, password: str):
        self.base_url = url
        self.username = username
        self.password = password

    def create_project(self, project_name: str, key: str, description: str) -> dict:
        """
        Create a new JIRA project.
        """
        url = f"{self.base_url}/rest/api/2/project"
        payload = {
            "name": project_name,
            "key": key,
            "description": description
        }
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.post(url, json=payload, headers=headers, auth=(self.username, self.password))
        if response.status_code == 201:
            return response.json()
        else:
            raise Exception(f"Failed to create JIRA project: {response.text}")

    def set_issue_type_scheme(self, project_key: str, issue_type_scheme_id: str):
        """
        Set the issue type scheme for a JIRA project.
        """
        url = f"{self.base_url}/rest/api/2/project/{project_key}/issuescheme"
        payload = {
            "issueTypeSchemeId": issue_type_scheme_id
        }
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.put(url, json=payload, headers=headers, auth=(self.username, self.password))
        if response.status_code != 204:
            raise Exception(f"Failed to set issue type scheme for JIRA project: {response.text}")

    def set_workflow_scheme(self, project_key: str, workflow_scheme_id: str):
        """
        Set the workflow scheme for a JIRA project.
        """
        url = f"{self.base_url}/rest/api/2/project/{project_key}/workflowscheme"
        payload = {
            "workflowSchemeId": workflow_scheme_id
        }
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.put(url, json=payload, headers=headers, auth=(self.username, self.password))
        if response.status_code != 204:
            raise Exception(f"Failed to set workflow scheme for JIRA project: {response.text}")
