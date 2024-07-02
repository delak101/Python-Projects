todo_list = []

def add_task():
    task = input("Enter a Task: ").strip()
    if task:
        todo_list.append(task)
        print(f"Task '{task}' added successfully.")
    else:
        print("No task entered. Please try again.")

def remove_task():
    if not todo_list:
        print("List is empty.")
        return
    task = input("Enter a Task To Remove: ").strip()
    if task in todo_list:
        todo_list.remove(task)
        print(f"Task '{task}' removed successfully.")
    else:
        print(f"Task '{task}' not found.")

def view_tasks():
    if todo_list:
        print("Your To-Do List:")
        for index, item in enumerate(todo_list):
            print(f"{index + 1}. {item}")
    else:
        print("List is empty.")

def clear_tasks():
    confirmation = input("Are you sure you want to clear all tasks? (yes/no): ").strip().lower()
    if confirmation == "yes":
        todo_list.clear()
        print("All tasks cleared successfully.")
    else:
        print("Clear operation cancelled.")

def main():
    while True:
        action = input("Enter Operation (add, view, remove, clear, exit): ").strip().lower()
        if action == "add":
            add_task()
        elif action == "remove":
            remove_task()
        elif action == "view":
            view_tasks()
        elif action == "clear":
            clear_tasks()
        elif action == "exit":
            print("Bye")
            break
        else:
            print("Invalid action. Please try again.")

if __name__ == "__main__":
    main()
