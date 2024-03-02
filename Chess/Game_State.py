import copy


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

        return valid_moves
