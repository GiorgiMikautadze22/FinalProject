def is_year_leap(year):
#
# Your code from LAB 4.3.1.6.
    return (year % 100 != 0 and year % 4 == 0) or (year % 400 == 0)

#

def days_in_month(year, month):
#
# Your code from LAB 4.3.1.7.
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if is_year_leap(year) else 28
    return None
#

def day_of_year(year, month, day):
#
# Write your new code here.
    days = day
    for i in range(1, month):
        days += days_in_month(year, i)
    return days
#

print(day_of_year(2000, 12, 31))
