for num in range(1, 16):
    square = f"{num} * {num} = {num ** 2}".ljust(30)
    power_10 = f"{num} ^ 10 = {num ** 10}".ljust(30)
    power_num = f"{num} ^ {num} = {num ** num}"

    print(square, power_10, power_num, sep="|")