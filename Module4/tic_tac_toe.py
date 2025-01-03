import random
tic_tac_toe = [[1,2,3], [4,5,6], [7,8,9]]

def display_board(board):
    print("+-------+-------+-------+")
    for i in range(3):
        print("|       |       |       |")
        print(f"|   {board[i][0]}   |   {board[i][1]}   |   {board[i][2]}   |")
        print("|       |       |       |")
        print("+-------+-------+-------+")


def enter_move(board):
    # The function accepts the board's current status, asks the user about their move,
    # checks the input, and updates the board according to the user's decision.
    user_choice = int(input("What's your move?: "))
    occupied = True
    for row in board:
        for col in row:
            if col == user_choice:
                index = row.index(col)
                row[index] = "O"
                occupied = False
    if occupied:
        display_board(board)
        print("Invalid input. Please try again")
        enter_move(board)

    check_winner(board)


def computer_move(board):
    random_row = random.choice([0,1,2])
    random_col = random.choice([0,1,2])

    if board[random_row][random_col] == "X" or board[random_row][random_col] == "O":
        computer_move(board)
    else:
        board[random_row][random_col] = "X"

    check_winner(board)

        
def check_winner(board):
    pass
    # Condition 1: If all rows are filled

    # Condition 2: If indexes of all columns match

    # Condition 3: If indexes of rows match the index of the row


tic_tac_toe[1][1] = "X"
while True:
    display_board(tic_tac_toe)
    enter_move(tic_tac_toe)
    computer_move(tic_tac_toe)
