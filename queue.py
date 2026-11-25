queue = []


def enqueue(task):
    for x in queue:
        if x["id"] == task["id"]:
            print("Task is already in the queue!")
            return

    queue.append(task)
    print(f"{task['name']} added to queue.")


def deQueue():
    if not queue:
        print("Queue is empty!")
        return None

    deQueue = queue.pop(0)
    print(deQueue, "removed in queue")
    return deQueue


def showQueue():
    if not queue:
        print("Queue is empty!")
        return

    for task in queue:
        print(f"ID: {task['id']}")
        print(f"Name: {task['name']}")
        print(f"Status: {task['status']}")