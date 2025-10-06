import os
TASKS_FILE = "to-do.txt"
tasks = []
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return [line.strip() for line in file.readlines()]
    return []

def save_tasks():
    with open(TASKS_FILE, "w") as file:
        for task in tasks:
            file.write(task + "\n") 
    print("Tasks saved successfully!")

def add_task():
    task_name = input("Enter the task: ")
    tasks.append(task_name)
    print(f'Task "{task_name}" added.')

def view_tasks():
    if not tasks:
        print("No tasks found.")
        return
    print("\nYour To-Do List:")
    for i, task in enumerate(tasks):
        print(f'{i + 1}. {task}')

def remove_task():
    view_tasks()
    if not tasks:
        return
    try:
        task_num = int(input("Enter the number of the task to remove: ")) - 1
        if 0 <= task_num < len(tasks):
            removed_task = tasks.pop(task_num)
            print(f'Task "{removed_task}" removed.')
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def show_menu():
    print("\n--- To-Do List Menu ---")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Remove a task")
    print("4. Save and exit")
if __name__ == "__main__":
    tasks = load_tasks()
    while True:
        show_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            save_tasks()
            break
        else:
            print("Invalid choice. Please try again.")