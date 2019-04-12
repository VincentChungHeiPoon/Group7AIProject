import pygame
from agent import Agent
from PDWorld import World
from PDWorld import Node

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (255, 0, 0)
LIGHTGREY = (100, 100, 100)
# This sets the tile size
TILESIZE = 100

node = Node()


class Visual:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 500))
        pygame.display.set_caption("Visualization")

    # def grid(self):
    #     for x in range(0, TILESIZE*5, TILESIZE):
    #         pygame.draw.line(self.screen, WHITE, (x, 0), (x, TILESIZE*5))
    #     for y in range(0, TILESIZE*5, TILESIZE):
    #         pygame.draw.line(self.screen, WHITE, (0, y), (TILESIZE*5, y))

    def draw(self):
        self.screen.fill(BLACK)
    #    self.grid()
        for x in range(5):
            for y in range(5):
                self.drawNode(x, y, node)
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

#fill in each squares with 4 triangle, with the q-value
    def drawNode(self, x, y, node):

        x *= 100
        y *= 100
        text = pygame.font.SysFont('Arial', 16)
        #north
        pygame.draw.polygon(self.screen, GREEN, [(x, y), (x + 100, y), ( x + 50, y + 50)])
        pygame.draw.polygon(self.screen, WHITE, [(x, y), (x + 100, y), ( x + 50, y + 50)], 3)
        textCanvas = text.render(str(node.qNorth), False, BLACK)
        self.screen.blit(textCanvas, (x + 50 - (textCanvas.get_rect().width / 2), y + 10))

        #east
        pygame.draw.polygon(self.screen, GREEN, [(x + 100, y + 100), (x + 100, y), (x + 50, y + 50)])
        pygame.draw.polygon(self.screen, WHITE, [(x + 100, y + 100), (x + 100, y), (x + 50, y + 50)], 3)
        textCanvas = text.render(str(node.qEast), False, BLACK)
        self.screen.blit(textCanvas, (x + 75 - (textCanvas.get_rect().width / 2), y + 50 - (textCanvas.get_rect().height / 2)))

        #south
        pygame.draw.polygon(self.screen, GREEN, [(x + 100, y + 100), (x, y + 100), (x + 50, y + 50)])
        pygame.draw.polygon(self.screen, WHITE, [(x + 100, y + 100), (x, y + 100), (x + 50, y + 50)], 3)
        textCanvas = text.render(str(node.qEast), False, BLACK)
        self.screen.blit(textCanvas, (x + 50 - (textCanvas.get_rect().width / 2), y + 75 - (textCanvas.get_rect().height / 2)))

        #west
        pygame.draw.polygon(self.screen, GREEN, [(x, y), (x, y + 100), (x + 50, y + 50)])
        pygame.draw.polygon(self.screen, WHITE, [(x, y), (x, y + 100), (x + 50, y + 50)], 3)
        textCanvas = text.render(str(node.qEast), False, BLACK)
        self.screen.blit(textCanvas, (x + 25 - (textCanvas.get_rect().width / 2), y + 50 - (textCanvas.get_rect().height / 2)))

        a = 123
        # textCanvas = text.render( str(node.qNorth), False, BLACK)
        # self.screen.blit(textCanvas, (x + 50, y + 10))






show = Visual()
show.run_visual()
show.quit()