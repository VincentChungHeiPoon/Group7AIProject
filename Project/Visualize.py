import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
LIGHTGREY = (100, 100, 100)
# This sets the tile size
TILESIZE = 100


class Visual:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 500))
        pygame.display.set_caption("Visualization")

    def grid(self):
        for x in range(0, TILESIZE*5, TILESIZE):
            pygame.draw.line(self.screen, WHITE, (x, 0), (x, TILESIZE*5))
        for y in range(0, TILESIZE*5, TILESIZE):
            pygame.draw.line(self.screen, WHITE, (0, y), (TILESIZE*5, y))

    def draw(self):
        self.screen.fill(BLACK)
        self.grid()
        pygame.display.flip()

    def run_visual(self):
    # game loop - set self.playing = False to end the game
        self.running = True
        while self.running:
            pygame.time.delay(1000)
            for self.event in pygame.event.get():
                if self.event.type == pygame.QUIT:
                    self.running = False
            self.draw()

    def quit(self):
        pygame.quit()
