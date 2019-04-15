# Project Experiment 1
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
    show = Visual()

    agent = Agent(0, 4, False)

    havePackageWorld = World()
    noPackageWorld = World()

    resetNumber = 0
    previousTermination = 0
    terminationSteps = 0
    terminationList = []

    for i in range(4000):
        oldAgent = copy.deepcopy(agent)
        if not agent.havePackage:
            world = noPackageWorld
            world.worldUpdate(havePackageWorld, noPackageWorld)
        else:
            world = havePackageWorld
            world.worldUpdate(noPackageWorld, havePackageWorld)

        SelectMove.PRANDOM(agent, world, False)
        newAgent = copy.deepcopy(agent)
        updateMatrix.QUpdate(oldAgent, newAgent, world, .3, .5)
        if world.isCompleteDelevery():
            noPackageWorld.mapReset()
            havePackageWorld.mapReset()
            resetNumber += 1
            print("MapReset")
            terminationSteps = agent.steps - previousTermination
            terminationList.append(terminationSteps)
            previousTermination = agent.steps

        if i == 1999:
            show.run_visual(noPackageWorld, havePackageWorld, agent, resetNumber, terminationList)
        if i == 3999:
            show.run_visual(noPackageWorld, havePackageWorld, agent, resetNumber, terminationList)

    for j in range(4000):
        oldAgent = copy.deepcopy(agent)
        if not agent.havePackage:
            world = noPackageWorld
            world.worldUpdate(havePackageWorld, noPackageWorld)
        else:
            world = havePackageWorld
            world.worldUpdate(noPackageWorld, havePackageWorld)

        SelectMove.PGREEDY(agent, world, False)
        newAgent = copy.deepcopy(agent)
        updateMatrix.QUpdate(oldAgent, newAgent, world, 0.3, .5)
        if world.isCompleteDelevery():
            noPackageWorld.mapReset()
            havePackageWorld.mapReset()
            resetNumber += 1
            print("MapReset")
            terminationSteps = agent.steps - previousTermination
            terminationList.append(terminationSteps)
            previousTermination = agent.steps

        if j == 1999:
            show.run_visual(noPackageWorld, havePackageWorld, agent, resetNumber, terminationList)
        if j == 3999:
            show.run_visual(noPackageWorld, havePackageWorld, agent, resetNumber, terminationList)

    show.run_visual(noPackageWorld, havePackageWorld, agent, resetNumber, terminationList)
    show.quit()
