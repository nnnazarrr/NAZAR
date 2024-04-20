import pygame
import random

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
GRID_SIZE = 20
INITIAL_SPEED = 10

WHITE = (255, 255, 255)
PINK = (231, 129, 235)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

class Snake:
    def __init__(self):
        self.body = [(100, 100)]
        self.direction = (1, 0)
        self.speed = INITIAL_SPEED   
        self.food_position = self.generate_food_position()
        self.score = 0
        self.level = 1

    def move(self):
        head = (self.body[0][0] + self.direction[0] * GRID_SIZE, self.body[0][1] + self.direction[1] * GRID_SIZE)
        # Wrap around the screen edges
        head = (head[0] % SCREEN_WIDTH, head[1] % SCREEN_HEIGHT)
        # Check for self collision
        if head in self.body[1:]:
            return True  # Game over
        self.body.insert(0, head)
        if head == self.food_position:
            self.score += 1
            if self.score % 3 == 0:
                self.level += 1
                self.speed += 1  # Increase speed
            self.food_position = self.generate_food_position()
        else:
            self.body.pop()
        return False

    def change_direction(self, direction):
        if (direction[0] * -1, direction[1] * -1) != self.direction:
            self.direction = direction

    def generate_food_position(self):
        while True:
            x = random.randrange(0, SCREEN_WIDTH, GRID_SIZE)
            y = random.randrange(0, SCREEN_HEIGHT, GRID_SIZE)
            if (x, y) not in self.body:
                return (x, y)
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Snake")
        self.clock = pygame.time.Clock()
        self.snake = Snake()

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.snake.change_direction((0, -1))
                    elif event.key == pygame.K_DOWN:
                        self.snake.change_direction((0, 1))
                    elif event.key == pygame.K_LEFT:
                        self.snake.change_direction((-1, 0))
                    elif event.key == pygame.K_RIGHT:
                        self.snake.change_direction((1, 0))

            self.screen.fill(WHITE)
            game_over = self.snake.move()
            if game_over:
                running = False
            self.draw_snake()
            self.draw_food()
            self.draw_score_and_level()
            pygame.display.flip()
            self.clock.tick(self.snake.speed)
        pygame.quit()

    def draw_snake(self):
        for segment in self.snake.body:
            pygame.draw.rect(self.screen, GREEN, (segment[0], segment[1], GRID_SIZE, GRID_SIZE))

    def draw_food(self):
        pygame.draw.rect(self.screen,  PINK, (self.snake.food_position[0], self.snake.food_position[1], GRID_SIZE, GRID_SIZE))

    def draw_score_and_level(self):
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"Score: {self.snake.score}", True, BLACK)
        level_text = font.render(f"Level: {self.snake.level}", True, BLACK)
        self.screen.blit(score_text, (10, 10))
        self.screen.blit(level_text, (10, 40))

if __name__ == "__main__":
    game = Game()
    game.run()