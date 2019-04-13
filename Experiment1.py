from agent import Agent
from PDWorld import World
from PDWorld import Node
import random
from SelectMove import SelectMove
from Storing import updateMatrix
import copy
import pygame
from Visualize import Visual
class E1:


    agent = Agent(0, 4, False)

    havePackageWorld = World()
    noPackageWorld = World()

    for i in range(4000):
        oldAgent = copy.deepcopy(agent)
        if not (agent.havePackage):
            world = noPackageWorld
        else:
            world = havePackageWorld

        SelectMove.PRANDOM(agent, world, False)
        newAgent = copy.deepcopy(agent)
        updateMatrix.QUpdate(oldAgent, newAgent, world, .3, .5)


    for j in range(4000):
        oldAgent = copy.deepcopy(agent)
        if not (agent.havePackage):
            world = noPackageWorld
        else:
            world = havePackageWorld

        SelectMove.PGREEDY(agent, world, False)
        newAgent = copy.deepcopy(agent)
        updateMatrix.QUpdate(oldAgent, newAgent, world, 0.3, .5)



    show = Visual()
    show.run_visual(noPackageWorld, havePackageWorld, agent)
    show.quit()

