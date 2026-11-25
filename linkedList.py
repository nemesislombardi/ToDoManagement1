head = None


def addToHistory(task):
    global head

    node = {
        "data": task.copy(),
        "next": None
    }

    if head is None:
        head = node
        return

    current = head

    while current["next"]:
        current = current["next"]

    current["next"] = node


def showHistory():
    if head is None:
        print("Task history is empty!")
        return

    current = head

    while current:
        task = current["data"]

        print(f"ID: {task['id']}")
        print(f"Name: {task['name']}")
        print(f"Status: {task['status']}")

        current = current["next"]