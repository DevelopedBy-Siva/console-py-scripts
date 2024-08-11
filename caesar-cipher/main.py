import data

# Logo
print(data.logo)

# Alphabets in lowercase
alphabets = list(data.alphabets)


# Get transformed letter index
def get_position(letter_index, shift, encode=True):
    # To reduce large shift numbers
    to_move = shift - 26 * (shift // 26)
    if encode:
        pos = to_move + letter_index
        if pos < 26:
            return pos
        return pos - 26
    return letter_index - to_move


def is_alphabet_lower(letter: str):
    if letter >= "a" and letter <= "z":
        return True
    elif letter >= "A" and letter <= "Z":
        return False
    else:
        return None


# Encode or Decode the text
def encode_or_decode(text: str, shift: int, encode: bool):
    transformed_text = ""
    for letter in text:
        # Check is Alphabet and lower or upper case
        is_lower = is_alphabet_lower(letter)
        if is_lower != None:
            index = alphabets.index(letter.lower())
            position = get_position(index, shift, encode)
            alphabet = alphabets[position]
            # Is letter is uppercase, covert it to uppercase, else lower
            if not is_lower:
                transformed_text += alphabet.upper()
            else:
                transformed_text += alphabet
        else:
            transformed_text += letter
    return transformed_text


# Loop until the users says 'no'
while True:
    what_to_do = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    # Validate user input
    if what_to_do not in ["encode", "decode"]:
        print("Invalid input. Try again.\n")
        continue

    # Take input from the user
    message = input("Type your message:\n")
    shift_number = int(input("Type the shift number:\n"))

    # Encode or Decode
    if what_to_do == "encode":
        result = encode_or_decode(message, shift_number, encode=True)
        print(f"Here's the encoded result: {result}")
    else:
        result = encode_or_decode(message, shift_number, encode=False)
        print(f"Here's the decoded result: {result}")

    # Exit or Continue
    try_again = input(
        "Type 'yes' if you want to go again. Otherwise type 'no'.\n"
    ).lower()

    if try_again == "yes":
        continue
    else:
        print("Goodbye")
        break
