# Project Experiment 4
from agent import Agent
from PDWorld import World
from SelectMove import SelectMove
from Storing import updateMatrix
import copy
import pygame
from Visualize import Visual


class E4:
    agent = Agent(0, 4, False)
    oldAgent1 = copy.deepcopy(agent)
    oldAgent2 = copy.deepcopy(agent)
    havePackageWorld = World()
    noPackageWorld = World()
    show = Visual()

    resetNumber = 0
    previousTermination = 0
    terminationSteps = 0
    terminationList = []

    for i in range(200):
        oldAgent2 = copy.deepcopy(oldAgent1)
        oldAgent1 = copy.deepcopy(agent)
        if not agent.havePackage:
            world = noPackageWorld
            world.worldUpdate(havePackageWorld, noPackageWorld)
        else:
            world = havePackageWorld
            world.worldUpdate(noPackageWorld, havePackageWorld)

        SelectMove.PRANDOM(agent, world, False)
        newAgent = copy.deepcopy(agent)
        if i >= 1:
            if not oldAgent2.havePackage:
                updateMatrix.SARSAUpdate(oldAgent2, oldAgent1, newAgent, noPackageWorld, .3, 1)
            elif oldAgent2.havePackage:
                updateMatrix.SARSAUpdate(oldAgent2, oldAgent1, newAgent, havePackageWorld, .3, 1)

        if world.isCompleteDelevery():
            noPackageWorld.mapReset()
            havePackageWorld.mapReset()
            resetNumber += 1
            print("Map Reset")
            terminationSteps = agent.steps - previousTermination
            terminationList.append(terminationSteps)
            previousTermination = agent.steps

    show.run_visual(noPackageWorld, havePackageWorld, agent, resetNumber, terminationList)

    for j in range(7800):
        oldAgent2 = copy.deepcopy(oldAgent1)
        oldAgent1 = copy.deepcopy(agent)
        if not agent.havePackage:
            world = noPackageWorld
            world.worldUpdate(havePackageWorld, noPackageWorld)
        else:
            world = havePackageWorld
            world.worldUpdate(noPackageWorld, havePackageWorld)

        SelectMove.PEPLOIT(agent, world, False)
        newAgent = copy.deepcopy(agent)
        if j >= 1:
            if not oldAgent2.havePackage:
                updateMatrix.SARSAUpdate(oldAgent2, oldAgent1, newAgent, noPackageWorld, .3, 1)
            elif oldAgent2.havePackage:

                updateMatrix.SARSAUpdate(oldAgent2, oldAgent1, newAgent, havePackageWorld, .3, 1)
        if world.isCompleteDelevery():
            noPackageWorld.mapReset()
            havePackageWorld.mapReset()
            resetNumber += 1
            print("Map Reset")
            terminationSteps = agent.steps - previousTermination
            terminationList.append(terminationSteps)
            previousTermination = agent.steps

        if j == 1799 or j == 3799 or j == 5799:
            show.run_visual(noPackageWorld, havePackageWorld, agent, resetNumber, terminationList)

    show.run_visual(noPackageWorld, havePackageWorld, agent, resetNumber, terminationList)
    show.quit()
