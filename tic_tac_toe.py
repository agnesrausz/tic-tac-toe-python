import os

def init_board():
    """Returns an empty 3-by-3 board (with .)."""
    board = [['.','.','.'],['.','.','.'],['.','.','.']]
    return board


def get_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    return row, col


def get_ai_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    return row, col


def mark(board, player, row, col):
    """Marks the element at row & col on the board for player."""
    pass


def has_won(board, player):
    """Returns True if player has won the game."""
    return False


def is_full(board):
    """Returns True if board is full."""
    board = init_board()
    how_many_are_empty = 0
    for i, x in enumerate(board):
        for j, a in enumerate(x):
            if "." in a:
                how_many_are_empty+=1
    if how_many_are_empty == 0:
        full = True
        print("Board is full")
    if full == True:
        print("Game over.")
        exit(0)
    


def print_board(board):
    """Prints a 3-by-3 board on the screen with borders."""
    rows=["A","B","C"]
    columns =["  ","1  ","2  ","3"]
    board = init_board()
    i = 0
    n = max(len(x) for l in board for x in l)
    print(*columns)
    for row in board:
        print(rows[i],'|'.join(x.center(n + 2) for x in row))
        print(" ","---+---+---")
        i+=1


def print_result(winner):
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    pass


def tictactoe_game(mode='HUMAN-HUMAN'):
    board = init_board()

    # use get_move(), mark(), has_won(), is_full(), and print_board() to create game logic
    print_board(board)
    row, col = get_move(board, 1)
    mark(board, 1, row, col)

    winner = 0
    print_result(winner)


def main_menu():
    width = os.get_terminal_size().columns
    clear = lambda: os.system('clear')
    print("This is the main menu.".center(width))
    print("Press 1 if you want to play against a stupid AI.".center(width))
    print("Press 2 if you want to play against another player.".center(width))
    players_choice=input("")
    while players_choice != "1" or "2": 

        if players_choice == "1":
            game_mode = "AI"
            print("Playing against an AI. Good luck. ;)")
            return(game_mode)
        if players_choice == "2":
            game_mode = "HUMAN-HUMAN"
            print("Playing against another player. Good luck. ;)")
            return(game_mode)
        else:
            clear()
            print("You trying to be sneaky, right? Well, you can't choose anything else.".center(width))
            print("")
            print("This is the main menu.".center(width))
            print("Press 1 if you want to play against a stupid AI.".center(width))
            print("Press 2 if you want to play against another player.".center(width))
            players_choice=input("")


if __name__ == '__main__':
    main_menu()
