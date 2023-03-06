from datetime import datetime
from deadline_maker import DeadlineMaker
from task import Task
from loggable import Loggable

class TaskManager(DeadlineMaker, Loggable):
    def __init__(self):
        self.task_storage = {}
        self.last_id = 1

    def new_task(self):
        name = input("Input task name >>> ")
        author = input("Input author name >>> ")
        priority = int(input("Input priority >>> "))
        deadline = int(input("How many days before deadline? >>> "))
        description = input("Input description >>> ")
        new = Task(self.last_id, name, author, description, priority, self.deadline(deadline))
        self.task_storage[self.last_id] = new
        self.last_id += 1
        self.log(new.info())
        print(self.last_id)

    def show_tasks(self):
        print(self.task_storage)
        print(self.last_id)
        for i in sorted(self.task_storage, key = lambda x: self.task_storage[x].priority):   
            print(self.task_storage[i].info())

    def show_log(self):
        with open('log.txt', 'r', encoding = 'utf-8') as file:
            print(file.read())

