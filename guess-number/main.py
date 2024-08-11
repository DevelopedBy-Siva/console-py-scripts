import random

import art

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# Generate a random number for the user to guess
number = random.randint(1, 100)

# Difficulty modes
modes = {"easy": 10, "hard": 5}

# Select difficulty modes. If invalid mode, try again
while True:
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    attempts = modes.get(difficulty)
    if not attempts:
        print("Invalid input. Try again.")
        continue
    break

# loops until attempts are over
while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    # Take user input number
    guess = int(input("Make a guess: "))
    if guess == number:
        print(f"You got it! The answer was {number}")
        break
    elif guess > number:
        print("Too high.")
    else:
        print("Too low.")

    attempts -= 1
    # Attempts over
    if attempts == 0:
        print("You've run out of guesses, you lose.")
    else:
        print("Guess again.")
