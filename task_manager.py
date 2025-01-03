# This is a simple task management app. It will take the number of tasks from the user and
# then it will take the task name from the user and store it in a list.
# Then it will ask the user to perform the following operations like vew, add, update, delete, and exit.

def task():
    tasks = []
    print("------Welcome to the task amnagement app------")
    
    total_task = int(input("Enter how many tasks you want to add : "))
    for i in range(1, total_task+1):
        task_name = input(f"Enter task {i} : ")
        tasks.append(task_name)

    print(f"Today's tasks are \n{tasks}")
    while True:
        operation = int(input("\nEnter \n1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop\n"))
        if operation == 1:
            add = input("Enter task you want to add : ")
            tasks.append(add)
            print(f"task {add} has been successfully added.")

        elif operation == 2:
            updated_val = input("Enter the task name you want to update : ")
            if updated_val in tasks:
                up = input("Enter new task : ")
                ind = tasks.index(updated_val)
                tasks[ind] = up
                print("task updated")
            else:
                print("task not found.")

        elif operation == 3:
            del_val = input("which task you wnat to delete : ")
            if del_val in tasks:
                ind = tasks.index(del_val)
                del tasks[ind]
                print(f"{del_val} has beeen deleted.")

        elif operation == 4:
            print(f"total task is/are {tasks}")

        elif operation == 5:
            print("programe is closed. Thank you for using our application.")
            break
        else:
            print("Invalid input")    
task()