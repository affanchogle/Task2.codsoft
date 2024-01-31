tasks =[]
t=len(tasks)

def addTask():
    task = input("Enter a task:")
    tasks.append(task)
print(f"Task{tasks} added to the list.")

def listTask():
    if not tasks:
        print("There is no tasks currentlly.")
    else:
        print("     ")
        print("Current Tasks:-")
        for index,task in enumerate(tasks):
            print(f"    Task{index}:'{task}'.")

def deleteTask():
    listTask()
    try:
        taskToDelete=int(input("Chose the task you want to delete:"))
        if taskToDelete >=0 and taskToDelete < len(tasks):
            tasks.pop(taskToDelete)
            print(f"Task{taskToDelete} has been removed.")
        else:
            print(f"Task {taskToDelete} was not found.")
    except:
        print("Invalid Input.")
        


if __name__=="__main__":
    print("Welcome to the to do list app:")
    while True:
        print("\n")
        print("Please select one of the following option")
        print("------------------------------")
        print("1.Add a new task")
        print("2.Delete a task")        
        print("3.List task")
        print("4.Quit")
        
        choice =input("Enter your choice:")
        
        if(choice== "1"):
            addTask()
        elif(choice=="2"):
            deleteTask()
        elif(choice=="3"):
            listTask()
        elif(choice=="4"):
            break
        else:
            print("Invallid Input.Please try again.")
    print("Goodbye")