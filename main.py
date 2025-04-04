class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)
    
    def pop(self):
        if self.isEmpty():
            return "Stack is empty"
        return self.stack.pop()
    
    def isEmpty(self):
        return len(self.stack) == 0
    
class Task:
    def __init__(self, id, title, priority, due, pointer):
        self.setID(id)
        self.setTitle(title)
        self.setPriority(priority)
        self.setDue(due)
        self.setPointer(pointer)
    
    def setID(self, id):
        self.id = str(id)

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
    
    def getDataforSaving(self):
        return [self.id, self.title, self.priority, self.due]
        
    def __str__(self):
        return f"ID: {self.id}, Title: {self.title}, Priority: {self.priority}, Due: {self.due}"

class TaskManager:
    def __init__(self, filename=None):
        self.tasks = None
        self.length = 0
        self.undoStack = Stack()
        self.delimiter = ";$:@:$;"
        self.filename = "tasks.txt"

        if (filename != None):
            self.loadFile(filename)

    def addTasks(self, title, priority, due, printMsg=True):
        self.tasks = Task(id=self.length,title=title, priority=priority, due=due, pointer=self.tasks)
        print(self.tasks)
        self.length += 1
        if (printMsg):
            print("Task added successfully!\n")

    def viewTasks(self):
        current_node = self.tasks
        print_list = []

        while current_node != None:
            print_list.append(current_node)
            current_node = current_node.pointer

        print_list.reverse()

        if (len(print_list) == 0):
            print("""
(No tasks to display)

1. Add a Task
2. View All Tasks
3. Complete a Task
4. Undo Last Action
5. Exit
                  """)
            
        for each in print_list:
            print(each)

        print("\n")

    def removeTask(self, id):
        previous_node = None
        current_node = self.tasks

        if (current_node is not None and current_node.id == id):
            self.undoStack.push(self.tasks)
            self.tasks = current_node.pointer
            self.length -= 1
            return

        while (current_node is not None and current_node.id != id):
            previous_node = current_node
            current_node = current_node.pointer

        if current_node is None:
            print(f"Id: {id} Doesn't exist")
            return

        self.length -= 1
        self.undoStack.push(previous_node.pointer)
        previous_node.pointer = current_node.pointer
        print("\n")

    def undoTasks(self):
        try:
            self.undoTask = self.undoStack.pop()
            self.undoTask.pointer = self.tasks
            self.tasks = self.undoTask
            self.length += 1
            print("Last action undone successfully!\n")
        except:
            print("Nothing to Undo!")

    def clearFile(self):
        f = open(self.filename, "w")
        f.write("")
        f.close()
        
    def saveFile(self):
        self.clearFile()

        f = open(self.filename, "a")

        current_node = self.tasks
        save_List = []

        while current_node != None:
            save_List.append(current_node.getDataforSaving())
            current_node = current_node.pointer

        save_List.reverse()

        for each in save_List:
            f.write(f"{each[0]}{self.delimiter}{each[1]}{self.delimiter}{each[2]}{self.delimiter}{each[3]}\n")

        f.close()

    def loadFile(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                data=line.strip().split(self.delimiter)
                self.addTasks(data[1], data[2], data[3], printMsg=False)

        print("File loaded successfully!")

def initMsg():
    print("Welcome to Task Manager Simulator!\n")
    print("1. Add a Task")
    print("2. View All Tasks")
    print("3. Complete a Task")
    print("4. Undo Last Action")
    print("5. Exit")

def isInputValid(userInput):
    try:
        userInput = int(userInput)
        return True
    except ValueError:
        print("Error: User Input must be a valid number only")
        return False

def addTaskInput():
    print("\n")
    taskTitle = input("Enter task title: ")
    taskPriority = input("Enter priority (1 = high, 2 = medium, 3 = low): ")
    taskDue = input("Enter time estimate (minutes): ")
    taskManager.addTasks(taskTitle, taskPriority, taskDue)

def removeTaskInput():
    print("\n")
    try:
        taskId = str(input("Enter Task Id that you wanna remove: "))
        taskManager.removeTask(taskId)
    except:
        print("Something Went Wrong!")

def main():

    initMsg()
    
    while True:
        userInput = input("Choose an option: ")
        if isInputValid(userInput):
            userInput = int(userInput)
            
            try:
                match userInput:
                    case 1:
                        addTaskInput()
                    case 2:
                        taskManager.viewTasks()
                    case 3:
                        removeTaskInput()
                    case 4:
                        taskManager.undoTasks()
                    case 5:
                        print("GoodBye!")
                        break
                    case _:
                        print("Error: Input must be between 1 to 5")
            except:
                print("Something went wrong!")

        print("\n")

# taskManager = TaskManager(filename="tasks.txt") # To load from file
taskManager = TaskManager()

if (__name__ == "__main__"):
    main()