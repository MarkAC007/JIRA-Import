import csv


class CsvHandler:
    """
    A class that handles importing data from a CSV file.
    """

    def __init__(self, csv_file: str):
        self.csv_file = csv_file

    def import_data(self):
        """
        Import data from the CSV file and return a list of Epics and Tasks.
        """
        epics = []
        with open(self.csv_file, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                epic_name = row.get('EPIC')
                epic_description = row.get('Description')
                task_name = row.get('Task')
                if epic_name and task_name:
                    task = Task(name=task_name)
                    epic = next((e for e in epics if e.name == epic_name), None)
                    if not epic:
                        epic = Epic(name=epic_name, description=epic_description)
                        epics.append(epic)
                    epic.tasks.append(task)
        return epics


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
