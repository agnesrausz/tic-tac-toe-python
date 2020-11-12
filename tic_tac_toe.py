import os
import random

player = ("x", "o")
def init_board():
    """Returns an empty 3-by-3 board (with .)."""
    board = [['.','.','.'],['.','.','.'],['.','.','.']]
    return board


def get_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    boardcoord = []
    boardrange = ("A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3")
    boardcoordnum = []
    coordcounter = 0
    for boardrow in board:
        for coord in boardrow:
            coordcounter +=1
            if coord != ".":
                boardcoordnum.append(coordcounter)
    if 1 in boardcoordnum:
        boardcoord.append("A1")
    if 2 in boardcoordnum:
        boardcoord.append("A2")
    if 3 in boardcoordnum:
        boardcoord.append("A3")
    if 4 in boardcoordnum:
        boardcoord.append("B1")
    if 5 in boardcoordnum:
        boardcoord.append("B2")
    if 6 in boardcoordnum:
        boardcoord.append("B3")
    if 7 in boardcoordnum:
        boardcoord.append("C1")    
    if 8 in boardcoordnum:
        boardcoord.append("C2")
    if 9 in boardcoordnum:
        boardcoord.append("C3")
    
    playercoord = (input("Add coordinate!")).upper()
    while True:
        if not len(str(playercoord)) == 2:
            playercoord = (input("I'ts not valid coordinate. Add another coordinate!")).upper()
        elif playercoord in boardcoord:
            playercoord = (input("I'ts taken. Add another coordinate!")).upper()
        elif not playercoord in boardrange:
            playercoord = (input("Out of range. Add another coordinate!")).upper()
        else:
            break        
    if playercoord[0] == "A":
        row = 0
    elif playercoord[0] == "B":
        row = 1
    elif playercoord[0] == "C":
        row = 2
    if playercoord[1] == "1":
        col = 0
    elif playercoord[1] == "2":
        col = 1
    elif playercoord[1] == "3":
        col =2
    return row, col

def get_ai_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    if is_full(board) == True: 
        return None
    boardcoord = []
    boardrange = (("A1", "A2", "A3"), ("B1", "B2", "B3"), ("C1", "C2", "C3"))
    inboardrange = ("A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3")
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != ".":
                boardcoord.append(boardrange[i][j])
    while True:
        aicoord = random.choice(inboardrange)
        if not aicoord in boardcoord:
            break
    if aicoord[0] == "A":
        row = 0
    elif aicoord[0] == "B":
        row = 1
    elif aicoord[0] == "C":
        row = 2
    if aicoord[1] == "1":
        col = 0
    elif aicoord[1] == "2":
        col = 1
    elif aicoord[1] == "3":
        col =2
    return row, col

def mark(board, player, row, col):
    """Marks the element at row & col on the board for player."""
    board = init_board()
    for i, x in enumerate(board):
        for j, a in enumerate(x):
            if "." in a:
                board[i][j] = a.replace(".","player")

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
        return full
    if full == True:
        print("Game over.")
        exit(0)
        return full
    

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
