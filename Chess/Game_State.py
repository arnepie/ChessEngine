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
