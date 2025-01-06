test_data = """
295743861
431865927
876192543
387459216
612387495
549216738
763524189
928671354
154938672
"""

horizontal = [list(row) for row in test_data.strip().split("\n")]

vertical = [[horizontal[row][col] for row in range(9)] for col in range(9)]

sub_tiles = [
    [horizontal[row][col]
     for row in range(block_row, block_row + 3)
     for col in range(block_col, block_col + 3)]
    for block_row in range(0, 9, 3)
    for block_col in range(0, 9, 3)
]

# Function to check validity of rows, columns, or sub-tiles
def check(data):
    return all(len(set(row)) == 9 and set(row) == set("123456789") for row in data)

is_valid = check(horizontal) and check(vertical) and check(sub_tiles)

print("Yes" if is_valid else "No")
