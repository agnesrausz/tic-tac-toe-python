import os
import random

def init_board():
    """Returns an empty 3-by-3 board (with .)."""
    board = []
    for _ in range(3):
        board.append(['.'] * 3)
    return board


def get_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    first_letter_ascii_code = ord('a')
    row_len = len(board)
    col_len = len(board[0])

    while True:
        move = get_user_input(f'Player {player}, enter your move (example: B2): ').strip().lower()

        if len(move) != 2:
            print('Invalid coordinate, try again!')
            continue

        if not move[0].isalpha() or not move[1].isdigit():
            print('Invalid coordinate, try again!')
            continue

        row = ord(move[0]) - first_letter_ascii_code
        col = int(move[1]) - 1

        if not (0 <= row < row_len and 0 <= col < col_len):
            print('That move is out of bounds, try again!')
            continue

        if board[row][col] != '.':
            print('That square is already taken, try again!')
            continue

        return row, col


def get_ai_move(board, player):
    """Returns the coordinates of a valid move for player on board."""
    if is_full(board):
        return None

    winning_move = None
    for row in range(3):
        for col in range(3):
            if board[row][col] == '.':
                board[row][col] = player
                if has_won(board, player):
                    winning_move = (row, col)
                board[row][col] = '.'
    if winning_move:
        return winning_move

    counter_move = None
    for row in range(3):
        for col in range(3):
            if board[row][col] == '.':
                enemy = 'O' if player == 'X' else 'X'
                board[row][col] = enemy
                if has_won(board, enemy):
                    counter_move = (row, col)
                board[row][col] = '.'
    if counter_move:
        return counter_move

    free_coordinates = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == '.':
                free_coordinates.append((row, col))
    if free_coordinates:
        return random.choice(free_coordinates)
    return None


def mark(board, player, row, col):
    """Marks the element at row & col on the board for player."""
    if 0 <= row < len(board) and 0 <= col < len(board[0]) and board[row][col] == '.':
        board[row][col] = player
    return board


def has_won(board, player):
    """Returns True if player has won the game."""
    win_cases = [
        # Horizontal
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        # Vertical
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        # Diagonal
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
    ]
    for case in win_cases:
        all_cells_match = True
        for row, col in case:
            if board[row][col] != player:
                all_cells_match = False
                break
        if all_cells_match:
            return True
    return False


def is_full(board):
    """Returns True if board is full."""
    return all(cell != '.' for row in board for cell in row)


def print_board(board):
    """Prints a 3-by-3 board on the screen with borders."""
    clear()
    for col in range(len(board[0])):
        print('   ' + str(col + 1), end='')
    print()
    for row in range(len(board)):
        row_str = chr(ord('A') + row) + '  '
        for col in range(len(board[0])):
            row_str += board[row][col]
            if col < len(board[0]) - 1:
                row_str += ' | '
        print(row_str)
        if row < len(board) - 1:
            print('  ' + '---+---+---')


def print_result(winner):
    """Congratulates winner or proclaims tie (if winner equals zero)."""
    match winner:
        case 'X':
            print("X has won!")
        case 'O':
            print("O has won!")
        case 0:
            print("It's a tie!")
        case 'you':
            print("You have won!")
        case 'ai':
            print("AI has won!")
        case _:
            raise ValueError("Invalid winner value")


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_user_input(prompt):
    while True:
        user_input = input(prompt)
        normalized_user_input = user_input.strip().lower()
        if normalized_user_input in ('q', 'quit', 'exit'):
            print("Exiting the game. Goodbye!")
            exit()
        return user_input


def tictactoe_game(mode='HUMAN-HUMAN'):
    board = init_board()

    # use get_move(), mark(), has_won(), is_full(), and print_board() to create game logic
    winner = 0
    player = 'X'
    if mode == 'HUMAN-AI':
        ai_player = 'O'
    elif mode == 'AI-HUMAN':
        ai_player = 'X'
    else:
        ai_player = None

    while True:
        print_board(board)
        if mode in ['HUMAN-AI', 'AI-HUMAN'] and player == ai_player:
            row, col = get_ai_move(board, player)
        else:
            row, col = get_move(board, player)
        mark(board, player, row, col)
        if has_won(board, player):
            winner = player
            break
        if is_full(board):
            break
        player = 'O' if player == 'X' else 'X'

    print_board(board)
    if mode in ['HUMAN-AI', 'AI-HUMAN'] and winner != 0:
        if winner == ai_player:
            winner = 'ai'
        else:
            winner = 'you'
    print_result(winner)


def main_menu():
    while True:
        print("Welcome to Tic-Tac-Toe!")
        print("1. Human vs Human")
        print("2. Human vs AI")
        print("3. AI vs Human")
        choice = get_user_input("Select an option (1, 2 or 3): ").strip()
        if choice == '1':
            tictactoe_game('HUMAN-HUMAN')
        elif choice == '2':
            tictactoe_game('HUMAN-AI')
        elif choice == '3':
            tictactoe_game('AI-HUMAN')
        else:
            print("Invalid choice, please try again.")


if __name__ == '__main__':
    main_menu()
