import os
import random
import time

def init_board():
    """Returns an empty 3-by-3 board (with .)."""
    board = [['.','.','.'],['.','.','.'],['.','.','.']]
    return board


def get_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    row, col = 0, 0
    boardcoord = []
    boardrange = (("A1", "A2", "A3"), ("B1", "B2", "B3"), ("C1", "C2", "C3"))
    inboardrange = ("A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3")
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != ".":
                boardcoord.append(boardrange[i][j])
    
    playercoord = (input("What is your next move?\n")).upper()
    while True:
        if not len(str(playercoord)) == 2:
            playercoord = (input("It's not valid coordinate. Add another coordinate!\n")).upper()
        elif playercoord in boardcoord:
            playercoord = (input("It's taken. Add another coordinate!\n")).upper()
        elif not playercoord in inboardrange:
            playercoord = (input("Out of range. Add another coordinate!\n")).upper()
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
    board[row][col] = player


def has_won(board, player):
    """Returns True if player has won the game."""
    playercoord = []
    boardrange = (("A1", "A2", "A3"), ("B1", "B2", "B3"), ("C1", "C2", "C3"))
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == player:
                playercoord.append(boardrange[i][j])
    if ("A1"in playercoord and "A2"in playercoord and "A3"in playercoord) or ("B1" in playercoord and "B2" in playercoord and "B3"in playercoord) or ("C1" in playercoord and "C2"in playercoord and "C3"in playercoord) or ("A1" in playercoord and "B1" in playercoord and "C1"in playercoord) or ("A2"in playercoord and "B2"in playercoord and "C2"in playercoord) or ("A3"in playercoord and "B3"in playercoord and "C3"in playercoord) or ("A1"in playercoord and "B2"in playercoord and "C3"in playercoord) or ("A3"in playercoord and "B2"in playercoord and "C1"in playercoord):
        return True
    else:
        return False


def is_full(board):
    """Returns True if board is full."""
    how_many_are_not_empty = 0
    for boardrow in board:
        for coord in boardrow:
            if not "." in coord:
                how_many_are_not_empty+=1
    if how_many_are_not_empty == 9:
        return True
    else:
        return False


def print_board(board):
    """Prints a 3-by-3 board on the screen with borders."""
    rows=["A","B","C"]
    columns =["  ","1  ","2  ","3"]
    i = 0
    n = max(len(x) for l in board for x in l)
    print(*columns)
    for row in board:
        print(rows[i],'|'.join(x.center(n + 2) for x in row))
        print(" ","---+---+---")
        i+=1


def print_result(winner):
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    if winner == "X":
        print("Congratulations! X has won!\n")
    elif winner == "0":
        print("Congratulations! 0 has won!\n")
    else:
        print("What a turn of events! It's a tie!")

# use get_move(), mark(), has_won(), is_full(), and print_board() to create game logic
def tictactoe_game(mode='HUMAN-HUMAN'):
    if mode == 'HUMAN-HUMAN':
        board = init_board()
        player = "0"
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            if player == "0":
                player = "X"
            else:
                player = "0"
            print_board(board)
            print(player + "'s turn")
            row, col = get_move(board, player)
            mark(board, player, row, col)
            if has_won(board,player):
                os.system('cls' if os.name == 'nt' else 'clear')
                print_result(player)
                break
            if is_full(board):
                os.system('cls' if os.name == 'nt' else 'clear')
                print_result("")
                break
        print_board(board)
        time.sleep(1.65)
    else:
        board = init_board()
        player = "0"
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            if player == "0":
                player = "X"
            else:
                player = "0"
            print_board(board)
            if player == "X":
                print(player + "'s turn")
                row, col = get_move(board, player)
                mark(board, player, row, col)
            else:
                print("AI's turn.")
                print("AI is thinking...hard.")
                time.sleep(1.65)
                row, col = get_ai_move(board,player)
                mark(board,player,row,col)
            if has_won(board,player):
                os.system('cls' if os.name == 'nt' else 'clear')
                print_result(player)
                break
            if is_full(board):
                os.system('cls' if os.name == 'nt' else 'clear')
                print_result("")
                break
        print_board(board)
        time.sleep(1.65)


def main_menu():

    while True:
        print("\n","T I C - T A C - T O E\n MAIN MENU:\n 1.PLAYER VS PLAYER\n 2.PLAYER VS AI\n 3.EXIT\n")
        userchoice = input("Please choose an option!\n")
        if userchoice == "1":
            tictactoe_game('HUMAN-HUMAN')
        elif userchoice == "2":
            tictactoe_game('AI-HUMAN')
        elif userchoice =="3":
            print("Goodbye!")
            exit()
        else:
            print("I feel like you can't count to 3...\n")

if __name__ == '__main__':
    main_menu()
