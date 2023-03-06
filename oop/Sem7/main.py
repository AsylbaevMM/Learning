from manager import TaskManager
import time


manager1 = TaskManager()
while True:
    print("""Hello! Choice your move:
    1. Add new task
    2. Show all tasks
    3. Show log 
    4. Exit""")
    choise = input(' >>>')


    if choise == '1':
        manager1.new_task()
    elif choise == '2':
        manager1.show_tasks()
    elif choise == '3':
        manager1.show_log()
    elif choise == "4":
        print("Good bye!")
        time.sleep(3)
        break
    else:
        print("Sorry, we hawe only 4 moves.")


