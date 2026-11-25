from linkedList import *
from menu import *
from queue1 import *
from stat import *
from tasks import *
from stack import *


def getInt(text):
    while True:
        try:
            return int(input(text))
        except ValueError:
            print("Please enter a valid number.")

def main():

    while True:
        showMenu()

        choice = getInt("Enter choice: ")

        if choice == 1:

            name = input("Enter task name: ")
            addTask(name)
            push(tasks[-1])

            input("\nPress ENTER to continue...")

        elif choice == 2:

            getTaskID = getInt("Enter task ID: ")
            taskID = getTaskID
            name = input("Enter new task name: ")

            updateTask(taskID, name)

            input("\nPress ENTER to continue...")

        elif choice == 3:

            getTaskID = getInt("Enter task ID: ")
            taskID = getTaskID

            removeTask(taskID)

            input("\nPress ENTER to continue...")

        elif choice == 4:           
            showTasks()
            input("\nPress ENTER to continue...")

        elif choice == 5:

            getTaskID = getInt("Enter task ID: ")
            taskID = getTaskID

            enqueue(taskID)

            input("\nPress ENTER to continue...")

        elif choice == 6:

            task = deQueue()

            if task:
                task['status'] = 'Completed'
                addToHistory(task)
                print(f"Task completed: {task['name']}")

            input("\nPress ENTER to continue...")

        elif choice == 7:
            undo(tasks)
            input("\nPress ENTER to continue...")

        elif choice == 8:
            showHistory()
            input("\nPress ENTER to continue...")

        elif choice == 9:
            showQueue()
            input("\nPress ENTER to continue...")

        elif choice == 0:
            print('Closing..')
            break

        else:
            print('Something went wrong...')
            input("\nPress ENTER to continue...")
            continue

main()






