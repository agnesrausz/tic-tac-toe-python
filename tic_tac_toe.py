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
        move = input('Enter your move (example: B2): ').strip().lower()

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
    row, col = 0, 0
    return row, col


def mark(board, player, row, col):
    """Marks the element at row & col on the board for player."""
    if 0 <= row < len(board) and 0 <= col < len(board[0]) and board[row][col] == '.':
        board[row][col] = player
    return board


def has_won(board, player):
    """Returns True if player has won the game."""
    return False


def is_full(board):
    """Returns True if board is full."""
    return False


def print_board(board):
    """Prints a 3-by-3 board on the screen with borders."""
    pass


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
    tictactoe_game('HUMAN-HUMAN')


if __name__ == '__main__':
    main_menu()
