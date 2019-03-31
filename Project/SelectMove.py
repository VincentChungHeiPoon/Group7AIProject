#this file contains all seelct move algorithem, PRANDOM, PEPLOID, PGREEDY
from agent import Agent
from PDWorld import World
from PDWorld import Node
import random


class SelectMove:
#path finding
#roll untill a random valid move 0,1,2,3 corrispond to north, east, south, west

#select at complete random
    def PRANDOM(agent, world):
        if(world.map[agent.x][agent.y].isPickUp and world.map[agent.x][agent.y].canPickUpBlock and agent.canPickUp()):
            world.map[agent.x][agent.y].pickUpAblock()
            agent.pickUpPackage()
            agent.score += 13
            print("Agent Picked Up Block")
        elif(world.map[agent.x][agent.y].isDropOff and world.map[agent.x][agent.y].canDropOffBlock and agent.canDropOff()):
            world.map[agent.x][agent.y].dropOffBlock()
            agent.dropOffPackage()
            agent.score += 13
            print("Agent Dropped Off Block")
        else:
            legalMove = False
            while not (legalMove):
                move = random.randint(0,3)
                if(move == 0 and agent.canMoveNorth(0)):
                    agent.moveNorth(0)
                    legalMove = True
                    print("Agent moved North")
                elif(move == 1 and agent.canMoveEast(4)):
                    agent.moveEast(4)
                    legalMove = True
                    print("Agent moved East")
                elif (move == 2 and agent.canMoveSouth(4)):
                    agent.moveSouth(4)
                    legalMove = True
                    print("Agent moved South")
                elif (move == 3 and agent.canMoveWest(0)):
                    agent.moveWest(0)
                    legalMove = True
                    print("Agent moved West")

            agent.score -= 1
            print("Agent is at x: ", agent.x, " y: ", agent.y)

#select best move at 80%, random at 20%
    # def PEPLOIT(agent, world):
    #     rand = random.randint(1,10)
    #     #at 20% change, select randomly
    #     if(rand <= 2):
    #         SelectMove.PRANDOM(agent, world)
    #     #at 80% select the best q value
    #     elif(random > 2 and rand <= 10):






#this method select the move with best q value, break tie by rolling a dice
#0,1,2,3 for North, East, South, West
    def findBestQValue(node) -> int:
        # sort all 4, compare each to highest to see if there is a tie
        value = [node.qNorth, node.qEast, node.qSouth, node.qWest]
        value.sort(reverse=True)
        #if frist 2 value is not the same, there is no tie
        if not (value[0] == value[1]):
            if(node.qNorth == value[0]):
                return 0
            elif(node.qEast == value[0]):
                return 1
            elif(node.qSouth == value[0]):
                return 2
            elif(node.qWest == value[0]):
                return 3
            # append all highest index into a list, and draw a random one
        else:
            list = []
            if (node.qNorth == value[0]):
                list.append(0)
            if (node.qEast == value[0]):
                list.append(1)
            if (node.qSouth == value[0]):
                list.append(2)
            if (node.qWest == value[0]):
                list.append(3)

            return list[random.randint(0, (len(list) - 1))]

