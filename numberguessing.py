import random
game_mode = input("Enter the games difficulty!: Easy, Normal or Hard: ").lower()
if game_mode == "easy":
    number = random.randint(1,10)
    attempts = 5
    starting_attempts = 5
    guess = int(input("Guess a number from 1 to 10: "))
elif game_mode == "normal":
    number = random.randint(1,50)
    attempts = 15
    starting_attempts = 15
    guess = int(input("Guess a number from 1 to 50: "))
elif game_mode == "hard":
    number = random.randint(1,100)
    attempts = 20
    starting_attempts = 20
    guess = int(input("Guess a number from 1 to 100: "))
else:
    print("You misspelled it! Restart the programm to retry.")
    exit()
while number != guess and attempts > 0:
    if guess > number:
        attempts -= 1
        print(f"Nope! Too high! {attempts} attempts left")
    else:
        attempts -= 1
        print(f"Nope! Too low! {attempts} attempts left")
    if attempts == 0:
        break
    guess = int(input("Guess again!: "))

if attempts <= 0:
    print(f"You lost... The correct number was {number}")
elif attempts <= starting_attempts - 1:
    print(f"Yoooo you got it in {starting_attempts - attempts} attempts !")
else:
    print("You got it first try!")