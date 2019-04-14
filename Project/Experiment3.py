from agent import Agent
from PDWorld import World
from SelectMove import SelectMove
from Storing import updateMatrix
import copy
from Visualize import Visual
class E3:


    # Run the SARSA algorithm for 200 steps with policy PRANDOM, then run 7200 steps with policy PEXPLOIT

    show = Visual()

    agent = Agent(0, 4, False)
    oldAgent1 = copy.deepcopy(agent)

    havePackageWorld = World()
    noPackageWorld = World()

    for i in range(200):
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

        if (i >= 1):
            if not (oldAgent2.havePackage):
                updateMatrix.SARSAUpdate(oldAgent2, oldAgent1, newAgent, noPackageWorld, .3, .5)
            elif (oldAgent2.havePackage):
                updateMatrix.SARSAUpdate(oldAgent2, oldAgent1, newAgent, havePackageWorld, .3, .5)

        if(world.isCompleteDelevery()):
            noPackageWorld.mapReset()
            havePackageWorld.mapReset()

        if( i == 99):
            show.run_visual(noPackageWorld, havePackageWorld, agent)
        if( i == 199):
            show.run_visual(noPackageWorld, havePackageWorld, agent)


    for j in range(7200):
        oldAgent2 = copy.deepcopy(oldAgent1)
        oldAgent1 = copy.deepcopy(agent)


        if not (agent.havePackage):
            world = noPackageWorld
            world.worldUpdate(havePackageWorld, noPackageWorld)
        else:
            world = havePackageWorld
            world.worldUpdate(noPackageWorld, havePackageWorld)

        SelectMove.PEPLOIT(agent, world, False)
        newAgent = copy.deepcopy(agent)

        if (j >= 1):
            if not (oldAgent2.havePackage):
                updateMatrix.SARSAUpdate(oldAgent2, oldAgent1, newAgent, noPackageWorld, .3, .5)
            elif (oldAgent2.havePackage):
                updateMatrix.SARSAUpdate(oldAgent2, oldAgent1, newAgent, havePackageWorld, .3, .5)


        if (world.isCompleteDelevery()):
            noPackageWorld.mapReset()
            havePackageWorld.mapReset()

        if (j == 1999):
            show.run_visual(noPackageWorld, havePackageWorld, agent)
        if (j == 3999):
            show.run_visual(noPackageWorld, havePackageWorld, agent)
        if (j == 6998):
            show.run_visual(noPackageWorld, havePackageWorld, agent)
