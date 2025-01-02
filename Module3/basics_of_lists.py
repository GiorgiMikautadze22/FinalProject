hat_list = [1, 2, 3, 4, 5]  # This is an existing list of numbers hidden in the hat.

# Step 1: write a line of code that prompts the user
# to replace the middle number with an integer number entered by the user.
user_num = int(input("Enter number: "))
middle_index = len(hat_list) // 2
hat_list[middle_index] = user_num

# Step 2: write a line of code that removes the last element from the list.
hat_list = hat_list[:-1]

# Step 3: write a line of code that prints the length of the existing list.
print("Length: ",len(hat_list))

print(hat_list)