#Project Experiment 5
from agent import Agent
from PDWorld import World
from PDWorld import Node
from SelectMove import SelectMove
from Storing import updateMatrix
from Visualize import Visual
import pygame
import copy
import random

class E5:
# Create agent in starting location with no package
    agent = Agent(4, 0, False)

# Create two worlds for when agent has/has no package
    havePackageWorld = World()
    noPackageWorld = World()

# Used to visualize grids
    show = Visual()

    resetNumber = 0
# Run 200 operations with PRANDOM with a = 0.3, g = 0.5
    for i in range(200):
        oldAgent = copy.deepcopy(agent)
        if not (agent.havePackage):
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

# Show grids for PRANDOM
    show.run_visual(noPackageWorld, havePackageWorld, agent, resetNumber)

# Run 7800 operations of PEXPLOIT
# When the agent reaches a terminal state the 2nd time, swap pickup/drop off locations
    terminalCounter = 0
    for i in range(7800):
        oldAgent = copy.deepcopy(agent)
        if not (agent.havePackage):
            world = noPackageWorld
            world.worldUpdate(havePackageWorld, noPackageWorld)
        else:
            world = havePackageWorld
            world.worldUpdate(noPackageWorld, havePackageWorld)
        SelectMove.PEPLOIT(agent, world, False)
        newAgent = copy.deepcopy(agent)
        updateMatrix.QUpdate(oldAgent, newAgent, world, 0.3, 0.5)

        if world.isCompleteDelevery():
            print("MapReset")
            resetNumber += 1
            # pickup/dropoff are reset like normal for the first terminal state
            if terminalCounter == 0:
                noPackageWorld.mapReset()
                havePackageWorld.mapReset()
                terminalCounter += 1
            # pickup/dropoff are swapped on the second terminal state
            elif terminalCounter == 1:
                # swap on each map
                noPackageWorld.invertPickUpDropOff()
                havePackageWorld.invertPickUpDropOff()
                terminalCounter += 1
            # continue resetting packages with the swapped positions
            elif terminalCounter == 2:
                noPackageWorld.mapReset()
                havePackageWorld.mapReset()
                print("MapReset")

        if (i == 1799 or i == 3799 or i == 5799):
            show.run_visual(noPackageWorld, havePackageWorld, agent, resetNumber)
            print("terminalCounter: " + str(terminalCounter))


# Print data
    print("terminalCounter: " + str(terminalCounter))

# Show grids for PEXPOLIT
    show.run_visual(noPackageWorld, havePackageWorld, agent, resetNumber)
