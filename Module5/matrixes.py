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
print(Fore.BLUE + str(transpose))