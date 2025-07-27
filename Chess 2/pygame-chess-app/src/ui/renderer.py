import pygame

class Renderer:
    def __init__(self, screen, board):
        self.screen = screen
        self.board = board
        self.square_size = 80  # Size of each square on the chessboard
        self.colors = [pygame.Color(255, 255, 255), pygame.Color(0, 0, 0)]  # White and Black

    def draw_board(self):
        for row in range(8):
            for col in range(8):
                color = self.colors[(row + col) % 2]
                pygame.draw.rect(self.screen, color, (col * self.square_size, row * self.square_size, self.square_size, self.square_size))

    def draw_pieces(self):
        for piece in self.board.pieces:
            if piece is not None:
                self.screen.blit(piece.image, (piece.col * self.square_size, piece.row * self.square_size))

    def render(self):
        self.draw_board()
        self.draw_pieces()
        pygame.display.flip()  # Update the full display Surface to the screen

    def clear(self):
        self.screen.fill((0, 0, 0))  # Clear the screen with black before redrawing