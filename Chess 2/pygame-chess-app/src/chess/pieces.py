class Piece:
    def __init__(self, color):
        self.color = color

    def valid_moves(self, board):
        raise NotImplementedError("This method should be overridden by subclasses")


class Pawn(Piece):
    def valid_moves(self, board):
        # Implement pawn movement logic
        pass


class Rook(Piece):
    def valid_moves(self, board):
        # Implement rook movement logic
        pass


class Knight(Piece):
    def valid_moves(self, board):
        # Implement knight movement logic
        pass


class Bishop(Piece):
    def valid_moves(self, board):
        # Implement bishop movement logic
        pass


class Queen(Piece):
    def valid_moves(self, board):
        # Implement queen movement logic
        pass


class King(Piece):
    def valid_moves(self, board):
        # Implement king movement logic
        pass