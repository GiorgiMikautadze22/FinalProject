
# capitalize() - Converts the first character to upper case and all the others into lowercase
print("my name is GIORGI".capitalize(), end="\n")

# casefold() - Converts string into lowercase
print("my name is Giorgi".casefold(), end="\n")

# center() - returns a centered string
print("my name is Giorgi".center(50, "-"), end="\n")

# count() - returns the number of times a specified value occurs in a string
print("my name is Giorgi".count("i"), end="\n")

# encode() - returns encoded version of a string
print("my name is Giorgi".encode(), end="\n")

# endswith() - Returns true if the string ends with the specified value
print("my name is Giorgi".endswith("Giorgi"), end="\n")

# expandtabs() - Sets the tab size of the string
print("\t my name is Giorgi".expandtabs(12), end="\n")

# find() - Searches the string for a specified value and returns the position of where it was found
print("my name is Giorgi".find("Giorgi"), end="\n")

# format() - Formats specified values in a string
print("The sum of 1 + 2 is {0}".format(1+2), end="\n")

# format_map() Formats specified values in a string
class Default(dict):
    def __missing__(self, key):
        return key

print("My name is {name}".format_map(Default(name="Giorgi")), end="\n")







