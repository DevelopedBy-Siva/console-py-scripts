import os

import art

# Print logo
print(art.logo)


# clear the console screen
def cls():
    os.system("cls" if os.name == "nt" else "clear")


bidders = []

while True:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bidders.append({"name": name, "bid": bid})
    bid_again = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()

    # Continue bidding
    if bid_again == "yes":
        cls()
        continue

    # Check highest bidder
    highest_bidder_index = 0
    for index in range(len(bidders)):
        if bidders[index]["bid"] > bidders[highest_bidder_index]["bid"]:
            highest_bidder_index = index
    winner = bidders[highest_bidder_index]

    # Print winner
    print(f'The winner is {winner["name"]} with a bid of ${winner["bid"]}')
    # End bidding
    break
