tasks = []

while True:
    print("\n--Menu--")
    print("1 Add task")
    print("2 View task")
    print("3 Exit")
    choice = input("Enter choice:")
    if choice == "1":
        task = input("Enter task to add:")
        tasks.append(task)
        print("Task added")
    elif choice == "2":
        print("\n your tasks")
        for task in tasks:
            print("-",tasks)
    elif choice == "3":
        print("Goodbye")
        break
    else:
        print("Invalid task")
        