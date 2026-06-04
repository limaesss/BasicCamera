import pygame as pg

class Camera:
    def __init__(self):
        self.holdKeys = pg.key.get_pressed()
        self.tapKeys = pg.key.get_just_pressed()

        self.leftVel = 0
        self.rightVel = 0
        self.upVel = 0
        self.downVel = 0

        self.maxVel = 4

        self.accel = 0.5
        self.decell = 0.4