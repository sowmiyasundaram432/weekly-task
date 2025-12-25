def todo_list():
 task=[]
 while True:
    T=input("add or view or remove or exit:").lower()
    if T=="add":
        t=input("Enter the task:")
        task.append(t)
        print("Task added sucessfully")
    elif T=="view":
        if len(task)==0:
            print("To Do List is empty add task to view")
        else:
            for x in task:
             print(f"-{x}")
    elif T=="remove":
        s=input("Enter task to remove:")
        if len(task)==0:
            print("To Do List is empty")
        #s=input("Enter task to remove:")
        if s in task:
                task.remove(s)
                print("Task is removed")
    elif T=="exit":
        break
todo_list()