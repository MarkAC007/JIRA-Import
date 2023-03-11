class Project:
    """
    A class that represents a JIRA project.
    """

    def __init__(self, name: str, key: str, description: str):
        self.name = name
        self.key = key
        self.description = description


class IssueTypeScheme:
    """
    A class that represents an issue type scheme in JIRA.
    """

    def __init__(self, name: str, description: str, issue_types: list):
        self.name = name
        self.description = description
        self.issue_types = issue_types


class WorkflowScheme:
    """
    A class that represents a workflow scheme in JIRA.
    """

    def __init__(self, name: str, description: str, workflows: list):
        self.name = name
        self.description = description
        self.workflows = workflows
