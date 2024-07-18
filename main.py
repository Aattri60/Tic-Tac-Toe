import random

def display_board(board):
    print("+-------+-------+-------+")
    for row in board:
        print("|       |       |       |")
        print(f"|   {row[0]}   |   {row[1]}   |   {row[2]}   |")
        print("|       |       |       |")
        print("+-------+-------+-------+")

def enter_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if move < 1 or move > 9:
                print("Invalid move! Choose a number between 1 and 9.")
                continue
            row, col = divmod(move - 1, 3)
            if board[row][col] in ['X', 'O']:
                print("Square already occupied! Choose another move.")
            else:
                board[row][col] = 'O'
                break
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 9.")

def make_list_of_free_fields(board):
    free_fields = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['X', 'O']:
                free_fields.append((row, col))
    return free_fields

def victory_for(board, sign):
    # Check rows
    for row in board:
        if all([cell == sign for cell in row]):
            return True

    # Check columns
    for col in range(3):
        if all([board[row][col] == sign for row in range(3)]):
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == sign:
        return True
    if board[0][2] == board[1][1] == board[2][0] == sign:
        return True

    return False

def draw_move(board):
    free_fields = make_list_of_free_fields(board)
    if free_fields:
        row, col = random.choice(free_fields)
        board[row][col] = 'X'

def play_game():
    board = [[str(i + j * 3 + 1) for i in range(3)] for j in range(3)]
    print("Welcome to Tic-Tac-Toe!")
    print("You are 'O' and the computer is 'X'.")
    display_board(board)

    while True:
        enter_move(board)
        display_board(board)

        if victory_for(board, 'O'):
            print("Congratulations! You won!")
            break
        elif victory_for(board, 'X'):
            print("Sorry, the computer won!")
            break
        elif len(make_list_of_free_fields(board)) == 0:
            print("It's a tie!")
            break

        draw_move(board)
        display_board(board)

        if victory_for(board, 'O'):
            print("Congratulations! You won!")
            break
        elif victory_for(board, 'X'):
            print("Sorry, the computer won!")
            break
        elif len(make_list_of_free_fields(board)) == 0:
            print("It's a tie!")
            break

if __name__ == "__main__":
    play_game()
