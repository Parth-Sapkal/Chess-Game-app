import pygame
from chess.board import Board
from chess.game import Game
from ui.renderer import Renderer

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Chess Game")
    
    clock = pygame.time.Clock()
    board = Board()
    game = Game(board)
    renderer = Renderer(screen, board)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            game.handle_event(event)

        game.update()
        renderer.render()
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()