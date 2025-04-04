import Tasks
import Stack


class TaskManager:
    def __init__(self):
        self.tasks = None
        self.undoStack = Stack.Stack()

    def addTasks(self, id, title, priority, due):
        self.tasks = Tasks.Task(id, title, priority, due, self.tasks)

    def viewTasks(self):
        current_node = self.tasks
        print_list = []

        while current_node != None:
            print_list.append(current_node)
            current_node = current_node.pointer

        print_list.reverse()

        for each in print_list:
            print(each)
        

    def removeTask(self, id):
        previous_node = None
        current_node = self.tasks

        if (current_node != None and current_node.id == id):
            self.undoStack.push(self.tasks)
            self.tasks = current_node.pointer
            return

        while (current_node != None and current_node.id != id):
            previous_node = current_node
            current_node = current_node.pointer


        if current_node is None:
            return

        self.undoStack.push(previous_node.pointer)
        previous_node.pointer = current_node.pointer

    def undoTasks(self):
        self.undoTask = self.undoStack.pop()
        self.undoTask.pointer = self.tasks
        self.tasks = self.undoTask

    # def saveTasks(self):
