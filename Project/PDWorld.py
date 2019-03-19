#this PDworld contatins the world as 2, 2d arrays, for agent carrrying and not carrying a block

class Node:
    #x, y is position, isPickUp/DropOff refer to is a pick or drop off location, block count is how many block is in the node
    def __init__(self, x, y, isPickUp, isDropOff, blockCount):
        self.x = x
        self.y = y
        self.isPickUp = isPickUp
        self.isDropOff = isDropOff
        self.blockCount = blockCount

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


