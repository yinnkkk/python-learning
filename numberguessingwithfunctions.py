import random
def get_difficulty_settings():
    while True:
        game_mode = input("Enter the games difficulty! Easy, Normal or Hard: ").lower()
        if game_mode == "easy":
            starting_attempts = 5
            max_number = 10
            break
        elif game_mode == "normal":
            starting_attempts = 7
            max_number = 30
            break
        elif game_mode == "hard":
            starting_attempts = 9
            max_number = 50
            break
        else:
            print("Seems like you misspelled something, try again.")
    return max_number, starting_attempts

def get_valid_guess(max_number):
    while True:
        try:
            guess = int(input(f"guess a numba from 1 to {max_number}: "))
            break
        except:
            print("That was not a propa number bucko..")
    return guess

def play_game(max_number, starting_attempts):
    number = random.randint(1,max_number)
    attempts = 1
    guess = get_valid_guess(max_number)
    while number != guess and starting_attempts > attempts:
        if guess > number:
            attempts += 1
            print(f"Nope! Too high! {starting_attempts - attempts} attempts left")
        else:
            attempts += 1
            print(f"Nope! Too low! {starting_attempts - attempts} attempts left")
        if attempts == starting_attempts:
            break
        guess = get_valid_guess(max_number)
    won = guess == number
    return attempts, won, number

def presentation(won,attempts,number):
    while won is True:
        if attempts == 1:
            print("Wow! You guessed it in one try!")
            break
        else:
            print(f"Correct guess! Took you {attempts} tries!")
            break
    if won is False:
        print(f"Damn, you lost. Correct number was {number}")

def main():
    max_number, starting_attempts = get_difficulty_settings()
    attempts, won, number = play_game(max_number, starting_attempts)
    presentation(won, attempts, number)

if __name__ == "__main__":
    main()

