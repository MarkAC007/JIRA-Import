class Epic:
    """
    A class that represents an Epic in the CSV file.
    """

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
        self.tasks = []


class Task:
    """
    A class that represents a Task in the CSV file.
    """

    def __init__(self, name: str):
        self.name = name
