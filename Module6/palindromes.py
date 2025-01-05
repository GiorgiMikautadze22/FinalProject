user_input = input("Enter text: ")

text = user_input.strip(" ").lower().replace(" ", "")

if text == text[::-1]:
    print("True")
else:
    print("False")