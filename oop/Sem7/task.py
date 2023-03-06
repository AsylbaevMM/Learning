from loggable import Loggable
from datetime import datetime

class Task(Loggable):
    def __init__(self,id, name, author, description, priority, deadline):
        self.id = id
        self.name = name
        self.author = author
        self.created = datetime.now()
        self.description = description
        self.priority = priority
        self.deadline = deadline
        
    
    def info(self):
        return f"Task {self.name} with id = {self.id} by {self.author} created {self.created.strftime('%d %b %Y, %H:%M:%S')} \
with priority={self.priority} and deadline at {self.deadline.strftime('%d %b %Y, %H:%M')} \
having description: {self.description}"
    
    