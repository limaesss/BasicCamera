import pygame as pg

class Camera:
    def __init__(self):
        self.instances = []

        self.holdKeys = pg.key.get_pressed()
        self.tapKeys = pg.key.get_just_pressed()

        self.leftVel = 0
        self.rightVel = 0
        self.upVel = 0
        self.downVel = 0

        self.maxVel = 4

        self.accel = 0.5
        self.decell = 0.4

        self.targetOffsetX = 0
        self.targetOffsetY = 0
        self.offsetX = self.targetOffsetX
        self.offsetY = self.targetOffsetY

    def update(self): # it updates the velocities then moves everything
        holdKeys = self.holdKeys # for less self.'s i hate them
        if holdKeys[pg.K_LEFT]:
            self.leftVel = min(self.leftVel + self.accel, self.maxVel) # increments leftVel until it hits maxVel
        else:
            self.leftVel = max(self.leftVel - self.decell, 0) # decrements leftVel until it hits 0

        # same for all the 'if' statements below

        if holdKeys[pg.K_RIGHT]:
            self.rightVel = min(self.rightVel + self.accel, self.maxVel)
        else:
            self.rightVel = max(self.rightVel - self.decell, 0)

        if holdKeys[pg.K_UP]:
            self.upVel = min(self.upVel + self.accel, self.maxVel)
        else:
            self.upVel = max(self.upVel - self.decell, 0)

        if holdKeys[pg.K_DOWN]:
            self.downVel = min(self.downVel + self.accel, self.maxVel)
        else:
            self.downVel = max(self.downVel - self.decell, 0)
        
        self.moveEverything()

    def moveEverything(self):
        for instance in self.instances:

            instance.x -= round(self.rightVel) # rounded because 
            instance.x += round(self.leftVel) # it was buggy without it

            instance.y += round(self.upVel)
            instance.y -= round(self.downVel)

            self.applyOffset(instance.x,instance.y) # apply offset to all the instances

    def updateOffset(self, customMax, customMultiplier, customOffsetReducer):
        xVel = round(self.rightVel, customMax) - round(self.leftVel, customMax) # xVel,yVel made  
        yVel = round(self.downVel, customMax) - round(self.upVel, customMax) # so it takes less lines of code, and looks simpler

        self.targetOffsetX = -xVel * customMultiplier # customizable for the purposes of me
        self.targetOffsetY = -yVel * customMultiplier # being picky asf lol

        self.offsetX += (self.targetOffsetX - self.offsetX) * customOffsetReducer # offset reducer so
        self.offsetY += (self.targetOffsetY - self.offsetY) * customOffsetReducer # it doesnt fly away

    def applyOffset(self, x, y):
        return x + self.offsetX, y + self.offsetY 

    def getPlayerPosition(self, screenHeight):
        screenCenterX = 935
        screenCenterY = screenHeight / 2

        playerX = screenCenterX + self.offsetX
        playerY = screenCenterY + self.offsetY 
        
        return playerX, playerY
