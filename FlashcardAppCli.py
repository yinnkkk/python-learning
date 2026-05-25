import json
import time
with open("tasks.txt", "a") as f:
    pass
print("Welcome to my app. Enter a number to proceed: ")
def menu():
    while True:
        print("1 = show flashcards\n2 = add flashcard\n3 = delete flashcard\n4 = quiz me\n5 = quit")
        try:
            choice = int(input("Enter: "))
        except:
            print("That was not a proper number.")
            continue
        if choice == 1:
            show_flash()
            time.sleep(1)
        elif choice == 2:
            add_flash()
            time.sleep(1)
        elif choice == 3:
            del_flash()
            time.sleep(1)
        elif choice == 4:
            quiz()
        elif choice == 5:
            print("Please leave 5 stars on apple store...")
            break
        else:
            print("That was not a proper number.")

def add_flash():
    try:
        with open("flash.json", "r") as f:
            flashcard = json.load(f)
    except: 
        flashcard = []
    question = input("Question: ")
    answer = input("Answer: ")
    topic = input("Topic: ")
    dic = {"Question": question, "Answer": answer, "Topic": topic}
    flashcard.append(dic)
    with open("flash.json", "w") as f:
        json.dump(flashcard, f)

def show_flash():
    try:
        with open("flash.json", "r") as f:
            flashcard = json.load(f)
            for index, flash in enumerate(flashcard, start = 1):
                print(f"{index}. Question: {flash['Question']} | Answer: {flash['Answer']} | Topic: {flash['Topic']}")
        return flashcard
    except: 
        reaction = input("No flashcards currently. Wanna make some? (y/n)").lower()
        if reaction == "y":
            add_flash()
            return
        else:
            return
        
def del_flash():
    flashcard = show_flash()
    if flashcard:
        flashcard.pop(int(input("Which flashcard would you like to delete (Type the index number)")) - 1)
        print("Succesfully deleted.")
    else:
        reaction = input("No flashcards currently. Wanna make some? (y/n)").lower()
        if reaction == "y":
            add_flash()
            return
        else:
            return
    with open ("flash.json", "w") as f:
        json.dump(flashcard, f)


if __name__ == "__main__":
    menu()



        