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
    if all(cell != '.' for row in board for cell in row):
        return True
    return False


def print_board(board):
    """Prints a 3-by-3 board on the screen with borders."""
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
        case '0':
            print("0 has won!")
        case 0:
            print("It's a tie!")
        case _:
            raise ValueError("Invalid winner value")


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
