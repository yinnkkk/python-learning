import time
tasks = []
print("Welcome to my app. Enter a number to proceed.")
def menu():
    while True:
        print("1 = show tasks\n2 = add task\n3 = delete task\n4 = quit")
        choice = int(input("Enter:"))
        if choice == 1:
            show_tasks()
            input("Press Enter to continue...")  
        elif choice == 2:
            add_tasks()
            input("Press Enter to continue...")  
        elif choice == 3:
            del_tasks()
        else:
            break

def show_tasks():
    for index,task in enumerate(tasks):
        index = str(index)
        print(str(index) + ". " + task)

def add_tasks():
    add = input("Which task would you like to add?")
    tasks.append(add)

def del_tasks():
    show_tasks()
    time.sleep(1)
    tasks.pop(int(input("Which task would you like to remove? (type the index number)")))

if __name__ == "__main__":
    menu()