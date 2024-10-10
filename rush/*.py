class ChessBoard:
    def __init__(self):
        # Initialize an 8x8 board
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.setup_pieces()

    def setup_pieces(self):
       
        self.board[0] = ['R', 'N', 'B', 'K', 'Q', 'B', 'N', 'R']  #Black
        self.board[1] = ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P']

        self.board[6] = ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p']  #White
        self.board[7] = ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']

    def display(self):
       
        print("  a b c d e f g h")
        print(" +-----------------+")
        for i, row in enumerate(self.board):
            row_display = ' '.join(piece if piece else '.' for piece in row)
            print(f"{8 - i}| {row_display} |")
        print(" +-----------------+")

def main():
    chess_board = ChessBoard()
    chess_board.display()

if __name__ == "__main__":
    main()
class Piece:
    def __init__(self, color, name):
        self.color = color
        self.name = name

    def valid_moves(self, position, board):
        return []

class Pawn(Piece):
    def valid_moves(self, position, board):
        row, col = position
        direction = -1 if self.color == 'white' else 1
        moves = [(row + direction, col)]

        if (self.color == 'white' and row == 6) or (self.color == 'black' and row == 1):
            moves.append((row + 2 * direction, col))

        # Capture diagonally
        capture_moves = [(row + direction, col - 1), (row + direction, col + 1)]
        moves.extend([move for move in capture_moves if 0 <= move[0] < 8 and 0 <= move[1] < 8 and board[move[0]][move[1]] is not None and board[move[0]][move[1]].color != self.color])

        return [(r, c) for r, c in moves if 0 <= r < 8 and 0 <= c < 8]

class Rook(Piece):
    def valid_moves(self, position, board):
        return self.linear_moves(position, board)

    def linear_moves(self, position, board):
        moves = []
        for direction in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            for step in range(1, 8):
                new_row = position[0] + step * direction[0]
                new_col = position[1] + step * direction[1]
                if 0 <= new_row < 8 and 0 <= new_col < 8:
                    if board[new_row][new_col] is None:
                        moves.append((new_row, new_col))
                    else:
                        if board[new_row][new_col].color != self.color:
                            moves.append((new_row, new_col))
                        break
                else:
                    break
        return moves

class Knight(Piece):
    def valid_moves(self, position, board):
        moves = []
        row, col = position
        knight_moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
        for dr, dc in knight_moves:
            new_row, new_col = row + dr, col + dc
            if 0 <= new_row < 8 and 0 <= new_col < 8:
                if board[new_row][new_col] is None or board[new_row][new_col].color != self.color:
                    moves.append((new_row, new_col))
        return moves

class Bishop(Piece):
    def valid_moves(self, position, board):
        return self.linear_moves(position, board)

    def linear_moves(self, position, board):
        moves = []
        for direction in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
            for step in range(1, 8):
                new_row = position[0] + step * direction[0]
                new_col = position[1] + step * direction[1]
                if 0 <= new_row < 8 and 0 <= new_col < 8:
                    if board[new_row][new_col] is None:
                        moves.append((new_row, new_col))
                    else:
                        if board[new_row][new_col].color != self.color:
                            moves.append((new_row, new_col))
                        break
                else:
                    break
        return moves

class Queen(Piece):
    def valid_moves(self, position, board):
        return Rook(self.color, self.name).linear_moves(position, board) + Bishop(self.color, self.name).linear_moves(position, board)

class King(Piece):
    def valid_moves(self, position, board):
        moves = []
        row, col = position
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < 8 and 0 <= new_col < 8:
                    if board[new_row][new_col] is None or board[new_row][new_col].color != self.color:
                        moves.append((new_row, new_col))
        return moves

class Board:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.setup_pieces()
        self.current_turn = 'white'

    def setup_pieces(self):
        self.board[0] = [Rook('black', 'R'), Knight('black', 'N'), Bishop('black', 'B'),  King('black', 'K'), Queen('black', 'Q') ,Bishop('black', 'B'), Knight('black', 'N'), Rook('black', 'R')]
        self.board[1] = [Pawn('black', 'P') for _ in range(8)]
        self.board[6] = [Pawn('white', 'P') for _ in range(8)]
        self.board[7] = [Rook('white', 'R'), Knight('white', 'N'), Bishop('white', 'B'), Queen('white', 'Q'), King('white', 'K'), Bishop('white', 'B'), Knight('white', 'N'), Rook('white', 'R')]

    def display(self):
        print("   a b c d e f g h")
        print(" +-----------------+")
        for i, row in enumerate(self.board):
            row_display = ' '.join([piece.name if piece and piece.color == 'black' else piece.name.lower() if piece else '.' for piece in row])
            print(f"{8 - i}| {row_display} |")
        print(" +-----------------+")

    def get_piece(self, position):
        row, col = position
        return self.board[row][col]

    def move_piece(self, start, end):
        start_piece = self.get_piece(start)
        if start_piece and start_piece.color == self.current_turn and end in start_piece.valid_moves(start, self.board):
            if self.get_piece(end) is not None:
                print(f"Captured {self.get_piece(end).name}.")
            self.board[end[0]][end[1]] = start_piece
            self.board[start[0]][start[1]] = None
            self.current_turn = 'black' if self.current_turn == 'white' else 'white'
            return True
        return False

class Player:
    def __init__(self, name, color):
        self.name = name
        self.color = color

def main():
    player_white = Player("White Player", "white")
    player_black = Player("Black Player", "black")
    board = Board()
    board.display()

    while True:
        current_player = player_white if board.current_turn == 'white' else player_black
        print(f"{current_player.name}'s turn")
        move = input("Enter your move (e.g., e2 e4) or 'exit' to quit: ")
        if move.lower() == 'exit':
            break

        try:
            start, end = move.split()
            start_row, start_col = 8 - int(start[1]), ord(start[0]) - ord('a')
            end_row, end_col = 8 - int(end[1]), ord(end[0]) - ord('a')
            if board.move_piece((start_row, start_col), (end_row, end_col)):
                board.display()
            else:
                print("Invalid move!")
        except (ValueError, IndexError):
            print("Invalid input format! Please use 'e2 e4'.")

if __name__ == "__main__":
    main()


