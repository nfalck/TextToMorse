from morse_data import MORSE_DATA
generator_should_continue = True

print("Welcome to the Text to Morse Generator!")

def encode(start_text):
    result_text = ""
    for letter in start_text:
        morse = MORSE_DATA[letter.capitalize()]
        result_text += morse
        result_text += " "
    return result_text
def decode(start_text):
    result_text = ""
    chunks = start_text.split(" ")
    capitalize = True
    for chunk in chunks:
        letter = [k for k, v in MORSE_DATA.items() if v == chunk][0]
        if chunk == "/":
            result_text += letter
            continue
        if capitalize:
            result_text += letter
            capitalize = False
        else:
            result_text += letter.lower()
        if letter == "." or letter == "!" or letter == "?":
            capitalize = True
            continue
    return result_text

def generator(start_text, generator_direction):
    if generator_direction == "e":
        return encode(start_text)
    elif generator_direction == "d":
        return decode(start_text)
    else:
        result = "Error: you need to write 'e' or 'd'"
        return result

while generator_should_continue:
    direction = input("Type 'e' to encrypt or 'd' to decrypt: ")
    text = input("Type your text: ")
    print(generator(text, direction))
    continue_or_not = input("Type 'y' if you want to go again, otherwise write 'n': ")
    if continue_or_not == 'n':
        generator_should_continue = False
        print("Thank you and Good Bye!")