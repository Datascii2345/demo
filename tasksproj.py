tasks = {}

def add_task(description):
    tasks[description] = False

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        print("Tasks:")
        for index, (task, completed) in enumerate(tasks.items(), start=1):
            status = "✓" if completed else "✗"
            print(f"{index}. [{status}] {task}")

def filter_tasks(status):
    filtered_tasks = {task: completed for task, completed in tasks.items() if completed == status}
    if not filtered_tasks:
        print(f"No {'completed' if status else 'incomplete'} tasks available.")
    else:
        print(f"{'Completed' if status else 'Incomplete'} Tasks:")
        for index, task in enumerate(filtered_tasks, start=1):
            print(f"{index}. {task}")


def mark_task_complete(task_index):
    if task_index < 1 or task_index > len(tasks):
        print("Invalid task index.")
    else:
        task = list(tasks.keys())[task_index - 1]
        tasks[task] = True
        print(f"Task '{task}' marked as complete.")

def task_reminders():
  print("Remaining Tasks:")
  for index, (task, completed) in enumerate(tasks.items(), start=1):
      status = "✓" if completed else "✗"
      if status == "✗":
            print(f"{index}. [{status}] {task}")
      else:
        pass;

def task_status():
  print("Filtered Tasks:")
  for index, (task, completed) in enumerate(tasks.items(), start=1):
      status = "✓" if completed else "✗"
      if status == "✗":
            print("Incomplete tasks")
            print(f"{index}. [{status}] {task}")
      else:
            pass;

  for index, (task, completed) in enumerate(tasks.items(), start=1):
      status = "✓" if completed else "✗"
      if status == "✓":
            print("Completed tasks")
            print(f"{index}. [{status}] {task}")
      else:
            pass;

def delete_task(task_index):
    if task_index < 1 or task_index > len(tasks):
        print("Invalid task index.")
    else:
        task = list(tasks.keys())[task_index - 1]
        del tasks[task]
        print(f"Task '{task}' deleted.")

def mark_task_incomplete(task_index):
    if task_index < 1 or task_index > len(tasks):
        print("Invalid task index.")

    else:
        task = list(tasks.keys())[task_index - 1]
        if tasks[task] == False:
           print(f"Task '{task}' is already incomplete.")
        else:
           tasks[task] = False
           print(f"Task '{task}' marked as incomplete.")

# Sample usage
while True:
    print("\nTask Manager")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Complete")
    print("4. Mark Task as Incomplete")
    print("5. View Reminders")
    print("6. View Tasks Status")
    print("7. Filter Tasks by Status")
    print("8. Delete Task")
    print("9. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        description = input("Enter task description: ")
        add_task(description)
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        view_tasks()
        task_index = int(input("Enter the index of the task to mark as complete: "))
        mark_task_complete(task_index)
    elif choice == "4":
        view_tasks()
        task_index = int(input("Enter the index of the task to mark as incomplete: "))
        mark_task_incomplete(task_index)
    elif choice == "5":
        view_tasks()
        task_reminders()
    elif choice == "6":
        view_tasks()
        task_status()
    elif choice == "7":
        status = input("Enter task status (complete/incomplete): ").lower()
        if status == "complete":
            filter_tasks(True)
        elif status == "incomplete":
            filter_tasks(False)
        else:
            print("Invalid status. Please enter 'complete' or 'incomplete'.")
    elif choice == "8":
        view_tasks()
        task_index = int(input("Enter the index of the task to delete: "))
        delete_task(task_index)
    elif choice == "9":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")

