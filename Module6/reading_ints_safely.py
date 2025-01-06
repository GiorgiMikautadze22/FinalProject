def read_int(prompt, min, max):
    while True:
        try:
            user_num = int(input(prompt))
            if min < user_num < max:
                return f"The number is: {user_num}"
            else:
                print(f"Error: the value is not within permitted range: {min}-{max}")
        except ValueError:
            print("Error: Invalid Input")

v = read_int("Enter a number from -10 to 10: ", -10, 10)

print(v)