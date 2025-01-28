import pygame
import random
import sys
import json
from enum import Enum

# Initialize Pygame
pygame.init()


# Game States
class GameState(Enum):
    MENU = 1
    PLAYING = 2
    GAME_OVER = 3


# Constants
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 600
GRAVITY = 0.25
FLAP_STRENGTH = -7
PIPE_SPEED = 3
PIPE_SPAWN_TIME = 1500
PIPE_GAP = 150

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GRAY = (169, 169, 169)

# Set up the display
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Flappy Bird Clone')
clock = pygame.time.Clock()


class Button:
    def __init__(self, x, y, width, height, text, color, hover_color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color or self.lighten_color(color)
        self.current_color = color
        self.font = pygame.font.Font(None, 36)

    def lighten_color(self, color):
        return tuple(min(c + 30, 255) for c in color)

    def draw(self):
        mouse_pos = pygame.mouse.get_pos()
        self.current_color = self.hover_color if self.rect.collidepoint(mouse_pos) else self.color

        # Draw button with a border
        pygame.draw.rect(screen, BLACK, self.rect.inflate(4, 4))
        pygame.draw.rect(screen, self.current_color, self.rect)

        text_surface = self.font.render(self.text, True, BLACK)
        text_rect = text_surface.get_rect(center=self.rect.center)
        screen.blit(text_surface, text_rect)

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)


class Bird:
    def __init__(self):
        self.reset()
        self.flap_sound = pygame.mixer.Sound('flap.wav') if self.load_sound('flap.wav') else None

    def load_sound(self, filename):
        try:
            return pygame.mixer.Sound(filename)
        except:
            return None

    def reset(self):
        self.x = WINDOW_WIDTH // 3
        self.y = WINDOW_HEIGHT // 2
        self.velocity = 0
        self.size = 20
        self.rotation = 0

    def flap(self):
        self.velocity = FLAP_STRENGTH
        if self.flap_sound:
            self.flap_sound.play()

    def update(self):
        self.velocity += GRAVITY
        self.y += self.velocity

        # Update rotation based on velocity
        self.rotation = max(-30, min(self.velocity * 2, 90))

        if self.y < 0:
            self.y = 0
            self.velocity = 0
        elif self.y > WINDOW_HEIGHT - self.size:
            self.y = WINDOW_HEIGHT - self.size
            self.velocity = 0

    def draw(self):
        # Draw bird with rotation
        surface = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        pygame.draw.rect(surface, BLUE, (0, 0, self.size, self.size))
        rotated = pygame.transform.rotate(surface, -self.rotation)
        screen.blit(rotated, (self.x - rotated.get_width() / 2 + self.size / 2,
                              self.y - rotated.get_height() / 2 + self.size / 2))


