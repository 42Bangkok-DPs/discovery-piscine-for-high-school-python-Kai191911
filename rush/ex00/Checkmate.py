#!/usr/bin/env python3

import examples

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
                while 0 <= r < len(board) and 0 <= c < len(board[0]):
                    if board[r][c] != '.':
                        if (piece == 'pawn' and board[r][c] == 'P' and dr == 1):  # Simplified pawn check
                            return True
                        elif (board[r][c] == 'R' and piece == 'rook') or \
                             (board[r][c] == 'B' and piece == 'bishop') or \
                             (board[r][c] == 'Q' and piece == 'queen'):
                            return True
                        break
                    r, c = r + dr, c + dc
        return False

    king_pos = find_king(board)
    if king_pos and is_in_check(*king_pos):
        print("Success")
    else:
        print("Fail")

print("Example 1:")
checkmate(examples.get_example1())

print("Example 2:")
checkmate(examples.get_example2())
