import os

import art


# clear the console screen
def cls():
    os.system("cls" if os.name == "nt" else "clear")


# Perform mathematical operations
def calculate(op, fNumber, lNumber):
    """
        Perform mathematical operations
    Args:
        op: Type of Operation
        fNumber: First Number
        lNumber: First Number

    Returns:
        Result of the operation
    """
    if op == "+":
        return fNumber + lNumber
    elif op == "-":
        return fNumber - lNumber
    elif op == "*":
        return fNumber * lNumber
    else:
        return fNumber / lNumber


new_calculation = True
while True:

    if new_calculation:
        # print logo
        print(art.logo)
        new_calculation = False
        result = 0
        # Get first number
        fNumber = float(input("What's the first number?: "))

    # Get type of operation from the user
    operations = ["+", "-", "*", "/"]
    for op in operations:
        print(op)
    selected_operation = input("Pick an operation: ")
    if selected_operation not in operations:
        print("Invalid operation. Try again.\n")
        continue

    # Get second number
    lNumber = float(input("What's the next number?: "))

    # Calculate and print the result
    result = calculate(op=selected_operation, fNumber=fNumber, lNumber=lNumber)
    print(f"{fNumber} {selected_operation} {lNumber} = {result}")

    # Exit, continue or new calculation
    continue_calculating = input(
        f"Type 'y' to continue calculating with {result}, type 'n' to start a new calculation, or type 'exit' to quit calculator: "
    )

    # If user wants to quit, clear the console and exit the program
    if continue_calculating == "exit":
        cls()
        break

    # If user doesn't want to continue, clear the console and begin new calculation
    if continue_calculating == "n":
        new_calculation = True
        # clear console
        cls()
        continue

    # If user wants to continue, then the result is used as the first number
    fNumber = result
