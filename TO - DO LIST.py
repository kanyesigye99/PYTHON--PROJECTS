tasks = []
while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Quit")
    choice = input("Enter your choice: ")
    if choice == "1":
        task = input("Enter your task: ")
        tasks.append(task)
        print("Task Added! ✅")
    elif choice == "2":
        print("\nTask List")

        for i, task in enumerate(tasks, 1):
           print(f"{i}. {task}")
    elif choice == "3":
         print("Goodbye!")
         break
    else:
         print("Invalid Choice!")
