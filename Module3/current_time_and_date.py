import platform
import time
from datetime import datetime
import os
digits = {
    "0": [
        " ### ",
        "#   #",
        "#   #",
        "#   #",
        " ### "
    ],
    "1": [
        "  #  ",
        " ##  ",
        "  #  ",
        "  #  ",
        " ### "
    ],
    "2": [
        " ### ",
        "#   #",
        "   # ",
        "  #  ",
        "#####"
    ],
    "3": [
        " ### ",
        "#   #",
        "  ## ",
        "#   #",
        " ### "
    ],
    "4": [
        "   # ",
        "  ## ",
        " # # ",
        "#####",
        "   # "
    ],
    "5": [
        "#####",
        "#    ",
        "#### ",
        "    #",
        "#### "
    ],
    "6": [
        " ### ",
        "#    ",
        "#### ",
        "#   #",
        " ### "
    ],
    "7": [
        "#####",
        "    #",
        "   # ",
        "  #  ",
        "  #  "
    ],
    "8": [
        " ### ",
        "#   #",
        " ### ",
        "#   #",
        " ### "
    ],
    "9": [
        " ### ",
        "#   #",
        " ####",
        "    #",
        " ### "
    ],
    ":" : [
        "    ",
        ' ## ',
        "    ",
        " ## ",
        "    "
    ]
}

def clear_console():
    if platform.system() == "Windows":
        os.system("cls")
    else:
        os.system("clear")



def print_current_time():
    current_time = str(datetime.now()).split(" ")[1].split(".")[0]

    for row in range(5):
        for char in current_time:
            print(digits[char][row], end=" ")

        print()

while True:
    clear_console()
    time.sleep(1)
    print_current_time()