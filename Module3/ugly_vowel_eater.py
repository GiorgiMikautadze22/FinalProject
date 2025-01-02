# Prompt the user to enter a word
# and assign it to the user_word variable.
user_word = input("Enter a word: ").upper()
vowels = ['A', 'E', 'I', 'O', 'U']

for letter in user_word:
    # Complete the body of the for loop.
    if letter in vowels:
        continue
    else:
        print(letter)
