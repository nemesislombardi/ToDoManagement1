stack = []


def push(task):
    stack.append(task.copy())


def undo(tasks):
    if not stack:
        print("Undo history is empty!")
        return

    lastTask = stack.pop()

    for task in tasks:
        if task["id"] == lastTask["id"]:
            tasks.remove(task)
            print(f"Undo: {lastTask['name']} deleted.")
            return

    print("Task was already deleted!")