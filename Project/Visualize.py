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

#world 1 is world with no packagr, world 2 is with package
    def draw(self, world1, world2, agent):
        self.screen.fill(BLACK)
        w1Maxq = self.findMax(world1)
        w1Minq = self.findMin(world1)

        w2Maxq = self.findMax(world2)
        w2Minq = self.findMin(world2)

        print(w1Maxq)
        print(w1Minq)

        print(w2Maxq)
        print(w2Minq)
        # self.grid()
        for x in range(11):
            if x != 5:
                for y in range(5):
                    if x < 5:
                        self.drawNode(x, y, world1.map[x][y], w1Maxq, w1Minq)
                    else:
                        self.drawNode(x, y, world2.map[x-6][y], w2Maxq, w2Minq)
        self.drawAgentLocationLeftMap(agent)
        self.drawAgentLocationRightMap(agent)
        self.addText(agent)
        pygame.display.flip()

    def addText(self, agent):
        font = pygame.font.SysFont('Arial', 30)
        info = "Agent without package"
        text = font.render(info, False, WHITE)
        self.screen.blit(text, (0, 500))

        info2 = "Agent with package"
        text = font.render(info2, False, WHITE)
        self.screen.blit(text, (600, 500))

        info3 = "Operator Counter: " + str(agent.steps) + "                   Agent Reward: " + str(agent.score)
        text = font.render(info3, False, WHITE)
        self.screen.blit(text, (0, 550))

    #function to determine color gradient based on max and min q values
    def getGradient(self, maxq, minq, currq):
        g = 0
        r = 0
        #error prevention features
        smaxq = maxq
        sminq = minq
        if maxq == 0:
            smaxq = 1
        if minq == 0:
            sminq = 1
        if currq > maxq or currq < minq:
            return (0,0,255)
            
        if currq >= 0:
            scale = currq/smaxq
            g = scale*255
        else:
            scale = currq/sminq
            r = scale*255
        return (r,g,0)
    
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
    def drawNode(self, x, y, node, maxq, minq):

        x *= 100
        y *= 100
        text = pygame.font.SysFont('Arial', 16)


        #north
        color = self.getGradient(maxq, minq, node.qNorth)
        pygame.draw.polygon(self.screen, color, [(x, y), (x + TILESIZE, y), ( x + (TILESIZE / 2), y + (TILESIZE / 2))])
        pygame.draw.polygon(self.screen, WHITE, [(x, y), (x + TILESIZE, y), ( x + (TILESIZE / 2), y + (TILESIZE / 2))], 3)
        textCanvas = text.render(str(round(node.qNorth, 2)), False, BLACK)
        self.screen.blit(textCanvas, (x + (TILESIZE / 2) - (textCanvas.get_rect().width / 2), y + (TILESIZE / 10)))

        #east
        color = self.getGradient(maxq, minq, node.qEast)
        pygame.draw.polygon(self.screen, color, [(x + TILESIZE, y + TILESIZE), (x + TILESIZE, y), (x + (TILESIZE / 2), y + (TILESIZE / 2))])
        pygame.draw.polygon(self.screen, WHITE, [(x + TILESIZE, y + TILESIZE), (x + TILESIZE, y), (x + (TILESIZE / 2), y + (TILESIZE / 2))], 3)
        textCanvas = text.render(str(round(node.qEast, 2)), False, BLACK)
        self.screen.blit(textCanvas, (x + ((3 * TILESIZE) / 4) - (textCanvas.get_rect().width / 2), y + (TILESIZE / 2) - (textCanvas.get_rect().height / 2)))

        #south
        color = self.getGradient(maxq, minq, node.qSouth)
        pygame.draw.polygon(self.screen, color, [(x + TILESIZE, y + TILESIZE), (x, y + TILESIZE), (x + (TILESIZE / 2), y + (TILESIZE / 2))])
        pygame.draw.polygon(self.screen, WHITE, [(x + TILESIZE, y + TILESIZE), (x, y + TILESIZE), (x + (TILESIZE / 2), y + (TILESIZE / 2))], 3)
        textCanvas = text.render(str(round(node.qSouth, 2)), False, BLACK)
        self.screen.blit(textCanvas, (x + (TILESIZE / 2) - (textCanvas.get_rect().width / 2), y + 75 - (textCanvas.get_rect().height / 2)))

        #west
        color = self.getGradient(maxq, minq, node.qWest)
        pygame.draw.polygon(self.screen, color, [(x, y), (x, y + TILESIZE), (x + (TILESIZE / 2), y + (TILESIZE / 2))])
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
    def findMax(self, world):
        max = 0.0;
        for i in range(5):
            for j in range(5):
                if (world.map[i][j].qNorth) > max:
                    max = world.map[i][j].qNorth
                if (world.map[i][j].qEast) > max:
                    max = world.map[i][j].qEast
                if (world.map[i][j].qSouth) > max:
                    max = world.map[i][j].qSouth
                if (world.map[i][j].qWest) > max:
                    max = world.map[i][j].qWest
        return max


    def findMin(self, world):
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






