#if you have a class you created, use the syntax from "file" import "class"
#aware that file do not have .py extension anymore
from agent import Agent
from PDWorld import World
from PDWorld import Node
import random

#2d 5x5 grid
agent = Agent(0,0,False)
world = World()


#move, update, repeat till done


#path finding
#roll untill a random valid move 0,1,2,3 corrispond to north, east, south, west
def selectMovePRANDOM(agent, world):
    if(world.map[agent.x][agent.y].isPickUp and world.map[agent.x][agent.y].canPickUpBlock and agent.canPickUp()):
        world.map[agent.x][agent.y].pickUpAblock()
        agent.pickUpPackage()
        agent.score += 13
        print("Agent Picked Up Block")
    elif(world.map[agent.x][agent.y].isDropOff and world.map[agent.x][agent.y].canDropOffBlock and agent.canDropOff()):
        world.map[agent.x][agent.y].dropOffBlock()
        agent.dropOffPackage()
        agent.score += 13
        print("Agent Dropped Off Block")
    else:
        legalMove = False
        while not (legalMove):
            move = random.randint(0,3)
            print(agent.x, agent.y)
            if(move == 0 and agent.canMoveUp(0)):
                agent.moveUp(0)
                legalMove = True
                print("Agent moved North")
            elif(move == 1 and agent.canMoveRight(4)):
                agent.moveRight(4)
                legalMove = True
                print("Agent moved East")
            elif (move == 2 and agent.canMoveDown(4)):
                agent.moveDown(4)
                legalMove = True
                print("Agent moved South")
            elif (move == 3 and agent.canMoveLeft(0)):
                agent.moveLeft(0)
                legalMove = True
                print("Agent moved West")

        agent.score -= 1
            #print(agent.x, agent.y)






# selectMovePRANDOM(agent, world)
# selectMovePRANDOM(agent, world)
# selectMovePRANDOM(agent, world)
# selectMovePRANDOM(agent, world)
# selectMovePRANDOM(agent, world)
# selectMovePRANDOM(agent, world)
# selectMovePRANDOM(agent, world)
# selectMovePRANDOM(agent, world)
# selectMovePRANDOM(agent, world)
# selectMovePRANDOM(agent, world)
# selectMovePRANDOM(agent, world)
# print(agent.score)