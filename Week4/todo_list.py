# HANDS-ON
# 5] Build a to-do list that persists between runs

# -------------------------------------------------
# TYPE - 1 BASIC
# -------------------------------------------------
# If file doesn't exist → tasks saved in list temporarily
# When saving using "w" → file is created + tasks are written
# Next run → program loads old tasks from file

try:
    with open("todo.txt", "r") as file:
        tasks = file.read().splitlines()
except FileNotFoundError:
    tasks = []

while True:
    print("\nYour tasks:", tasks)
    task = input("Add a new task (or type 'exit'): ")

    if task.lower() == "exit":
        break

    tasks.append(task)

# Save tasks
with open("todo.txt", "w") as file:
    for t in tasks:
        file.write(t + "\n")

# -------------------------------------------------
# TYPE - 2 ADVANCED - Numbered tasks, Delete, Update
# -------------------------------------------------

# --------------------------
# 1. LOAD EXISTING TASKS
# --------------------------
try:
    with open("todo.txt", "r") as file:
        tasks = file.read().splitlines()
except FileNotFoundError:
    tasks = []

# --------------------------
# 2. MAIN MENU LOOP
# --------------------------
while True:
    print("\nYOUR TO-DO LIST:")
    if len(tasks) == 0:
        print("   (No tasks yet)")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"   {i}. {task}")

    print("\nWhat do you want to do?")
    print("1. Add a task")
    print("2. Delete a task")
    print("3. Update a task")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    # --------------------------
    # 3. ADD TASK
    # --------------------------
    if choice == "1":
        new_task = input("Enter new task: ")
        tasks.append(new_task)
        print("Task added.")

    # --------------------------
    # 4. DELETE TASK
    # --------------------------
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks to delete.")
            continue

        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            print(f"Deleted task: {removed}")
        else:
            print("Invalid task number.")

    # --------------------------
    # 5. UPDATE TASK
    # --------------------------
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to update.")
            continue

        num = int(input("Enter task number to update: "))

        if 1 <= num <= len(tasks):
            new_text = input("Enter updated task: ")
            tasks[num - 1] = new_text
            print("Task updated.")
        else:
            print("Invalid task number.")

    # --------------------------
    # 6. EXIT (SAVE TASKS)
    # --------------------------
    elif choice == "4":
        break
    else:
        print("Invalid choice. Try again.")

# --------------------------
# 7. SAVE TASKS BEFORE EXIT
# --------------------------
with open("todo.txt", "w") as file:
    for t in tasks:
        file.write(t + "\n")

print("\nTasks saved. Goodbye.")
