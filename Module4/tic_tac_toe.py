import random

def initialize_board():
    return [[1 + col + row * 3 for col in range(3)] for row in range(3)]

def display_board(board):
    print("+-------+-------+-------+")
    for row in board:
        print("|       |       |       |")
        print("|   " + "   |   ".join(map(str, row)) + "   |")
        print("|       |       |       |")
        print("+-------+-------+-------+")

def get_available_moves(board):
    return [cell for row in board for cell in row if isinstance(cell, int)]


def enter_move(board):
    user_choice = int(input("What's your move?: "))
    if user_choice in get_available_moves(board):
        for row in board:
            if user_choice in row:
                row[row.index(user_choice)] = "O"
                break
    else:
         print("Invalid move. Please try again")

def computer_move(board):
    move = random.choice(get_available_moves(board))
    for row in board:
        if move in row:
            row[row.index(move)] = "X"
            break


def check_winner(board, player):
    # Check rows and columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False


# Check for a draw
def is_draw(board):
    return not get_available_moves(board)

tic_tac_toe_board = initialize_board()
tic_tac_toe_board[1][1] = "X" # Computer goes first in the middle at first
while True:
    display_board(tic_tac_toe_board)
    enter_move(tic_tac_toe_board)
    if check_winner(tic_tac_toe_board, "O"):
        display_board(tic_tac_toe_board)
        print("You have won")
        break
    elif is_draw(tic_tac_toe_board):
        display_board(tic_tac_toe_board)
        print("It's a draw")
        break
    computer_move(tic_tac_toe_board)
    if check_winner(tic_tac_toe_board, "X"):
        display_board(tic_tac_toe_board)
        print("Computer won")
        break
    elif is_draw(tic_tac_toe_board):
        display_board(tic_tac_toe_board)
        print("It's a draw")
        break
