user_input = input("What do you want to encode?: ")
num = int(input("How many shifts?: "))


def caesar_cipher(word, shift):
    alphabet = [
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
        "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
    ]

    encoded_word = ""

    for char in word:
        if char not in alphabet:
            encoded_word += char
        else:
            index = alphabet.index(char)
            new_index = (index + shift) % 26
            encoded_word += alphabet[new_index]

    return encoded_word

print(caesar_cipher(user_input, num))