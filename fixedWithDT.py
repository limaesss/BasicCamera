import pygame as pg

pg.init()

class Camera:
    def __init__(self):
        self.instances = []

        self.leftVel = 0
        self.rightVel = 0
        self.upVel = 0
        self.downVel = 0

        self.maxVel = 300

        self.accel = 30
        self.decell = 25

        self.targetOffsetX = 0
        self.targetOffsetY = 0
        self.offsetX = self.targetOffsetX
        self.offsetY = self.targetOffsetY

    def update(self, holdKeys, dt): 
        # it updates the velocities then moves everything
        if holdKeys[pg.K_a]:
            self.leftVel = min(self.leftVel + self.accel * dt, self.maxVel * dt) # increments leftVel until it hits maxVel
        else:
            self.leftVel = max(self.leftVel - self.decell * dt, 0) # decrements leftVel until it hits 0

        # same for all the 'if' statements below

        if holdKeys[pg.K_d]:
            self.rightVel = min(self.rightVel + self.accel * dt, self.maxVel * dt)
        else:
            self.rightVel = max(self.rightVel - self.decell * dt, 0)

        if holdKeys[pg.K_w]:
            self.upVel = min(self.upVel + self.accel * dt, self.maxVel * dt)
        else:
            self.upVel = max(self.upVel - self.decell * dt, 0)

        if holdKeys[pg.K_s]:
            self.downVel = min(self.downVel + self.accel * dt, self.maxVel * dt)
        else:
            self.downVel = max(self.downVel - self.decell * dt, 0)
        
        self.moveEverything(dt)

    def moveEverything(self, dt):
        for instance in self.instances:

            instance.x -= round(self.rightVel) # rounded because 
            instance.x += round(self.leftVel) # it was buggy without it

            instance.y += round(self.upVel)
            instance.y -= round(self.downVel)

            self.applyOffset(instance.x,instance.y) # apply offset to all the instances

    def updateOffset(self, customMultiplier, customOffsetReducer, dt):
        customOffsetReducer = max(0, min(customOffsetReducer, 1))

        xVel = (round(self.rightVel - self.leftVel))# xVel,yVel made  
        yVel = (round(self.downVel - self.upVel)) # so it takes less lines of code, and looks simpler

        self.targetOffsetX = (-xVel * customMultiplier) # customizable for the purposes of me
        self.targetOffsetY = (-yVel * customMultiplier) # being picky asf lol

        self.offsetX += ((self.targetOffsetX - self.offsetX) * customOffsetReducer) # offset reducer so
        self.offsetY += ((self.targetOffsetY - self.offsetY) * customOffsetReducer) # it doesnt fly away

    def applyOffset(self, x, y):
        return x + self.offsetX, y + self.offsetY 

    def addInstance(self, instance):
        self.instances.append(instance)

    def getPlayerPosition(self, screenHeight):
        screenCenterX = 935
        screenCenterY = screenHeight / 2    

        playerX = screenCenterX + self.offsetX
        playerY = screenCenterY + self.offsetY 
        
        return playerX, playerY

camera = Camera()