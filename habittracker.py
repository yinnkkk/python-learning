import json
with open("habits.json", "a") as f:
    pass
print("Welcome to my app. Enter a number to proceed: ")
def menu():
    while True:
        print("1 = show habits\n2 = add habits\n3 = complete habit\n4 = quit")
        try:
            choice = int(input("Enter: "))
        except:
            print("That was not a proper number. Try again.")
            continue
        if choice == 1:
            show_habits()
            input("Press Enter to continue...")  
        elif choice == 2:
            add_habits()
            input("Press Enter to continue...")  
        elif choice == 3:
            complete_habit()
            input("Press Enter to continue...")  
        elif choice == 4:
            print("Please leave 5 stars on apple store...")
            break
        else:
            print("Not a valid number!")

def show_habits():
    try:
        with open("habits.json", "r") as f:
            habits = json.load(f)
    except:
        reaction = input("Your dictionary is empty. Do you want to add habits? (Y/N): ")
        if reaction.lower() == "y":
            add_habits()
            return
        else:
            return
    for habit, count in habits.items():
        print(f"{habit}: {count}")
    return habits

def add_habits():
    try:
        with open ("habits.json", "r") as f:
            habits = json.load(f)
    except:
        habits = {}
    add = input("Which task would you like to add?")
    habits[add] = 0
    with open ("habits.json", "w") as f:
        json.dump(habits, f)
    return habits

def complete_habit():
    try:
        with open ("habits.json", "r") as f:
            habits = json.load(f)
    except:
        reaction = input("Your dictionary is empty. Do you want to add habits? (Y/N): ")
        if reaction.lower() == "y":
            add_habits()
            return
        else:
            return
    complete = input("Which habit did you complete?: ").lower()
    if complete in habits:
        habits[complete] += 1
        print(f"Succesfully completed {complete}")
    else: 
        print("This habit does not exist.")
        return
    with open ("habits.json", "w") as f:
        json.dump(habits, f)
    

if __name__ == "__main__":
    menu()

