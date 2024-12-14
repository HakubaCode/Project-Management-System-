# Python Task Management System

## Overview

This is a command-line Task Management System built in Python that allows users to create, manage, and track tasks with various features like priority sorting, task completion tracking, and persistent storage.

## Features

- **Add Tasks**: Create new tasks with title, description, priority, and due date
- **View Tasks**: 
  - List all tasks
  - Sort tasks by priority or due date
- **Task Tracking**:
  - Mark tasks as completed
  - Search tasks by keyword
- **Persistent Storage**: 
  - Tasks are automatically saved to and loaded from a JSON file

## Prerequisites

- Python 3.7+
- Standard Python libraries (json, datetime, os)

## Installation

1. Clone the repository
2. Ensure you have Python 3.7 or higher installed
3. No additional dependencies required

## Usage

Run the script and choose from the following options:

1. **Add Task**
   - Enter task details including title, description, priority, and due date

2. **View Tasks**
   - Choose to sort tasks by priority or due date
   - View task details including status

3. **Mark Task as Completed**
   - Mark a specific task as completed by its title

4. **Search Tasks**
   - Search for tasks using keywords (matches title or description)

5. **Exit**
   - Close the application

## Example

```bash
python task_management.py

1. Add Task
2. View Tasks
3. Mark Task as Completed
4. Search Tasks
5. Exit

Enter your choice (1-5): 
```

## Data Persistence

- Tasks are automatically saved to `tasks.json`
- Tasks are loaded from `tasks.json` when the application starts
- Allows for maintaining task list between application sessions

## Project Structure

- `Task` class: Represents individual tasks
- `ProjectManagementSystem` class: Manages task operations
- `main()` function: Provides command-line interface

## Potential Improvements

- Add task editing functionality
- Implement task deletion
- Create a graphical user interface (GUI)
- Add more advanced filtering options



## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
