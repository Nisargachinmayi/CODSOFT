import json
import os

# File to store tasks
TASKS_FILE = 'tasks.json'

def load_tasks():
    """
    Load tasks from the JSON file.
    Returns a list of tasks.
    """
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            try:
                tasks = json.load(file)
            except json.JSONDecodeError:
                tasks = []
    else:
        tasks = []
    return tasks

def save_tasks(tasks):
    """
    Save the list of tasks to the JSON file.
    """
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def display_tasks(tasks):
    """
    Display all tasks with their index and status.
    """
    if not tasks:
        print("\nYour to-do list is empty.")
    else:
        print("\nYour To-Do List:")
        for idx, task in enumerate(tasks, start=1):
            status = "✓" if task['completed'] else "✗"
            print(f"{idx}. [{status}] {task['title']}")

def add_task(tasks):
    """
    Add a new task to the list.
    """
    title = input("Enter the task description: ").strip()
    if title:
        tasks.append({'title': title, 'completed': False})
        print(f"Task '{title}' added.")
    else:
        print("Empty task description. Nothing added.")

def update_task(tasks):
    """
    Mark a task as completed or uncompleted.
    """
    display_tasks(tasks)
    if not tasks:
        return
    try:
        task_num = int(input("Enter the task number to toggle completion: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]['completed'] = not tasks[task_num - 1]['completed']
            status = "completed" if tasks[task_num - 1]['completed'] else "not completed"
            print(f"Task '{tasks[task_num - 1]['title']}' marked as {status}.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task(tasks):
    """
    Delete a task from the list.
    """
    display_tasks(tasks)
    if not tasks:
        return
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task['title']}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    """
    Main function to run the To-Do List application.
    """
    tasks = load_tasks()

    while True:
        print("\n=== To-Do List Application ===")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Toggle Task Completion")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Choose an option (1-5): ").strip()

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
            save_tasks(tasks)
        elif choice == '3':
            update_task(tasks)
            save_tasks(tasks)
        elif choice == '4':
            delete_task(tasks)
            save_tasks(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()