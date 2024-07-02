todo_list = []

while True:
    action = input("Enter Operation (add, view, remove, clear, exit): ")
    if action == "add":
        task = input("Enter a Task: ")
        todo_list.append(task)
        print("Task Added Successfully")

    elif action == "remove":
        task = input("Enter a Task To Remove: ")
        if not todo_list:
            print("List is empty")
        elif task in todo_list:
            todo_list.remove(task)
            print("Task Removed Successfully")
        else:
            print("404 - Task Not Found")

    elif action == "view":
        if todo_list:
            for index, item in enumerate(todo_list):
                print(index, " - ", item)
        else:
            print("List is empty")
            
    elif action == "clear":
        todo_list.clear()
        print("All tasks cleared successfully")

    elif action == "exit":
        print("Bye")
        break

    else:
        print("Invalid Action")
