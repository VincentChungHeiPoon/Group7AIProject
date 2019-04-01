# this file conatins the complete learning algoritm

from agent import Agent
from PDWorld import World
from PDWorld import Node

#find move, and update the table later
#equation for q learning
# Q(a,s)  (1-alpha) * Q(a,s) + alpha * [R(s’,a,s) + gamma * max,Q(a’,s’)]

class updateTable:
    def moveDirection(oldAgent, newAgent) -> int:
#0,1,2,3,4 for North, East, South, West, stayput(pickup/dropoff)
        #if stayput
        if(newAgent.x == oldAgent.x and newAgent.y == oldAgent.y):
            return 4
        #moved north
        elif(newAgent.y < oldAgent.y and newAgent.x == oldAgent.x):
            return 0
        #moved East
        elif(newAgent.x > oldAgent.x and newAgent.y == oldAgent.y):
            return 1
        #moved south
        elif(newAgent.y > oldAgent.y and newAgent.x == oldAgent.x):
            return 2
        #moved West
        elif(newAgent.x < oldAgent.x and newAgent.y == oldAgent.y):
            return 3


a = Agent(2,2, False)
b = a
b.moveNorth(0)
print(b.y)
print(updateTable.moveDirection(b, a))