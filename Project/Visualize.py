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

world1 = World()
world2 = World()
agent = Agent(1, 3, False)

class Visual:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1100, 600))
        pygame.display.set_caption("Visualization")

    # def grid(self):
    #     for x in range(0, TILESIZE*5, TILESIZE):
    #         pygame.draw.line(self.screen, WHITE, (x, 0), (x, TILESIZE*5))
    #     for y in range(0, TILESIZE*5, TILESIZE):
    #         pygame.draw.line(self.screen, WHITE, (0, y), (TILESIZE*5, y))

    def draw(self, world1, world2, agent):
        self.screen.fill(BLACK)
        # self.grid()
        for x in range(11):
            if x != 5:
                for y in range(5):
                    if x < 5:
                        self.drawNode(x, y, world1.map[x][y])
                    else:
                        self.drawNode(x, y, world2.map[x-6][y])
        self.drawAgentLocationLeftMap(agent)
        self.drawAgentLocationRightMap(agent)
        self.addText()
        pygame.display.flip()

    def addText(self):
        font = pygame.font.SysFont('Arial', 30)
        info = "Agent with package"
        text = font.render(info, False, WHITE)
        self.screen.blit(text, (0, 500))

        info2 = "Agent without package"
        text = font.render(info2, False, WHITE)
        self.screen.blit(text, (600, 500))

        info3 = "Operator Counter: " + "                     Agent Reward: "
        text = font.render(info3, False, WHITE)
        self.screen.blit(text, (0, 550))

    def run_visual(self, world1, world2, agent):
    # game loop - set self.playing = False to end the game
        self.running = True
        while self.running:
            pygame.time.delay(1000)
            for self.event in pygame.event.get():
                if self.event.type == pygame.QUIT:
                    self.running = False
            self.draw(world1, world2, agent)

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
        textCanvas = text.render(str(round(node.qNorth, 2)), False, BLACK)
        self.screen.blit(textCanvas, (x + (TILESIZE / 2) - (textCanvas.get_rect().width / 2), y + (TILESIZE / 10)))

        #east
        pygame.draw.polygon(self.screen, GREEN, [(x + TILESIZE, y + TILESIZE), (x + TILESIZE, y), (x + (TILESIZE / 2), y + (TILESIZE / 2))])
        pygame.draw.polygon(self.screen, WHITE, [(x + TILESIZE, y + TILESIZE), (x + TILESIZE, y), (x + (TILESIZE / 2), y + (TILESIZE / 2))], 3)
        textCanvas = text.render(str(round(node.qEast, 2)), False, BLACK)
        self.screen.blit(textCanvas, (x + ((3 * TILESIZE) / 4) - (textCanvas.get_rect().width / 2), y + (TILESIZE / 2) - (textCanvas.get_rect().height / 2)))

        #south
        pygame.draw.polygon(self.screen, GREEN, [(x + TILESIZE, y + TILESIZE), (x, y + TILESIZE), (x + (TILESIZE / 2), y + (TILESIZE / 2))])
        pygame.draw.polygon(self.screen, WHITE, [(x + TILESIZE, y + TILESIZE), (x, y + TILESIZE), (x + (TILESIZE / 2), y + (TILESIZE / 2))], 3)
        textCanvas = text.render(str(round(node.qSouth, 2)), False, BLACK)
        self.screen.blit(textCanvas, (x + (TILESIZE / 2) - (textCanvas.get_rect().width / 2), y + 75 - (textCanvas.get_rect().height / 2)))

        #west
        pygame.draw.polygon(self.screen, GREEN, [(x, y), (x, y + TILESIZE), (x + (TILESIZE / 2), y + (TILESIZE / 2))])
        pygame.draw.polygon(self.screen, WHITE, [(x, y), (x, y + TILESIZE), (x + (TILESIZE / 2), y + (TILESIZE / 2))], 3)
        textCanvas = text.render(str(round(node.qWest, 2)), False, BLACK)
        self.screen.blit(textCanvas, (x + (TILESIZE / 4) - (textCanvas.get_rect().width / 2), y + (TILESIZE / 2) - (textCanvas.get_rect().height / 2)))


    def drawAgentLocationLeftMap(self, agent):
        xPosition =  int((agent.x * TILESIZE) + (TILESIZE / 2))
        yPosition =  int((agent.y * TILESIZE) + (TILESIZE / 2))
        pygame.draw.circle(self.screen, AGENTCOLOR, (xPosition , yPosition), 10)

    def drawAgentLocationRightMap(self, agent):
        xPosition =  int((agent.x * TILESIZE) + (TILESIZE / 2))
        yPosition =  int((agent.y * TILESIZE) + (TILESIZE / 2))
        pygame.draw.circle(self.screen, AGENTCOLOR, (xPosition + 6 * TILESIZE, yPosition), 10)


# This function finds the max or min given a world, oldX and oldY. Returns highest or lowest q
    def findMax(world):
        max = 0.0;
        for i in range(4):
            for j in range(4):
                if (world.map[i][j].qNorth) > max:
                    max = world.map[i][j].qNorth
                if (world.map[i][j].qEast) > max:
                    max = world.map[i][j].qEast
                if (world.map[i][j].qSouth) > max:
                    max = world.map[i][j].qSouth
                if (world.map[i][j].qWest) > max:
                    max = world.map[i][j].qWest
        return max


    def findMin(world):
        min = 0.0;
        for i in range(5):
            for j in range(5):
                if (world.map[i][j].qNorth) < min:
                    min = world.map[i][j].qNorth
                if (world.map[i][j].qEast) < min:
                    min = world.map[i][j].qEast
                if (world.map[i][j].qSouth) < min:
                    min = world.map[i][j].qSouth
                if (world.map[i][j].qWest) < min:
                    min = world.map[i][j].qWest
        return min






