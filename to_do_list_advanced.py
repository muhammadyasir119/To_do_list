tasks = []

while True:
    print("\n--Menu--")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Exit")

    choice = input("Enter choice: ")

    # Add task
    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added ")

    # View tasks
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks found ")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(i + 1, "-", tasks[i])

    # Delete task
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to delete ")
        else:
            for i in range(len(tasks)):
                print(i + 1, "-", tasks[i])

            num = int(input("Enter task number to delete: "))
            
            if num > 0 and num <= len(tasks):
                removed = tasks.pop(num - 1)
                print("Removed:", removed)
            else:
                print("Invalid number ")

    # Exit
    elif choice == "4":
        print("Goodbye ")
        break

    else:
        print("Invalid choice ")