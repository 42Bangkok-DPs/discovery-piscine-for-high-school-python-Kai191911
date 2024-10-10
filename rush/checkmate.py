#!/usr/bin/env python3


def checkmate(board: str):
    board = [list(row) for row in board.splitlines()]
    directions = {
        'rook': [(0, 1), (0, -1), (1, 0), (-1, 0)],
        'bishop': [(1, 1), (-1, -1), (1, -1), (-1, 1)],
        'queen': [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (1, -1), (-1, 1)],
        'pawn': [(1, -1), (1, 1)]
    }

    def find_king(board):
        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c] == 'K': return r, c
        return None

    def is_in_check(kr, kc):
        for piece, dirs in directions.items():
            for dr, dc in dirs:
                r, c = kr + dr, kc + dc
                while 0 <= r < len(board) and 0 <= c < len(board):
                    if board[r][c] != '.':
                        if (board[r][c] == 'P' and piece == 'pawn') or board[r][c] in ('R', 'B', 'Q') and board[r][c][0] == piece[0].upper():
                            return True
                        break
                    r, c = r + dr, c + dc
        return False

    king_pos = find_king(board)
    if king_pos and is_in_check(*king_pos):
        print("Success")
    else:
        print("Fail")

# Ex 1
board1 = """\
R...
.K..
..P.
...."""
checkmate(board1)

# Ex 2
board2 = """\
..
.K"""
checkmate(board2)