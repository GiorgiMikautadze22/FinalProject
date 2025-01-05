user_birthday = input("Enter your birthday in format(YYYYMMDD): ")

def digit_of_file(birthday):
    num_list = []

    for num in birthday:
        num_list.append(int(num))

    result = sum(num_list)

    if result >= 10:
        digit_of_file(str(result))
    else:
        print(result)

digit_of_file(user_birthday)






