import pygame
from agent import Agent
from PDWorld import World
from PDWorld import Node

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
LIGHTGREY = (100, 100, 100)
AGENTCOLOR = (20, 180, 200)
# This sets the tile size
TILESIZE = 100

world = World()
agent = Agent(4, 4, False)

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

    def draw(self, world):
        self.screen.fill(BLACK)
        # self.grid()
        for x in range(5):
            for y in range(5):
                self.drawNode(x, y, world.map[x][y])
        self.drawAgentLocation(agent)
        pygame.display.flip()

    def run_visual(self):
    # game loop - set self.playing = False to end the game
        self.running = True
        while self.running:
            pygame.time.delay(1000)
            for self.event in pygame.event.get():
                if self.event.type == pygame.QUIT:
                    self.running = False
            self.draw(world)

    def quit(self):
        pygame.quit()

#fill in each squares with 4 triangle, with the q-value
    def drawNode(self, x, y, node):

        x *= 100
        y *= 100
        text = pygame.font.SysFont('Arial', 16)
        #north
        pygame.draw.polygon(self.screen, GREEN, [(x, y), (x + TILESIZE, y), ( x + (TILESIZE / 2), y + (TILESIZE / 2))])
        pygame.draw.polygon(self.screen, WHITE, [(x, y), (x + TILESIZE, y), ( x + (TILESIZE / 2), y + (TILESIZE / 2))], 3)
        textCanvas = text.render(str(round(node.qNorth)), False, BLACK)
        self.screen.blit(textCanvas, (x + (TILESIZE / 2) - (textCanvas.get_rect().width / 2), y + (TILESIZE / 10)))

        #east
        pygame.draw.polygon(self.screen, GREEN, [(x + TILESIZE, y + TILESIZE), (x + TILESIZE, y), (x + (TILESIZE / 2), y + (TILESIZE / 2))])
        pygame.draw.polygon(self.screen, WHITE, [(x + TILESIZE, y + TILESIZE), (x + TILESIZE, y), (x + (TILESIZE / 2), y + (TILESIZE / 2))], 3)
        textCanvas = text.render(str(round(node.qEast)), False, BLACK)
        self.screen.blit(textCanvas, (x + ((3 * TILESIZE) / 4) - (textCanvas.get_rect().width / 2), y + (TILESIZE / 2) - (textCanvas.get_rect().height / 2)))

        #south
        pygame.draw.polygon(self.screen, GREEN, [(x + TILESIZE, y + TILESIZE), (x, y + TILESIZE), (x + (TILESIZE / 2), y + (TILESIZE / 2))])
        pygame.draw.polygon(self.screen, WHITE, [(x + TILESIZE, y + TILESIZE), (x, y + TILESIZE), (x + (TILESIZE / 2), y + (TILESIZE / 2))], 3)
        textCanvas = text.render(str(round(node.qSouth)), False, BLACK)
        self.screen.blit(textCanvas, (x + (TILESIZE / 2) - (textCanvas.get_rect().width / 2), y + 75 - (textCanvas.get_rect().height / 2)))

        #west
        pygame.draw.polygon(self.screen, GREEN, [(x, y), (x, y + TILESIZE), (x + (TILESIZE / 2), y + (TILESIZE / 2))])
        pygame.draw.polygon(self.screen, WHITE, [(x, y), (x, y + TILESIZE), (x + (TILESIZE / 2), y + (TILESIZE / 2))], 3)
        textCanvas = text.render(str(round(node.qWest)), False, BLACK)
        self.screen.blit(textCanvas, (x + (TILESIZE / 4) - (textCanvas.get_rect().width / 2), y + (TILESIZE / 2) - (textCanvas.get_rect().height / 2)))


    def drawAgentLocation(self, agent):
        xPosition =  int((agent.x * TILESIZE) + (TILESIZE / 2))
        yPosition =  int((agent.y * TILESIZE) + (TILESIZE / 2))
        pygame.draw.circle(self.screen, AGENTCOLOR, (xPosition , yPosition), 10)






show = Visual()
show.run_visual()
show.quit()