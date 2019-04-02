#QMatrix/SARSA updates and storing written by Logan F.
from agent import Agent
from PDWorld import World
from PDWorld import Node
import random
from SelectMove import SelectMove


class updateMatrix:

    def moveDirection(oldAgent, newAgent) -> int:
        # 0,1,2,3,4 for North, East, South, West, stayput(pickup/dropoff)
        # if stayput
        if (newAgent.x == oldAgent.x and newAgent.y == oldAgent.y):
            return 4
        # moved north
        elif (newAgent.y < oldAgent.y and newAgent.x == oldAgent.x):
            return 0
        # moved East
        elif (newAgent.x > oldAgent.x and newAgent.y == oldAgent.y):
            return 1
        # moved south
        elif (newAgent.y > oldAgent.y and newAgent.x == oldAgent.x):
            return 2
        # moved West
        elif (newAgent.x < oldAgent.x and newAgent.y == oldAgent.y):
            return 3


    #Updating using Q-Learing
    def QUpdate(agentOld, agentCurr, world, alpha, gamma):
        reward = agentCurr.score - agentOld.score

        oldX = agentOld.x
        oldY = agentOld.y
        newX = agentCurr.x
        newY = agentCurr.y

        nextBestQ = max(world.map[newX][newY].qNorth, world.map[newX][newY].qEast, world.map[newX][newY].qSouth, world.map[newX][newY].qEast)

        movement = updateMatrix.moveDirection(agentOld, agentCurr)
        if(movement == 0):
            #We have moved north
            world.map[oldX][oldY].qNorth = (1-alpha)*(world.map[oldX][oldY].qNorth) + (alpha)*(reward + (gamma)*nextBestQ)
        elif(movement == 1):
            # We have moved east
            world.map[oldX][oldY].qEast = (1 - alpha) * (world.map[oldX][oldY].qEast) + (alpha) * (reward + (gamma) * nextBestQ)
        elif (movement == 2):
            # We have moved east
            world.map[oldX][oldY].qSouth = (1 - alpha) * (world.map[oldX][oldY].qSouth) + (alpha) * (reward + (gamma) * nextBestQ)
        elif (movement == 3):
            # We have moved east
            world.map[oldX][oldY].qWest = (1 - alpha) * (world.map[oldX][oldY].qWest) + (alpha) * (reward + (gamma) * nextBestQ)
        elif (movement == 4):
            #update all direction as 1 state
            world.map[oldX][oldY].qNorth = (1 - alpha) * (world.map[oldX][oldY].qNorth) + (alpha) * (reward + (gamma) * nextBestQ)
            world.map[oldX][oldY].qEast = (1 - alpha) * (world.map[oldX][oldY].qEast) + (alpha) * (reward + (gamma) * nextBestQ)
            world.map[oldX][oldY].qSouth = (1 - alpha) * (world.map[oldX][oldY].qSouth) + (alpha) * (reward + (gamma) * nextBestQ)
            world.map[oldX][oldY].qWest = (1 - alpha) * (world.map[oldX][oldY].qWest) + (alpha) * (reward + (gamma) * nextBestQ)









