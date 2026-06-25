todo_list = []

def show_menu():
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Remove Task")
    print("5. Exit")
    print("===========================\n")

def add_task():
    task = input("Enter a new task: ").strip()
    if task:
        todo_list.append({"title": task, "completed": False})
        print("Task added successfully.")
    else:
        print("Task cannot be empty.")

def view_tasks():
    if not todo_list:
        print("Your to-do list is empty.")
        return
    print("\nYour Tasks:")
    for i, task in enumerate(todo_list, 1):
        status = "Done" if task["completed"] else "Not Done"
        print(f"{i}. {task['title']} [{status}]")

def mark_completed():
    if not todo_list:
        print("No tasks to mark as completed.")
        return
    view_tasks()
    try:
        num = int(input("Enter the task number to mark as completed: "))
        if 1 <= num <= len(todo_list):
            todo_list[num - 1]["completed"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def remove_task():
    if not todo_list:
        print("No tasks to remove.")
        return
    view_tasks()
    try:
        num = int(input("Enter the task number to remove: "))
        if 1 <= num <= len(todo_list):
            removed = todo_list.pop(num - 1)
            print(f"Task '{removed['title']}' removed successfully.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

while True:
    show_menu()
    choice = input("Enter your choice (1-5): ").strip()

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        mark_completed()
    elif choice == '4':
        remove_task()
    elif choice == '5':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid option. Please choose a number between 1 and 5.")