class Pipe:
    def __init__(self):
        self.gap_y = random.randint(150, WINDOW_HEIGHT - 150)
        self.x = WINDOW_WIDTH
        self.width = 50
        self.scored = False

    def update(self):
        self.x -= PIPE_SPEED

    def draw(self):
        # Draw pipes with a border
        border_color = (0, 100, 0)  # Darker green for border

        # Top pipe
        pygame.draw.rect(screen, border_color,
                         (self.x - 2, 0, self.width + 4, self.gap_y - PIPE_GAP // 2))
        pygame.draw.rect(screen, GREEN,
                         (self.x, 0, self.width, self.gap_y - PIPE_GAP // 2))

        # Bottom pipe
        pygame.draw.rect(screen, border_color,
                         (self.x - 2, self.gap_y + PIPE_GAP // 2,
                          self.width + 4, WINDOW_HEIGHT - (self.gap_y + PIPE_GAP // 2)))
        pygame.draw.rect(screen, GREEN,
                         (self.x, self.gap_y + PIPE_GAP // 2,
                          self.width, WINDOW_HEIGHT - (self.gap_y + PIPE_GAP // 2)))


class Game:
    def __init__(self):
        self.bird = Bird()
        self.reset_game()
        self.state = GameState.MENU
        self.font = pygame.font.Font(None, 36)
        self.title_font = pygame.font.Font(None, 48)
        self.high_score = self.load_high_score()

        # Create buttons
        button_width = WINDOW_WIDTH // 2
        button_height = 50
        button_x = WINDOW_WIDTH // 4

        self.start_button = Button(button_x, WINDOW_HEIGHT // 2,
                                   button_width, button_height, "Start Game", GREEN)
        self.quit_button = Button(button_x, WINDOW_HEIGHT // 2 + 70,
                                  button_width, button_height, "Exit Game", RED)
        self.retry_button = Button(button_x, WINDOW_HEIGHT // 2,
                                   button_width, button_height, "Play Again", GREEN)
        self.exit_button = Button(button_x, WINDOW_HEIGHT // 2 + 70,
                                  button_width, button_height, "Exit", RED)

        # Load sounds
        self.point_sound = pygame.mixer.Sound('point.wav') if self.load_sound('point.wav') else None
        self.hit_sound = pygame.mixer.Sound('hit.wav') if self.load_sound('hit.wav') else None

    def load_sound(self, filename):
        try:
            return pygame.mixer.Sound(filename)
        except:
            return None

    def reset_game(self):
        self.pipes = []
        self.score = 0
        self.last_pipe = pygame.time.get_ticks()
        self.bird.reset()

    def load_high_score(self):
        try:
            with open('high_score.json', 'r') as f:
                return json.load(f)['high_score']
        except:
            return 0

    def save_high_score(self):
        with open('high_score.json', 'w') as f:
            json.dump({'high_score': self.high_score}, f)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                if self.state == GameState.MENU:
                    if self.start_button.is_clicked(mouse_pos):
                        self.state = GameState.PLAYING
                    elif self.quit_button.is_clicked(mouse_pos):
                        pygame.quit()
                        sys.exit()

                elif self.state == GameState.GAME_OVER:
                    if self.retry_button.is_clicked(mouse_pos):
                        self.reset_game()
                        self.state = GameState.PLAYING
                    elif self.exit_button.is_clicked(mouse_pos):
                        pygame.quit()
                        sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and self.state == GameState.PLAYING:
                    self.bird.flap()
                elif event.key == pygame.K_ESCAPE:
                    if self.state == GameState.PLAYING:
                        self.state = GameState.MENU

    def update(self):
        if self.state == GameState.PLAYING:
            self.bird.update()

            now = pygame.time.get_ticks()
            if now - self.last_pipe > PIPE_SPAWN_TIME:
                self.pipes.append(Pipe())
                self.last_pipe = now

            for pipe in self.pipes[:]:
                pipe.update()

                if not pipe.scored and pipe.x + pipe.width < self.bird.x:
                    self.score += 1
                    if self.point_sound:
                        self.point_sound.play()
                    if self.score > self.high_score:
                        self.high_score = self.score
                        self.save_high_score()
                    pipe.scored = True

                if pipe.x + pipe.width < 0:
                    self.pipes.remove(pipe)

                bird_rect = pygame.Rect(self.bird.x, self.bird.y,
                                        self.bird.size, self.bird.size)
                top_pipe = pygame.Rect(pipe.x, 0, pipe.width,
                                       pipe.gap_y - PIPE_GAP // 2)
                bottom_pipe = pygame.Rect(pipe.x, pipe.gap_y + PIPE_GAP // 2,
                                          pipe.width,
                                          WINDOW_HEIGHT - (pipe.gap_y + PIPE_GAP // 2))

                if bird_rect.colliderect(top_pipe) or bird_rect.colliderect(bottom_pipe):
                    if self.hit_sound:
                        self.hit_sound.play()
                    self.state = GameState.GAME_OVER

    def draw_menu(self):
        screen.fill(WHITE)

        # Draw title with shadow
        title = self.title_font.render("Flappy Bird Clone", True, BLACK)
        title_shadow = self.title_font.render("Flappy Bird Clone", True, GRAY)
        title_rect = title.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 4))
        screen.blit(title_shadow, title_rect.move(2, 2))
        screen.blit(title, title_rect)

        # Draw high score
        high_score_text = self.font.render(f"High Score: {self.high_score}", True, BLACK)
        high_score_rect = high_score_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 3))
        screen.blit(high_score_text, high_score_rect)

        # Draw instructions
        inst_text = self.font.render("Press SPACE to flap", True, BLACK)
        inst_rect = inst_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 3 + 40))
        screen.blit(inst_text, inst_rect)

        self.start_button.draw()
        self.quit_button.draw()

    def draw_game(self):
        screen.fill(WHITE)

        for pipe in self.pipes:
            pipe.draw()

        self.bird.draw()

        score_text = self.font.render(f'Score: {self.score}', True, BLACK)
        screen.blit(score_text, (10, 10))

        # Draw high score during gameplay
        high_score_text = self.font.render(f'Best: {self.high_score}', True, BLACK)
        screen.blit(high_score_text, (10, 40))

    def draw_game_over(self):
        screen.fill(WHITE)

        # Draw "Game Over" with shadow effect
        game_over_text = self.title_font.render("Game Over!", True, RED)
        game_over_shadow = self.title_font.render("Game Over!", True, GRAY)
        game_over_rect = game_over_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 4))
        screen.blit(game_over_shadow, game_over_rect.move(2, 2))
        screen.blit(game_over_text, game_over_rect)

        score_text = self.font.render(f"Score: {self.score}", True, BLACK)
        score_rect = score_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 3))
        screen.blit(score_text, score_rect)

        high_score_text = self.font.render(f"High Score: {self.high_score}", True, BLACK)
        high_score_rect = high_score_text.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2.5))
        screen.blit(high_score_text, high_score_rect)

        # Draw retry and exit buttons
        self.retry_button.draw()
        self.exit_button.draw()

    def draw(self):
        if self.state == GameState.MENU:
            self.draw_menu()
        elif self.state == GameState.PLAYING:
            self.draw_game()
        elif self.state == GameState.GAME_OVER:
            self.draw_game_over()

        pygame.display.flip()


def main():
    game = Game()

    while True:
        game.handle_events()
        game.update()
        game.draw()
        clock.tick(60)


if __name__ == "__main__":
    main()