ISSUE_TYPE_SCHEME = {
    "name": "My Issue Type Scheme",
    "description": "A custom issue type scheme for my JIRA project",
    "issueTypes": [
        {
            "id": "10001",
            "name": "Epic",
            "description": "A big user story that needs to be broken down",
            "subtask": False
        },
        {
            "id": "10002",
            "name": "Task",
            "description": "A small unit of work that can be completed in one go",
            "subtask": False
        },
        {
            "id": "10003",
            "name": "Sub-Task",
            "description": "A sub-task of a bigger task",
            "subtask": True
        }
    ]
}
