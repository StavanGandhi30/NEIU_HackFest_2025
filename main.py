from TaskManager import TaskManager

taskManager = TaskManager()

taskManager.addTasks("1","Title1", "1", "5")
taskManager.addTasks("2", "Title2", "2", "6")
taskManager.addTasks("3","Title3", "3", "7")
taskManager.addTasks("4", "Title4", "4", "8")
taskManager.addTasks("5","Title5", "5", "9")
taskManager.addTasks("6", "Title6", "6", "10")
taskManager.viewTasks()

print("\n\n")
taskManager.removeTask("2")
taskManager.viewTasks()

print("\n\n")
taskManager.undoTasks()
taskManager.viewTasks()