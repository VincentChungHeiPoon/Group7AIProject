#if you have a class you created, use the syntax from "file" import "class"
#aware that file do not have .py extension anymore
from agent import Agent
from PDWorld import World
from PDWorld import Node
import random
from SelectMove import SelectMove

#2d 5x5 grid
agent = Agent(0,0,False)
world = World()

world.map[agent.x][agent.y].qEast = 1
#update score after every move


# SelectMove.PEPLOIT(agent, world)
# SelectMove.PRANDOM(agent, world)
SelectMove.PGREEDY(agent, world)
SelectMove.PGREEDY(agent, world)
SelectMove.PGREEDY(agent, world)
SelectMove.PGREEDY(agent, world)
SelectMove.PGREEDY(agent, world)
SelectMove.PGREEDY(agent, world)
SelectMove.PGREEDY(agent, world)


# print("Agent is at x: ", agent.x, " y: ", agent.y)