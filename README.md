# JIRA-Import# JIRA API Python Project

This project is a Python application that utilizes the JIRA API to create a new project, set the issue type scheme, set the workflow scheme, and import data from a CSV file.

## Getting Started

1. Clone this repository to your local machine.
2. Install the required packages by running `pip install -r requirements.txt`.
3. Obtain authentication credentials for the JIRA API.
4. Update the configuration parameters in `project_creator.py` to match your JIRA settings.
5. Update the CSV file path in `project_creator.py` to match your local file path.
6. Run the project by executing `python project_creator.py`.

## Project Structure

- `jira/`: This folder contains the code related to the JIRA API integration.
- `csv_importer/`: This folder contains the code for importing the CSV file.
- `project_creator.py`: This file will be the main entry point for your program.
- `issue_type_scheme.py`: This file will define the issue type scheme that you want to use in your JIRA project.
- `workflow_scheme.py`: This file will define the workflow scheme that you want to use in your JIRA project.
- `requirements.txt`: This file contains the list of required Python packages for your project.

## Contributing

Feel free to contribute to this project by submitting a pull request. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the `LICENSE` file for details.
