# Task-Tracker

Task-Tracker is a command-line application to manage tasks. You can add, list, update, and delete tasks efficiently.

## Features
- Add new tasks with a description.
- List tasks with optional filtering by status (`todo`, `doing`, `done`).
- Update the status of a task.
- Delete tasks by ID.

## Prerequisites
- Python 3.x installed on your system.

## Setup
1. Clone this repository or download the files.
2. Navigate to the `Coding` directory:
   ```bash
   cd Coding
   ```

## To add a new Task
    python .py add "Task description"

## List Tasks
    python .py list

## To filter tasks by status
    python .py list --status todo

## Update Task Status
    python .py update <task_id> <new_status>

## Delete a Task
    python .py delete <task_id>
## Project URL:https://roadmap.sh/projects/task-tracker
