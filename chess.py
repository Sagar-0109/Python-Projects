import pygame
import chess
# import chess.engine

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
SQUARE_SIZE = WIDTH // 8
WHITE = (238, 238, 210)
BLACK = (118, 150, 86)

# Load images
PIECE_IMAGES = {}
for piece in ['p', 'r', 'n', 'b', 'q', 'k', 'P', 'R', 'N', 'B', 'Q', 'K']:
    PIECE_IMAGES[piece] = pygame.transform.scale(
        pygame.image.load(f'images/{piece}.jpg'), (SQUARE_SIZE, SQUARE_SIZE))

# Initialize board
board = chess.Board()

# Set up display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Chess")

# Draw board
def draw_board():
    for row in range(8):
        for col in range(8):
            color = WHITE if (row + col) % 2 == 0 else BLACK
            pygame.draw.rect(screen, color, (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

# Draw pieces
def draw_pieces():
    board_str = str(board).split("\n")
    for row in range(8):
        for col in range(8):
            piece = board_str[row][col]
            if piece != '.':
                screen.blit(PIECE_IMAGES[piece], (col * SQUARE_SIZE, row * SQUARE_SIZE))

# Main game loop
running = True
while running:
    draw_board()
    draw_pieces()
    pygame.display.flip()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
