first_word = input("Enter first word: ")
second_word = input("Enter second word: ")

anagram = [char for char in first_word if char in second_word]

if len(anagram) == len(second_word):
    print("Anagram")
else:
    print("Not Anagram")