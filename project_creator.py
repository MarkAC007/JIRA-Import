from jira.api import JiraAPI, Project, IssueTypeScheme, WorkflowScheme
from csv_importer.csv_handler import CsvHandler, Epic, Task
from issue_type_scheme import ISSUE_TYPE_SCHEME
from workflow_scheme import WORKFLOW_SCHEME


JIRA_BASE_URL = 'https://your-jira-instance.atlassian.net'
JIRA_USERNAME = 'your-jira-username'
JIRA_PASSWORD = 'your-jira-password'
JIRA_PROJECT_NAME = 'My Project'
JIRA_PROJECT_KEY = 'MYPROJ'
JIRA_PROJECT_DESCRIPTION = 'My Project Description'
CSV_FILE_PATH = 'path/to/my/csv/file.csv'


def create_project(api: JiraAPI, project: Project):
    """
    Create a new JIRA project using the provided JiraAPI object and Project object.
    """
    project_data = api.create_project(project.name, project.key, project.description)
    project_id = project_data.get('id')
    return project_id


def set_issue_type_scheme(api: JiraAPI, project_key: str):
    """
    Set the issue type scheme for a JIRA project using the provided JiraAPI object and project key.
    """
    api.set_issue_type_scheme(project_key, ISSUE_TYPE_SCHEME)


def set_workflow_scheme(api: JiraAPI, project_key: str):
    """
    Set the workflow scheme for a JIRA project using the provided JiraAPI object and project key.
    """
    api.set_workflow_scheme(project_key, WORKFLOW_SCHEME)


def import_csv_data(csv_file_path: str) -> list:
    """
    Import data from a CSV file using the CsvHandler object.
    """
    csv_handler = CsvHandler(csv_file_path)
    epics = csv_handler.import_data()
    return epics


def create_issues(api: JiraAPI, project_id: str, epics: list):
    """
    Create issues in JIRA for the provided Epics and Tasks using the provided JiraAPI object and project ID.
    """
    for epic in epics:
        epic_issue_data = api.create_issue(project_id, epic.name, 'Epic', epic.description)
        epic_issue_key = epic_issue_data.get('key')
        for task in epic.tasks:
            task_issue_data = api.create_issue(project_id, task.name, 'Task')
            task_issue_key = task_issue_data.get('key')
            api.link_issues(epic_issue_key, task_issue_key)


def main():
    api = JiraAPI(JIRA_BASE_URL, JIRA_USERNAME, JIRA_PASSWORD)
    project = Project(JIRA_PROJECT_NAME, JIRA_PROJECT_KEY, JIRA_PROJECT_DESCRIPTION)
    project_id = create_project(api, project)
    set_issue_type_scheme(api, project_id)
    set_workflow_scheme(api, project_id)
    epics = import_csv_data(CSV_FILE_PATH)
    create_issues(api, project_id, epics)


if __name__ == '__main__':
    main()
