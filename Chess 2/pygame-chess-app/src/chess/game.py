class Game:
    def __init__(self, board):
        self.board = board
        self.turn = 'white'
        self.history = []

    def make_move(self, start_pos, end_pos):
        piece = self.board.get_piece(start_pos)
        if piece and piece.color == self.turn:
            if piece.is_valid_move(start_pos, end_pos, self.board):
                self.history.append((start_pos, end_pos, piece))
                self.board.move_piece(start_pos, end_pos)
                self.switch_turn()
                return True
        return False

    def undo_move(self):
        if self.history:
            start_pos, end_pos, piece = self.history.pop()
            self.board.move_piece(end_pos, start_pos)
            self.turn = piece.color

    def switch_turn(self):
        self.turn = 'black' if self.turn == 'white' else 'white'

    def get_current_turn(self):
        return self.turn

    def is_game_over(self):
        # Implement game over logic (checkmate, stalemate, etc.)
        pass