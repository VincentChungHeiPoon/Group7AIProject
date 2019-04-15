# Project Experiment 2
from agent import Agent
from PDWorld import World
from PDWorld import Node
import random
from SelectMove import SelectMove
from Storing import updateMatrix
import copy
import pygame
from Visualize import Visual


class E2:
    agent = Agent(0, 4, False)
    havePackageWorld = World()
    noPackageWorld = World()

    resetNumber = 0
    previousTermination = 0
    terminationSteps = 0
    terminationList = []

    show = Visual()

    for i in range(200):
        oldAgent = copy.deepcopy(agent)
        if not agent.havePackage:
            world = noPackageWorld
            world.worldUpdate(havePackageWorld, noPackageWorld)
        else:
            world = havePackageWorld
            world.worldUpdate(noPackageWorld, havePackageWorld)

        SelectMove.PRANDOM(agent, world, False)
        newAgent = copy.deepcopy(agent)
        updateMatrix.QUpdate(oldAgent, newAgent, world, 0.3, 0.5)
        if world.isCompleteDelevery():
            noPackageWorld.mapReset()
            havePackageWorld.mapReset()
            resetNumber += 1
            print("MapReset")
            terminationSteps = agent.steps - previousTermination
            terminationList.append(terminationSteps)
            previousTermination = agent.steps

    # Show progress after PRANDOM
    show.run_visual(noPackageWorld, havePackageWorld, agent, resetNumber, terminationList)

    # Show progress at fixed intervals
    for i in range(7800):
        oldAgent = copy.deepcopy(agent)
        if not agent.havePackage:
            world = noPackageWorld
            world.worldUpdate(havePackageWorld, noPackageWorld)
        else:
            world = havePackageWorld
            world.worldUpdate(noPackageWorld, havePackageWorld)

        SelectMove.PEPLOIT(agent, world, False)
        newAgent = copy.deepcopy(agent)
        updateMatrix.QUpdate(oldAgent, newAgent, world, 0.3, 0.5)
        if i == 1799:
            show.run_visual(noPackageWorld, havePackageWorld, agent, resetNumber, terminationList)
        elif i == 3799:
            show.run_visual(noPackageWorld, havePackageWorld, agent, resetNumber, terminationList)
        elif i == 5799:
            show.run_visual(noPackageWorld, havePackageWorld, agent, resetNumber, terminationList)
        elif i == 7799:
            show.run_visual(noPackageWorld, havePackageWorld, agent, resetNumber, terminationList)
        if world.isCompleteDelevery():
            noPackageWorld.mapReset()
            havePackageWorld.mapReset()
            resetNumber += 1
            print("MapReset")
            terminationSteps = agent.steps - previousTermination
            terminationList.append(terminationSteps)
            previousTermination = agent.steps

    show.run_visual(noPackageWorld, havePackageWorld, agent, resetNumber, terminationList)
    show.quit()

    # update score after every move
    # SelectMove.PEXPLOIT(agent, world, printMove= False)
    # SelectMove.PRANDOM(agent, world, printMove= False)
    # SelectMove.PGREEDY(agent, world, printMove= False)
    # print("Agent is at x: ", agent.x, " y: ", agent.y)
