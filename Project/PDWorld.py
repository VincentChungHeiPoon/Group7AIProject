#this PDworld contatins the world as 2, 2d arrays, for agent carrrying and not carrying a block

class Node:
    #x, y is position, isPickUp/DropOff refer to is a pick or drop off location, block count is how many block is in the node
    #update them if they are assigned to be a pick up or drop off
    def __init__(self):
        self.isPickUp = False
        self.isDropOff = False
        self.blockCount = 0
        self.qUp = 0
        self.qDown = 0
        self.qLeft = 0
        self.qRight = 0

    def pickUpAblock(self):
        if(self.isPickUp and self.blockCount > 0):
                self.blockCount -= 1

    def canPickUpBlock(self) -> bool:
        if (self.isPickUp and self.blockCount > 0):
            return True
        else:
            return False


    def dropOffBlock(self):
        if(self.isDropOff and self.blockCount < 5):
            self.blockCount += 1

    def canDropOffBlock(self) -> bool:
        if(self.isDropOff and self.blockCount < 5):
            return True
        else:
            return False

class World:
    # this initialize the map for the class
    def __init__(self):
        cols = 5
        rows = 5
        self.map = [[Node() for j in range(cols)] for i in range(rows)]
        self.setPickUp(0,0)
        self.setPickUp(2,2)
        self.setPickUp(4,4)

        self.setDropOff(1,4)
        self.setDropOff(4,0)
        self.setDropOff(4,2)
    #set block as pickUpBlock
    def setPickUp(self, x, y):
        self.map[x][y].isPickUp = True
        self.map[x][y].blockCount = 5
    #set block as dropOffBlock
    def setDropOff(self, x, y):
        self.map[x][y].isDropOff = True

#w = World()
# print(w.map[0][0].blockCount)