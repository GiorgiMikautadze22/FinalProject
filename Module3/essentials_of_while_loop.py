blocks = int(input("Enter the number of blocks: "))

height = 0
#
# Write your code here.
while blocks - height > 0:
    height += 1
    blocks -= height
    print(height, blocks)
#

print("The height of the pyramid:", height)