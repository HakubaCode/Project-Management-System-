from datetime import datetime
import json
import os

class Task:
    def __init__(self, title, description, priority, due_date):
        self.title = title
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.completed = False
        self.created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "due_date": self.due_date,
            "completed": self.completed,
            "created_at": self.created_at
        }

class ProjectManagementSystem:
    def __init__(self):
        self.tasks = []
        self.filename = "tasks.json"
        self.load_tasks()

    def add_task(self, title, description, priority, due_date):
        task = Task(title, description, priority, due_date)
        self.tasks.append(task)
        self.save_tasks()
        return task

    def get_tasks(self, sort_by="priority"):
        if sort_by == "priority":
            return sorted(self.tasks, key=lambda x: x.priority)
        elif sort_by == "due_date":
            return sorted(self.tasks, key=lambda x: datetime.strptime(x.due_date, "%Y-%m-%d"))
        return self.tasks

    def mark_completed(self, title):
        for task in self.tasks:
            if task.title == title:
                task.completed = True
                self.save_tasks()
                return True
        return False

    def search_tasks(self, keyword):
        return [task for task in self.tasks 
                if keyword.lower() in task.title.lower() 
                or keyword.lower() in task.description.lower()]

    def save_tasks(self):
        with open(self.filename, 'w') as f:
            json_tasks = [task.to_dict() for task in self.tasks]
            json.dump(json_tasks, f)

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                tasks_data = json.load(f)
                for task_data in tasks_data:
                    task = Task(
                        task_data["title"],
                        task_data["description"],
                        task_data["priority"],
                        task_data["due_date"]
                    )
                    task.completed = task_data["completed"]
                    task.created_at = task_data["created_at"]
                    self.tasks.append(task)

def main():
    pms = ProjectManagementSystem()

    while True:
        print("\n1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Search Tasks")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            priority = int(input("Enter priority (1-5): "))
            due_date = input("Enter due date (YYYY-MM-DD): ")
            pms.add_task(title, description, priority, due_date)
            print("Task added successfully!")

        elif choice == "2":
            sort_by = input("Sort by (priority/due_date): ")
            tasks = pms.get_tasks(sort_by)
            for task in tasks:
                status = "Completed" if task.completed else "Pending"
                print(f"\nTitle: {task.title}")
                print(f"Description: {task.description}")
                print(f"Priority: {task.priority}")
                print(f"Due Date: {task.due_date}")
                print(f"Status: {status}")

        elif choice == "3":
            title = input("Enter task title to mark as completed: ")
            if pms.mark_completed(title):
                print("Task marked as completed!")
            else:
                print("Task not found!")

        elif choice == "4":
            keyword = input("Enter search keyword: ")
            results = pms.search_tasks(keyword)
            if results:
                print("\nSearch results:")
                for task in results:
                    print(f"\nTitle: {task.title}")
                    print(f"Description: {task.description}")
            else:
                print("No tasks found!")

        elif choice == "5":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
