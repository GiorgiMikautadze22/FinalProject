#TODO: Write a function that checks if the year is leap year
#TODO: Write a function that that returns in which day the month is starting
#TODO: Write a function that returns how many days is in a month
#TODO: Write a function that print the result

def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


def get_starting_day(year, month):
    # Zeller's Congruence algorithm to calculate the day of the week
    if month < 3:
        month += 12
        year -= 1
    k = year % 100
    j = year // 100
    day = (1 + 13 * (month + 1) // 5 + k + k // 4 + j // 4 - 2 * j) % 7
    return (day + 5) % 7  # Convert Zeller's day to start with Monday as 0

def get_month_days(month, year):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if is_leap_year(year) else 28
    return 0


def print_calendar():
    user_input = input("Enter a month and a year ( example: 11-2004 ): ")
    year = int(user_input.split("-")[1])
    month = int(user_input.split("-")[0])

    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]

    weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

    print(months[month - 1].rjust(15), year)
    print(" ".join(weekdays))

    current_day = 1
    for row in range(6):
        if current_day > get_month_days(month, year):
            break
        for column in range(7):
            if current_day > get_month_days(month, year):
                break
            elif row == 0 and column < get_starting_day(year, month):
                print("", end=" "*4)
            else:
                print(f"{current_day:2}  ", end="")
                current_day += 1

        print()

print_calendar()