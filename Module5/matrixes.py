import numpy as np
from colorama import Fore, init

init()

A = np.array([
    [0, 1, 2, 3, 4],
    [5, 6, 7, 8, 9],
    [10, 11, 12, 13, 14],
])

B = np.array([
    [0,1,2,3,4],
    [5,6,7,8,9],
    [10,11,12,13,14],
])


transpose = A.T
print(Fore.RED + str(transpose))

print()

rotated_90 = np.rot90(A, k=1)
print(Fore.GREEN + str(rotated_90))

print()

rotated_180 = np.rot90(A, k=2)
print(Fore.GREEN + str(rotated_180))

print()

rotated_270 = np.rot90(A, k=3)
print(Fore.GREEN + str(rotated_270))

print()

mirrored_right_to_left = np.flip(A)
print(Fore.GREEN + str(mirrored_right_to_left))

print()

mirrored_left_to_right= np.fliplr(A)
print(Fore.GREEN + str(mirrored_left_to_right))

print()

C = np.array([
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20]
])

D = np.array([
    [2,2,2,2,2],
    [2,2,2,2,2],
    [2,2,2,2,2],
    [2,2,2,2,2],
])


horizontally_stacked = np.hstack((C,D))
print(horizontally_stacked)

print()

vertically_stacked = np.vstack((C,D))
print(vertically_stacked)

print()


CD = np.hstack((C,D))
DC = np.hstack((D,C))
all_stacked = np.vstack((CD,DC))
print(all_stacked)

print()

D = np.array([
    [2,2,2,2],
    [2,2,2,2],
    [2,2,2,2],
    [2,2,2,2],
    [2,2,2,2],
])

multiply = np.dot(C,D)
print(multiply)

