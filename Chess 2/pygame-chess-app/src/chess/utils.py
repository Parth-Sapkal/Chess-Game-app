def load_image(file_path):
    """Load an image from the specified file path."""
    try:
        image = pygame.image.load(file_path)
        return image.convert_alpha()  # Use convert_alpha for transparency
    except pygame.error as e:
        print(f"Error loading image: {file_path} - {e}")
        return None

def check_valid_move(start_pos, end_pos, board):
    """Check if a move from start_pos to end_pos is valid."""
    # Implement logic to check if the move is valid based on the piece and board state
    pass

def handle_game_state_transition(current_state, action):
    """Handle transitions between different game states."""
    # Implement logic to transition between game states (e.g., from playing to game over)
    pass

def undo_move(move_history):
    """Undo the last move in the move history."""
    if move_history:
        return move_history.pop()  # Remove and return the last move
    return None