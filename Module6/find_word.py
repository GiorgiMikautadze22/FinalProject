first_string = input("First text: ")
second_string = input("Second text: ")

match = True
current_pos = 0

for char in first_string:
    index = second_string.find(char, current_pos)
    if index == -1:
        match = False
        break
    current_pos += 1



if match:
    print("yes")
else:
    print('no')