import random

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

options = rock, paper, scissors
win_criteria = "02", "10", "21"

# Get choice from the user
human_choice = int(
    input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
)
if human_choice not in range(3):
    print("Wrong choice")
else:
    computer_choice = random.randint(0, 2)

    # Combine choices for comparison with the win_criteria
    combined_choice = f"{computer_choice}{human_choice}"

    print(options[human_choice])
    print(f"Computer choice:\n{options[computer_choice]}")

    # Check result and print
    if computer_choice == human_choice:
        print("Draw")
    elif combined_choice in win_criteria:
        print("You lose")
    else:
        print("You win")
