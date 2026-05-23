import time
tasks = []
with open("tasks.txt", "a") as f:
    pass
print("Welcome to my app. Enter a number to proceed: ")
def menu():
    while True:
        print("1 = show tasks\n2 = add task\n3 = delete task\n4 = quit")
        try:
            choice = int(input("Enter: "))
        except:
            print("That was not a proper number.")
            continue
        if choice == 1:
            show_tasks()
            input("Press Enter to continue...")  
        elif choice == 2:
            add_tasks()
            input("Press Enter to continue...")  
        elif choice == 3:
            del_tasks()
        else:
            print("Please leave 5 stars on apple store...")
            break

def show_tasks():
    with open ("tasks.txt", "r") as f:
        tasks = f.readlines()
    if tasks:
        for index,task in enumerate(tasks, start=1):
            print(str(index) + ". " + task)
    else:
        reaction = input("Your list is empty. Do you want to add tasks? (Y/N): ")
        if reaction.lower() == "y":
            add_tasks()
    return tasks

def add_tasks():
    add = input("Which task would you like to add?")
    with open ("tasks.txt", "a") as f:
        f.write(add + "\n")
    with open ("tasks.txt", "r") as f:
        tasks = f.readlines()
    return tasks

def del_tasks():
    tasks = show_tasks()
    time.sleep(1)
    try:
        removed_task = tasks.pop(int(input("Which task would you like to remove? (type the index number)")) - 1)
        with open("tasks.txt", "w") as f: 
            for task in tasks: 
                f.write(task)
        print(f"{removed_task} succesfully removed.")
        input("Press Enter to continue...")  
    except:
        print("Make sure to enter the INDEX number.")
    return tasks

if __name__ == "__main__":
    menu()