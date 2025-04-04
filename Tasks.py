class Task:
    def __init__(self, id, title, priority, due, pointer):
        self.setID(id)
        self.setTitle(title)
        self.setPriority(priority)
        self.setDue(due)
        self.setPointer(pointer)
    
    def setID(self, id):
        self.id = id

    def setTitle(self, title):
        self.title = title

    def setPriority(self, priority):
        self.priority = priority

    def setDue(self, due):
        self.due = due

    def setPointer(self, pointer):
        self.pointer = pointer

    def getID(self):
        return (self.id)

    def getTitle(self):
        return self.title
    
    def getPriority(self):
        return self.priority
    
    def getDue(self):
        return self.due
    
    def getPointer(self):
        return self.pointer
    
    def __str__(self):
        return f"ID: {self.id} Title: {self.title}, Priority: {self.priority}, Due: {self.due}"