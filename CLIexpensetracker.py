import json
with open("expenses.json", "a") as f:
    pass
print("Welcome to my app. Enter a number to proceed: ")
def menu():
    while True:
        print("1 = show expenses\n2 = add expenses\n3 = show total spent\n4 = show spent by category\n5 = delete expense\n6 = quit")
        try:
            choice = int(input("Enter: "))
        except:
            print("That was not a proper number. Try again.")
            continue
        if choice == 1:
            show_exp()
            input("Press Enter to continue...")  
        elif choice == 2:
            add_exp()
            input("Press Enter to continue...")  
        elif choice == 3:
            total_spent()
            input("Press Enter to continue...")  
        elif choice == 4:
            category_spent()
            print("Please Enter to continue..")
        elif choice == 5:
            delete_exp()
            print("Please Enter to continue..")
        elif choice == 6:
            print("Dont forget to leave 5 stars.")
            break
        else:
            print("Not a valid number!")

def show_exp():
    expenses = load_expenses()
    for index, expense in enumerate(expenses, start=1):
        print(f"{index}. {expense['name']} | {expense['price']} | {expense['category']}")
    return expenses
                                            
def add_exp():
    try:
        with open("expenses.json", "r") as f:
            expenses = json.load(f)
    except: 
        expenses = []
    name = input("Name of the expense? ").lower()
    try:
        price = int(input("Price of the expense? "))
    except:
        print("Not a valid number. Try again.")
        return
    category = input("Category of the expense? ").lower()
    dic = {"name": name, "price": price, "category": category}
    expenses.append(dic)
    save_expenses(expenses)

def total_spent():
    total = 0
    expenses = load_expenses()
    for expense in expenses:
        total += expense['price']
    print(f"You spent {total} bucks.")


def category_spent():
    category_total = {}
    expenses = load_expenses()
    for expense in expenses:
        category = expense['category']
        price = expense ['price']
        if category in category_total:
            category_total[category] += price
        else:
            category_total[category] = price
    for category, price in category_total.items():
        print(f"{category} | {price}")

def delete_exp():
    expenses = show_exp()
    if expenses:
        deleted_expense = expenses.pop(int(input("Which expense would you like to delete? (Type in the number)")) - 1)
        print(f"expense {deleted_expense} succesfully deleted")
        save_expenses(expenses)
    else:
        print("You have no expenses")


def load_expenses():
    try:
        with open("expenses.json", "r") as f:
            expenses = json.load(f)
    except:
        reaction = input("Your expense-list is empty. Do you want to add expenses? (Y/N): ")
        if reaction.lower() == "y":
            add_exp()
            return 
        else:
            return 
    return expenses

def save_expenses(expenses):
    with open("expenses.json", "w") as f:
        json.dump(expenses, f)

if __name__ == "__main__":
    menu()

