import data

COFFEE_TYPES = ["espresso", "latte", "cappuccino"]


def qty_with_unit(resource: str, qty: int):
    """
    Align each resource with the appropriate unit (ml, g,or $)
    """
    if resource == "water" or resource == "milk":
        return f"{qty}ml"
    elif resource == "money":
        return f"${qty}"
    else:
        return f"{qty}g"


def is_resource_available(coffee_type: str, resources: dict):
    """
    Check availability of resources to brew coffee
    """
    # Get ingredients for the requested coffee type
    ingredients = data.MENU[coffee_type]["ingredients"]

    # Check if resource for the requested coffee is available
    for ingredient in ingredients:
        if ingredients[ingredient] > resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False

    return True


def brew_coffee(coffee_type: str, resources: dict):
    """
    Brew requested coffee
    """
    # Check resource availability
    if not is_resource_available(coffee_type, resources):
        return
    # Get coins from the user
    print("Please insert coins.")
    amount = 0
    coins = data.COIN_TYPES
    for coin in coins:
        value = int(input(f"How many {coin}?: "))
        amount += value * coins[coin]

    # if coffee cost more, then exit
    coffee_price = data.MENU[coffee_type]["cost"]
    if coffee_price > amount:
        print("Sorry that's not enough money. Money refunded.")
        return

    # Decrease resources
    ingredients = data.MENU[coffee_type]["ingredients"]
    for ingredient in ingredients:
        resources[ingredient] -= ingredients[ingredient]
    # Store the profit
    resources["money"] += coffee_price

    print(f"Here is ${format(amount - coffee_price,'.2f')} in change.")
    print(f"Here is your {coffee_type} ☕ Enjoy!")


def run():
    """
    Startup coffee machine
    """
    resources = data.RESOURCES
    while True:
        user_input = input(f"What would you like? ({'/'.join(COFFEE_TYPES)}): ").lower()
        # Turn off coffee machine
        if user_input == "off":
            break
        # Generate report of resources
        elif user_input == "report":
            for res in resources:
                print(f"{res.title()}: {qty_with_unit(res, resources[res])}")
        # Brew coffee
        elif user_input in COFFEE_TYPES:
            brew_coffee(coffee_type=user_input, resources=resources)
        # Invalid user input
        else:
            print("Invalid input. Try again\n")


# Run coffee machine
run()
