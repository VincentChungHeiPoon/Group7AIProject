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
agent = Agent(0,4,False)

#2 tables for agent is, is not carrying a package
havePackageWorld = World()
noPackageWorld = World()

# havePackageWorld.map[2][3].qWest = -2
#
# show = Visual()
# show.run_visual(noPackageWorld, havePackageWorld, agent)
# show.quit()

for i in range(1000):
    oldAgent = copy.deepcopy(agent)
    #swap in worlds depends on agent's carrying a package or not
    if not (agent.havePackage):
       world = noPackageWorld
    else:
        world = havePackageWorld

    SelectMove.PRANDOM(agent, world, False)

    newAgent = copy.deepcopy(agent)

    updateMatrix.QUpdate(oldAgent, newAgent, world, 0.5, 1)

print(agent.steps)
show = Visual()
show.run_visual(noPackageWorld, havePackageWorld, agent)
show.quit()

#update score after every move

#SelectMove.PEPLOIT(agent, world, printMove= False)

#SelectMove.PRANDOM(agent, world, printMove= False)

#SelectMove.PGREEDY(agent, world, printMove= False)

# print("Agent is at x: ", agent.x, " y: ", agent.y)