import random
import os

import art


# clear the console screen
def cls():
    os.system("cls" if os.name == "nt" else "clear")


# Play/Stop the game
def is_play(option: str):
    if option.lower() == "y":
        return True
    return False


# Calculate the score
def find_score(data: dict):
    return sum(data["draws"])


# Check if the draw is done
def is_draw_done(data: dict):
    return data["is_stopped"]


# Get the user or computer draws
def get_draws(data: dict, key: str = "computer"):
    return data[key]["draws"]


# Check if game is over and print the results
def game_result(data: dict):

    # Calculate the scores
    user_total = find_score(data["user"])
    comp_total = find_score(data["computer"])

    # Is user or computer draw is completed or not
    is_user_over = is_draw_done(data["user"])
    is_comp_over = is_draw_done(data["computer"])

    result = None
    # Check if the user or computer went over 21
    if user_total > 21:
        result = "You went over. You lose 😭"
    elif comp_total > 21:
        result = "Computer went over. You win 😁"
    # Both draws are completed, end the game
    elif is_user_over and is_comp_over:
        if user_total == comp_total:
            result = "Draw 🙃"
        elif comp_total > user_total:
            result = "You lose 😤"
        else:
            result = "You win 😁"

    # Game Over! Display results
    if result:
        user_draws = get_draws(data, "user")
        comp_draws = get_draws(data)
        print(f"\tYour final hand: {user_draws}, final score: {user_total}")
        print(f"\tComputer's final hand: {comp_draws}, final score: {comp_total}")
        print(f"{result}\n")
        return True

    return False


# Check if user or computer draw is completed, if not draw again
def draw_cards(data: dict, key: str, draw_more=True):

    # Draw completed or not
    is_over = is_draw_done(data[key])

    # Not completed, then draw again
    if not is_over:
        if (key == "user" and draw_more) or key == "computer":
            # Perform a random draw
            data[key]["draws"].append(random.randint(1, 10))

        # If 'computer', then randomize whether to draw or stop
        if key == "computer":
            draw_again = random.choice([True, False])
        else:
            # Based on user input ('y' or 'n'), decide whether to draw or stop
            draw_again = draw_more
        # Update the game data
        if not draw_again:
            data[key]["is_stopped"] = True


# Display current score and prompt for user input to continue drawing
def display_score_and_prompt(data: dict):
    user_draw_more = True
    # If user stopped drawing, don't display current score
    if not is_draw_done(data["user"]):
        u_total = find_score(data["user"])
        print(f"\t  Your cards: {get_draws(data, 'user')}, current score: {u_total}")
        print(f"\t  Computer's first card: {get_draws(data)[0]}")

        # if user went over '21', then don't take input from user
        if find_score(data["user"]) <= 21:
            another_card = input("Type 'y' to get another card, type 'n' to pass: ")
            user_draw_more = is_play(another_card)

    return user_draw_more


# Play the game
def play_game():
    # Initialize the game date
    data = {
        "user": {"draws": [], "is_stopped": False},
        "computer": {"draws": [], "is_stopped": False},
    }
    user_draw_more = True

    # Make the first user draw
    draw_cards(data, "user", user_draw_more)

    # Loop until the the game result is generated
    while True:

        # If game is over, end the game
        if game_result(data):
            break

        # Draw cards for user and computer
        draw_cards(data, "user", user_draw_more)
        draw_cards(data, "computer")

        # Display the user result and ask for keep drawing
        user_draw_more = display_score_and_prompt(data)


# Run the game until the user exit
while True:
    # Start the game or not
    start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    # Clear the console and start the game
    if is_play(start_game):
        cls()
        print(art.logo)
        play_game()
    else:
        # stop the game
        break
