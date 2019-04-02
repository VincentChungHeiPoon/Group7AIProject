#if you have a class you created, use the syntax from "file" import "class"
#aware that file do not have .py extension anymore
from agent import Agent
from PDWorld import World
from PDWorld import Node
import random
from SelectMove import SelectMove

#2d 5x5 grid
agent = Agent(0,0,False)

#2 tables for agent is, is not carrying a package
havePackageWorld = World()
noPackageWorld = World()
#Temporory world that is currently being updated
world = World()

havePackageWorld.map[agent.x][agent.y].qEast = 1

world = havePackageWorld

world.printWorld()
#update score after every move

#SelectMove.PEPLOIT(agent, world, printMove= False)

#SelectMove.PRANDOM(agent, world, printMove= False)

#SelectMove.PGREEDY(agent, world, printMove= False)

# print("Agent is at x: ", agent.x, " y: ", agent.y)