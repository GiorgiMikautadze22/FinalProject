
# For Loop Implementation
for i in range(1, 11):
    print('Hello World! ', i)


print("-"  * 50)
# While Loop Implementation
count = 0
while count < 10:
    count += 1
    print('Hello World! ', count)

print("-"  * 50)

# Recursion Implementation
def print_hello(num = 1):
    print('Hello World!', num)
    if num < 10:
        print_hello(num + 1)

print_hello()
