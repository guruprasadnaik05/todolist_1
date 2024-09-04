tasks = []

def addTask():
  task=input("please enter a task:")
  tasks.append(task)
  print(f"Task '{task}' added to the list.")

def listTasks():
  if not tasks:
    print("there are no tasks currently.")
  else:
    print("current tasks:")
    for index, task in enumerate(tasks):
      print(f"Task #{index}. {task}")

def deleteTask():
  listTasks()
  try:
    taskToDelete=int(input("Enter the # to delete:"))
    if taskToDelete >=0 and taskToDelete < len(tasks):
      tasks.pop(taskToDelete)
      print(f"Task '{taskToDelete}' has been removed.")
    else:
      print(f"Task #{taskToDelete} was not found.")

  except:
    print("Invalid input.")


if __name__ == "__main__":
      ###create a loop for run the app
      print("Welcome to the to do list app :)")
      while True:
          print("\n")
          print("please select one of the following options")
          print("------------------------------------------")
          print("1. add a new task")
          print("2. delete a task")
          print("3. list tasks")
          print("4. quit")

          choice = input("enter your choice:")

          if(choice == "1"):
            addTask()
          elif(choice == "2"):
            deleteTask()
          elif(choice=="3"):
            listTasks()
          elif(choice=="4"):
            break
          else:
            print("Invalid input. please try again.")
          
