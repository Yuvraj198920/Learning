tasks = []

def addTasks(task):
    tasks.append(task)
    print('Task added to the list')

def complete_task(index):
    if index < len(tasks):
        tasks[index] += "[COMPLETE]"
        print("Task marked as complete")
    else:
        print("Invalid task index!")


def view_tasks():
    if len(tasks) > 0:
        print("Tasks....")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")
    else:
        print("No tasks found.")

addTasks("Finish Homework")
complete_task(0)
view_tasks()