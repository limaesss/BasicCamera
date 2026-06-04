import pygame as pg

class Camera:
    def __init__(self):
        self.holdKeys = pg.key.get_pressed()
        self.tapKeys = pg.key.get_just_pressed()

        self.leftVel = 0
        self.rightVel = 0
        self.upVel = 0
        self.downVel = 0