#if you have a class you created, use the syntax from "file" import "class"
#aware that file do not have .py extension anymore
from agent import Agent
from PDWorld import World
from PDWorld import Node
import random
from SelectMove import SelectMove
from Storing import updateMatrix
import copy
import pygame
from Visualize import Visual

#2d 5x5 grid
agent = Agent(0,1,False)

#2 tables for agent is, is not carrying a package
havePackageWorld = World()
noPackageWorld = World()

# havePackageWorld.map[2][3].qWest = -2
#
# show = Visual()
# show.run_visual(noPackageWorld, havePackageWorld, agent)
# show.quit()

agent = Agent(0, 4, False)
oldAgent = copy.deepcopy(agent)
old2Agent = copy.deepcopy(agent)
havePackageWorld = World()
noPackageWorld = World()

for i in range(2000):

    if not (agent.havePackage):
        world = noPackageWorld
    else:
        world = havePackageWorld

    oldAgent2 = copy.deepcopy(oldAgent)
    oldAgent = copy.deepcopy(agent)

    SelectMove.PRANDOM(agent, world, True)
    newAgent = copy.deepcopy(agent)


    # if(i > 2):
    #     updateMatrix.SARSAUpdate(oldAgent2, oldAgent1, newAgent, world, .3, 1)

show = Visual()
show.run_visual(noPackageWorld, havePackageWorld, agent)
show.quit()

#update score after every move

#SelectMove.PEPLOIT(agent, world, printMove= False)

#SelectMove.PRANDOM(agent, world, printMove= False)

#SelectMove.PGREEDY(agent, world, printMove= False)

# print("Agent is at x: ", agent.x, " y: ", agent.y)