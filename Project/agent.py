#this class catains the information about the agent
class Agent:
    def __init__(self, startingX, startingY, havePackage):
        self.x = startingX
        self.y = startingY
        self.havePackage = havePackage

        #move up if there is space above you
    def moveUp(self, mapUpperLimiteIndex):
        if(self.y + 1 <= mapUpperLimiteIndex):
            self.y += 1
        else:
            print("(up) is not a valid move")

    def moveDown(self, mapLowerLimitIndex):
        if(self.y - 1 >= mapLowerLimitIndex):
            self.y -= 1
        else:
            print("(down) is not a valid move")

    def moveLeft(self, mapLeftLimiteIndex):
        if(self.x - 1 >= mapLeftLimiteIndex):
            self.x -= 1
        else:
            print("(left) is not a valid move")

    def moveRight(self, mapRightLimitIndex):
        if(self.x + 1 <= mapRightLimitIndex):
            self.x += 1
        else:
            print("(right) is not a valid move")

    def isCarryingPackage(self):
        return self.havePackage

    def pickUpPackage(self):
        if not (self.havePackage):
            self.havePackage = True
        else:
            print("(pick up package) is not a valid move")

    def dropOffPackage(self):
        if(self.havePackage):
            self.havePackage = False
        else:
            print("(drop off package) is not a valid move")