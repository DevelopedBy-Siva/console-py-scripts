import os
import random

import data


# clear the console screen
def cls():
    os.system("cls" if os.name == "nt" else "clear")


# Get details
def get_info(detail: dict):
    name = detail.get("name", "")
    description = detail.get("description", "")
    country = detail.get("country", "")
    followers = detail.get("follower_count", "")
    return name, description, country, followers


# Run the game
def run():

    result = None
    score = 0
    options = []
    game_over = False
    details = data.infos

    # Loop till the player fails
    while True:

        # Generate random choices. Max options is 2
        while len(options) != 2:
            opt = random.randint(0, len(details) - 1)
            if opt not in options:
                options.append(details[opt])

        cls()  # Clear the console
        # Logo
        print(data.higher_lower_logo)

        # Display result
        if result:
            print(result)

        # if game over, then exit
        if game_over:
            break

        # Retrieve & display information
        data_A = get_info(options[0])
        data_B = get_info(options[1])

        print(f"Compare A: {data_A[0]}, a {data_A[1]}, from {data_A[2]}.")
        # Logo
        print(data.vs_logo)
        print(f"Against B: {data_B[0]}, a {data_B[1]}, from {data_B[2]}.")

        # Get user guess
        player_input = input("Who has more followers? Type 'A' or 'B': ").lower()
        if player_input not in ["a", "b"]:
            result = "Invalid input. Try again."
            continue

        # Verify the result
        options.pop(0)
        if (player_input == "a" and data_A[3] >= data_B[3]) or (
            player_input == "b" and data_B[3] >= data_A[3]
        ):
            score += 1
            result = f"You're right! Current score: {score}"
        else:
            result = f"Sorry, that's wrong. Final score: {score}"
            game_over = True


run()
