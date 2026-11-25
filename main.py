from linkedList import *
from menu import *
from queue import *
from stat import *
from tasks import *

    # 1. Add task
    # 2. Update task
    # 3. Remove task
    # 4. Show all tasks
    # 5. Add task to queue
    # 6. Complete next task
    # 7. Undo
    # 8. Task history
    # 9. Show queue

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




