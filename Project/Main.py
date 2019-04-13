#this file is mainly for testing purpose
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

agent = Agent(4, 0, False)
oldAgent1 = copy.deepcopy(agent)
old2Agent = copy.deepcopy(agent)

havePackageWorld = World()
noPackageWorld = World()

for i in range(100):

    oldAgent2 = copy.deepcopy(oldAgent1)
    oldAgent1 = copy.deepcopy(agent)

    if not (agent.havePackage):
        world = noPackageWorld
        world.worldUpdate(havePackageWorld, noPackageWorld)
    else:
        world = havePackageWorld
        world.worldUpdate(noPackageWorld, havePackageWorld)

    SelectMove.PRANDOM(agent, world, False)
    newAgent = copy.deepcopy(agent)


    if(i >= 1):
        updateMatrix.SARSAUpdate(oldAgent2, oldAgent1, newAgent, world, .3, 1)

show = Visual()
show.run_visual(noPackageWorld, havePackageWorld, agent)
show.quit()


#update score after every move

#SelectMove.PEPLOIT(agent, world, printMove= False)

#SelectMove.PRANDOM(agent, world, printMove= False)

#SelectMove.PGREEDY(agent, world, printMove= False)