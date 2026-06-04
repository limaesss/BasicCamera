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

    def update(self):
        holdKeys = self.holdKeys
        if holdKeys[pg.K_LEFT]:
            self.leftVel = min(self.leftVel + self.accel, self.maxVel)
        else:
            self.leftVel = max(self.leftVel - self.decell, 0)

        if holdKeys[pg.K_RIGHT]:
            self.rightVel = min(self.rightVel + self.accel, self.maxVel)
        else:
            self.rightVel = max(self.rightVel - self.decell, 0)

        if holdKeys[pg.K_UP]:
            self.upVel = min(self.upVel + self.accel, self.maxVel)
        else:
            self.upVel = max(self.upVel - self.decell, 0)

        if holdKeys[pg.K_DOWN]:
            # Notice I changed downVel to downVel consistently
            self.downVel = min(self.downVel + self.accel, self.maxVel)
        else:
            self.downVel = max(self.downVel - self.decell, 0)

        self.moveEverything()