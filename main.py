from morse_data import MORSE_DATA

# Loop the program until the user decides to end it
generator_should_continue = True

print("Welcome to the Text to Morse Generator!")


def encode(start_text):
    """
    encode converts the text the user has written into morse

    :param start_text: the text the user has written
    :return: the morse equivalent is returned
    """
    result_text = ""
    for letter in start_text:
        # find the corresponding morse to the letter and add it to the result
        morse = MORSE_DATA[letter.capitalize()]
        result_text += morse
        result_text += " "
    return result_text


def decode(start_text):
    """
    decode converts the morse the user has written into text
    :param start_text: the morse the user has written
    :return: the text equivalent is returned
    """
    result_text = ""
    # split the morse into chunks to easier convert them into letters
    chunks = start_text.split(" ")
    # initially true in order to capitalize first letter
    capitalize = True
    for chunk in chunks:
        # find the corresponding key (character) according to value (morse)
        letter = [key for key, value in MORSE_DATA.items() if value == chunk][0]
        # if the chunk is a space in morse, the rest of code is skipped
        # this is to avoid setting capitalize to false when there is a space after a sentence
        if chunk == "/":
            result_text += letter
            continue
        # the first letter of every sentence is capitalized
        if capitalize:
            result_text += letter
            capitalize = False
        else:
            # rest of the letters are in lowercase
            result_text += letter.lower()
        # capitalize is set to true in order to capitalize the first letter of the next sentence
        if letter == "." or letter == "!" or letter == "?":
            capitalize = True
            continue
    return result_text


def generator(start_text, generator_direction):
    """
    generator converts either the text into morse or vice-versa
    :param start_text: the text or morse the user has written
    :param generator_direction: choice of user to encrypt or decode
    :return: the result, meaning the conversion
    """
    if generator_direction == "e":
        # text gets converted to morse
        return encode(start_text)
    elif generator_direction == "d":
        # morse gets converted to text
        return decode(start_text)
    else:
        # If the user has written something else when asked about direction
        result = "Error: you need to write 'e' or 'd'"
        return result


while generator_should_continue:
    # user is asked to either encrypt or decode
    direction = input("Type 'e' to encrypt or 'd' to decode: ")
    # user is asked to write the text or morse and the result is printed
    text = input("Type your text: ")
    print(generator(text, direction))
    # user is asked if they want to continue
    continue_or_not = input("Type 'y' if you want to go again, otherwise write 'n': ")
    # if user says no, then the program exits
    if continue_or_not == 'n':
        generator_should_continue = False
        print("Thank you and Good Bye!")
