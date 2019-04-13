from agent import Agent
from PDWorld import World
from SelectMove import SelectMove
from Storing import updateMatrix
import copy
from Visualize import Visual

class E4:

    agent = Agent(0, 4, False)
    havePackageWorld = World()
    noPackageWorld = World()

    for i in range(200):
        oldAgent = copy.deepcopy(agent)
        if not (agent.havePackage):
            world = noPackageWorld
        else:
            world = havePackageWorld

        SelectMove.PRANDOM(agent, world, False)
        newAgent = copy.deepcopy(agent)
        updateMatrix.SARSAUpdate(oldAgent, newAgent, world, .3, 1)

    for j in range(7800):
        oldAgent = copy.deepcopy(agent)
        if not (agent.havePackage):
            world = noPackageWorld
        else:
            world = havePackageWorld

        SelectMove.PEPLOIT(agent, world, False)
        newAgent = copy.deepcopy(agent)
        updateMatrix.SARSAUpdate(oldAgent, newAgent, world, .3, 1)

    show = Visual()
    show.run_visual(noPackageWorld, havePackageWorld, agent)
    show.quit()
