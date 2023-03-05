def print_board(board):
    """
    Prints the current state of the board.
    """
    print(board[0] + "|" + board[1] + "|" + board[2])
    print("-+-+-")
    print(board[3] + "|" + board[4] + "|" + board[5])
    print("-+-+-")
    print(board[6] + "|" + board[7] + "|" + board[8])

def get_move(board, player):
    """
    Asks the player for their move and returns it as an integer.
    """
    while True:
        move = input("Player " + player + ", enter your move (0-8): ")
        if not move.isdigit():
            print("Invalid input. Please enter a number between 0 and 8.")
        elif int(move) < 0 or int(move) > 8:
            print("Invalid input. Please enter a number between 0 and 8.")
        elif board[int(move)] != " ":
            print("That space is already occupied. Please choose another.")
        else:
            return int(move)

def check_win(board):
    """
    Checks if a player has won the game.
    Returns "X" if player X has won, "O" if player O has won,
    or None if no player has won yet.
    """
    for i in range(3):
        if board[i*3] == board[i*3+1] == board[i*3+2] != " ":
            return board[i*3]
        elif board[i] == board[i+3] == board[i+6] != " ":
            return board[i]
    if board[0] == board[4] == board[8] != " ":
        return board[0]
    elif board[2] == board[4] == board[6] != " ":
        return board[2]
    else:
        return None

def play_game():
    """
    Plays a game of Tic Tac Toe.
    """
    board = [" "] * 9
    current_player = "X"
    while True:
        print_board(board)
        move = get_move(board, current_player)
        board[move] = current_player
        winner = check_win(board)
        if winner is not None:
            print_board(board)
            print("Player " + winner + " wins!")
            break
        elif " " not in board:
            print_board(board)
            print("It's a tie!")
            break
        else:
            current_player = "O" if current_player == "X" else "X"

play_game()
