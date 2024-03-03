import copy
import sys

sys.setrecursionlimit(3000)


class GameState:
    def __init__(self):
        # Board is a 8x8 2d list, each element in list has 2 characters.
        # The first character represents the color of the piece: 'b' or 'w'.
        # The second character represents the type of the piece: 'R', 'N', 'B', 'Q', 'K' or 'p'.
        # The third character represents which of the multiple pieces of the same type it is.
        # "---" represents an empty space with no piece.
        self.board = [
            ["bR1", "bN1", "bB1", "bQ", "bK", "bB2", "bN2", "bR2"],
            ["bp1", "bp2", "bp3", "bp4", "bp5", "bp6", "bp7", "bp8"],
            ["---", "---", "---", "---", "---", "---", "---", "---"],
            ["---", "---", "---", "---", "---", "---", "---", "---"],
            ["---", "---", "---", "---", "---", "---", "---", "---"],
            ["---", "---", "---", "---", "---", "---", "---", "---"],
            ["wp1", "wp2", "wp3", "wp4", "wp5", "wp6", "wp7", "wp8"],
            ["wR1", "wN1", "wB1", "wQ", "wK", "wB2", "wN2", "wR2"]]
        self.moves = []
        self.white_to_move = True

    def check_valid_moves(self, piece_selected):
        valid_moves = []  # Empty list for valid moves

        if piece_selected[1] == "R" or piece_selected[1] == "Q":  # Rook and queen valid moves
            for row_index, row in enumerate(self.board):
                for col_index, square in enumerate(row):
                    if square == piece_selected:
                        for j in range(col_index + 1, len(row)):  # Horizontal to the right
                            if row[j] == "---":  # When empty square, move gets added
                                valid_move = copy.deepcopy(self.board)
                                valid_move[row_index][row.index(piece_selected)] = "---"
                                valid_move[row_index][j] = piece_selected
                                valid_moves.append(valid_move)
                            elif row[j][0] != square[0]:  # When opponents piece, move gets added but no further moves in that direction
                                valid_move = copy.deepcopy(self.board)
                                valid_move[row_index][row.index(piece_selected)] = "---"
                                valid_move[row_index][j] = piece_selected
                                valid_moves.append(valid_move)
                                break
                            else:  # When own piece, no further moves in that direction
                                break
                        for j in range(col_index - 1, -1, -1):  # Horizontal to the left
                            if row[j] == "---":  # When empty square, move gets added
                                valid_move = copy.deepcopy(self.board)
                                valid_move[row_index][row.index(piece_selected)] = "---"
                                valid_move[row_index][j] = piece_selected
                                valid_moves.append(valid_move)
                            elif row[j][0] != square[0]:  # When opponents piece, move gets added but no further moves in that direction
                                valid_move = copy.deepcopy(self.board)
                                valid_move[row_index][row.index(piece_selected)] = "---"
                                valid_move[row_index][j] = piece_selected
                                valid_moves.append(valid_move)
                                break
                            else:  # When own piece, no further moves in that direction
                                break
                        for i in range(row_index + 1, len(self.board)):  # Vertical down
                            if self.board[i][col_index] == "---":  # When empty square, move gets added
                                valid_move = copy.deepcopy(self.board)
                                valid_move[row_index][row.index(piece_selected)] = "---"
                                valid_move[i][col_index] = piece_selected
                                valid_moves.append(valid_move)
                            elif self.board[i][col_index][0] != square[0]:  # When opponents piece, move gets added but no further moves in that direction
                                valid_move = copy.deepcopy(self.board)
                                valid_move[row_index][row.index(piece_selected)] = "---"
                                valid_move[i][col_index] = piece_selected
                                valid_moves.append(valid_move)
                                break
                            else:  # When own piece, no further moves in that direction
                                break
                        for i in range(row_index - 1, -1, -1):  # Vertical up
                            if self.board[i][col_index] == "---":  # When empty square, move gets added
                                valid_move = copy.deepcopy(self.board)
                                valid_move[row_index][row.index(piece_selected)] = "---"
                                valid_move[i][col_index] = piece_selected
                                valid_moves.append(valid_move)
                            elif self.board[i][col_index][0] != square[0]:  # When opponents piece, move gets added but no further moves in that direction
                                valid_move = copy.deepcopy(self.board)
                                valid_move[row_index][row.index(piece_selected)] = "---"
                                valid_move[i][col_index] = piece_selected
                                valid_moves.append(valid_move)
                                break
                            else:  # When own piece, no further moves in that direction
                                break

        if piece_selected[1] == "B" or piece_selected[1] == "Q":  # Bishop and queen valid moves
            for row_index, row in enumerate(self.board):
                for col_index, square in enumerate(row):
                    if square == piece_selected:
                        for i, j in zip(range(row_index - 1, -1, -1), range(col_index - 1, -1, -1)):  # Diagonal up-left
                            if self.board[i][j] == "---":  # When empty square, move gets added
                                valid_move = copy.deepcopy(self.board)
                                valid_move[row_index][row.index(piece_selected)] = "---"
                                valid_move[i][j] = piece_selected
                                valid_moves.append(valid_move)
                            elif self.board[i][j][0] != square[0]:   # When opponents piece, move gets added but no further moves in that direction
                                valid_move = copy.deepcopy(self.board)
                                valid_move[row_index][row.index(piece_selected)] = "---"
                                valid_move[i][j] = piece_selected
                                valid_moves.append(valid_move)
                                break
                            else:  # When own piece, no further moves in that direction
                                break
                        for i, j in zip(range(row_index - 1, -1, -1), range(col_index + 1, len(self.board))):  # Diagonal up-right
                            if self.board[i][j] == "---":  # When empty square, move gets added
                                valid_move = copy.deepcopy(self.board)
                                valid_move[row_index][row.index(piece_selected)] = "---"
                                valid_move[i][j] = piece_selected
                                valid_moves.append(valid_move)
                            elif self.board[i][j][0] != square[0]:  # When opponents piece, move gets added but no further moves in that direction
                                valid_move = copy.deepcopy(self.board)
                                valid_move[row_index][row.index(piece_selected)] = "---"
                                valid_move[i][j] = piece_selected
                                valid_moves.append(valid_move)
                                break
                            else:  # When own piece, no further moves in that direction
                                break
                        for i, j in zip(range(row_index + 1, len(self.board)), range(col_index - 1, -1, -1)):  # Diagonal down-left
                            if self.board[i][j] == "---":  # When empty square, move gets added
                                valid_move = copy.deepcopy(self.board)
                                valid_move[row_index][row.index(piece_selected)] = "---"
                                valid_move[i][j] = piece_selected
                                valid_moves.append(valid_move)
                            elif self.board[i][j][0] != square[0]:  # When opponents piece, move gets added but no further moves in that direction
                                valid_move = copy.deepcopy(self.board)
                                valid_move[row_index][row.index(piece_selected)] = "---"
                                valid_move[i][j] = piece_selected
                                valid_moves.append(valid_move)
                                break
                            else:  # When own piece, no further moves in that direction
                                break
                        for i, j in zip(range(row_index + 1, len(self.board)), range(col_index + 1, len(self.board))):  # Diagonal down-right
                            if self.board[i][j] == "---":  # When empty square, move gets added
                                valid_move = copy.deepcopy(self.board)
                                valid_move[row_index][row.index(piece_selected)] = "---"
                                valid_move[i][j] = piece_selected
                                valid_moves.append(valid_move)
                            elif self.board[i][j][0] != square[0]:  # When opponents piece, move gets added but no further moves in that direction
                                valid_move = copy.deepcopy(self.board)
                                valid_move[row_index][row.index(piece_selected)] = "---"
                                valid_move[i][j] = piece_selected
                                valid_moves.append(valid_move)
                                break
                            else:  # When own piece, no further moves in that direction
                                break

        if piece_selected[1] == "N":
            for row_index, row in enumerate(self.board):
                for col_index, square in enumerate(row):
                    if square == piece_selected:
                        moves = [
                            (row_index - 2, col_index - 1), (row_index - 2, col_index + 1),
                            (row_index - 1, col_index - 2), (row_index - 1, col_index + 2),
                            (row_index + 1, col_index - 2), (row_index + 1, col_index + 2),
                            (row_index + 2, col_index - 1), (row_index + 2, col_index + 1)
                        ]  # All possible knight moves

                        for move in moves:
                            new_row, new_col = move
                            if 0 <= new_row < 8 and 0 <= new_col < 8:  # Check if inside board
                                if self.board[new_row][new_col] == "---" or self.board[new_row][new_col][0] != square[0]:  # When empty square or opponents piece, move gets added
                                    valid_move = copy.deepcopy(self.board)
                                    valid_move[row_index][col_index] = "---"
                                    valid_move[new_row][new_col] = piece_selected
                                    valid_moves.append(valid_move)

        if piece_selected[1] == "K":
            for row_index, row in enumerate(self.board):
                for col_index, square in enumerate(row):
                    if square == piece_selected:
                        moves = [
                            (row_index - 1, col_index - 1), (row_index - 1, col_index), (row_index - 1, col_index + 1),
                            (row_index, col_index - 1), (row_index, col_index + 1), (row_index + 1, col_index - 1),
                            (row_index + 1, col_index), (row_index + 1, col_index + 1)
                        ]  # All possible king moves

                        for move in moves:
                            new_row, new_col = move
                            if 0 <= new_row < 8 and 0 <= new_col < 8:  # Check if inside board
                                if self.board[new_row][new_col] == "---" or self.board[new_row][new_col][0] != square[0]:   # When empty square or opponents piece, move gets added
                                    temp_board = copy.deepcopy(self.board)
                                    temp_board[row_index][col_index] = "---"
                                    temp_board[new_row][new_col] = piece_selected
                                    if not self.is_in_check(temp_board, square[0]):  # Check if king can't be taken by opponents pieces
                                        valid_moves.append(temp_board)

        if piece_selected[1] == "p":
            pass

        return valid_moves

    def is_in_check(self, board, color):
        king_position = None
        for row_index, row in enumerate(board):
            for col_index, square in enumerate(row):
                if square[0] == color and square[1] == "K":  # Find kings position
                    king_position = (row_index, col_index)
                    break
            if king_position:
                break

        opponent_color = "w" if color == "b" else "b"  # Define opponents color

        pieces_to_check = [
            piece for row in board for piece in row
            if piece[0] == opponent_color and piece[1] != "K"  # Exclude the opponent's king from the list of pieces to check
        ]

        for piece in pieces_to_check:
            valid_moves = self.check_valid_moves(piece)  # Check valid moves for every black piece
            for move in valid_moves:
                if move[king_position[0]][king_position[1]] == piece:  # When piece can take king, return True
                    return True
        return False  # When no pieces can take king, return False

