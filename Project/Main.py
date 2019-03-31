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

#update score after every move

n = Node()

n.qNorth = 1
n.qSouth = 1

print(SelectMove.findBestQValue(n))
print(SelectMove.findBestQValue(n))
print(SelectMove.findBestQValue(n))
print(SelectMove.findBestQValue(n))
print(SelectMove.findBestQValue(n))


# SelectMove.PRANDOM(agent, world)
# SelectMove.PRANDOM(agent, world)
# SelectMove.PRANDOM(agent, world)
# SelectMove.PRANDOM(agent, world)
# SelectMove.PRANDOM(agent, world)
# SelectMove.PRANDOM(agent, world)
# SelectMove.PRANDOM(agent, world)
# SelectMove.PRANDOM(agent, world)
# SelectMove.PRANDOM(agent, world)

# value = [ 2, 3, 1, 4 ]
# value.sort(reverse= True)
# print(value)