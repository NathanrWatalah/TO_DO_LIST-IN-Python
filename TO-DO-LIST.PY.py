# To-Do List Program

tasks = []  # store all tasks

while True:
    print("\n--- TO DO LIST ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Choose an option: ")

    # Add task
    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added.")

    # View tasks
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks found.")
        else:
            print("\nYour Tasks:")
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

    # Remove task
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to remove.")
        else:
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])

            num = int(input("Enter task number to remove: "))
            removed_task = tasks.pop(num - 1)
            print("Removed:", removed_task)

    # Exit
    elif choice == "4":
        print("Goodbye! You exit the Program.")
        break

    # Wrong input
    else:
        print("Invalid choice. Try again.")
