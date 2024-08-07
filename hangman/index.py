import random

import arts
import words


# Check guessed letter is valid
def is_letter_valid(letter):
    if letter >= "a" and letter <= "z":
        return True
    return False


# Represent player progress with the guesses
def generate_user_guess(guessed_word: list):
    return " ".join(guessed_word)


# Hangman logo
print(arts.logo)

# Player lives
lives = list(arts.stages)
lives.reverse()

# Pick a random word
word = random.choice(words.word_list).lower()

# Player guesses
guessed_word = []
for _ in range(len(word)):
    guessed_word.append("_")

# Loop until player win/lose
while len(lives) > 1:
    print(f"Word to guess: {generate_user_guess(guessed_word)}")

    guessed_letter = input("Guess a letter: ").lower()

    # Check whether the guessed letter is valid
    if not is_letter_valid(guessed_letter):
        print("Invalid Letter. Try again.\n")
        continue

    # Check if the guess is correct or not
    found_index = word.find(guessed_letter)
    if found_index == -1:
        print(f"You guessed {guessed_letter}, that's not in the word. You lose a life.")
        lives.pop(0)
    else:
        letters = list(word)
        letters[found_index] = "#"
        word = "".join(letters)
        guessed_word[found_index] = guessed_letter
        print(generate_user_guess(guessed_word))

    # Check if the player has won or lost
    if "_" not in guessed_word:
        print("You win")
        break

    print(lives[0])
    print(f"*************************{len(lives)-1}/6 LIVES*************************")
    if len(lives) == 1:
        print("You lose")
