import pygame

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
BALL_SPEED = 5
PADDLE_SPEED = 10

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong Game")

# Fonts
font = pygame.font.Font(None, 50)

# Paddle class
class Paddle:
    def __init__(self, x):
        self.rect = pygame.Rect(x, HEIGHT // 2 - 50, 10, 100)

    def move(self, up=True):
        if up and self.rect.top > 0:
            self.rect.y -= PADDLE_SPEED
        elif not up and self.rect.bottom < HEIGHT:
            self.rect.y += PADDLE_SPEED

    def draw(self):
        pygame.draw.rect(screen, WHITE, self.rect)

# Ball class
class Ball:
    def __init__(self):
        self.rect = pygame.Rect(WIDTH // 2 - 10, HEIGHT // 2 - 10, 20, 20)
        self.dx = BALL_SPEED
        self.dy = BALL_SPEED

    def move(self):
        self.rect.x += self.dx
        self.rect.y += self.dy

        # Bounce off top and bottom
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.dy = -self.dy

    def reset(self):
        self.rect.x, self.rect.y = WIDTH // 2 - 10, HEIGHT // 2 - 10
        self.dx *= -1  # Change direction

    def draw(self):
        pygame.draw.ellipse(screen, WHITE, self.rect)

# Game class
class Game:
    def __init__(self):
        self.paddle_left = Paddle(20)
        self.paddle_right = Paddle(WIDTH - 30)
        self.ball = Ball()
        self.score_left = 0
        self.score_right = 0

    def handle_collision(self):
        # Ball hitting paddles
        if self.ball.rect.colliderect(self.paddle_left.rect) or self.ball.rect.colliderect(self.paddle_right.rect):
            self.ball.dx = -self.ball.dx

        # Ball goes out of bounds
        if self.ball.rect.left <= 0:
            self.score_right += 1
            self.ball.reset()
        elif self.ball.rect.right >= WIDTH:
            self.score_left += 1
            self.ball.reset()

    def draw_score(self):
        left_text = font.render(str(self.score_left), True, WHITE)
        right_text = font.render(str(self.score_right), True, WHITE)
        screen.blit(left_text, (WIDTH // 4, 20))
        screen.blit(right_text, (WIDTH * 3 // 4, 20))

    def check_winner(self):
        if self.score_left >= 5:
            return "Player 1 Wins!"
        if self.score_right >= 5:
            return "Player 2 Wins!"
        return None

    def run(self):
        running = True
        clock = pygame.time.Clock()

        while running:
            screen.fill(BLACK)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Player controls
            keys = pygame.key.get_pressed()
            if keys[pygame.K_w]:
                self.paddle_left.move(up=True)
            if keys[pygame.K_s]:
                self.paddle_left.move(up=False)
            if keys[pygame.K_UP]:
                self.paddle_right.move(up=True)
            if keys[pygame.K_DOWN]:
                self.paddle_right.move(up=False)

            # Move ball
            self.ball.move()
            self.handle_collision()

            # Draw everything
            self.paddle_left.draw()
            self.paddle_right.draw()
            self.ball.draw()
            self.draw_score()

            # Check for winner
            winner = self.check_winner()
            if winner:
                win_text = font.render(winner, True, WHITE)
                screen.blit(win_text, (WIDTH // 2 - 100, HEIGHT // 2))
                pygame.display.flip()
                pygame.time.delay(2000)
                running = False

            pygame.display.flip()
            clock.tick(60)

        pygame.quit()

# Run the game
if __name__ == "__main__":
    Game().run()
