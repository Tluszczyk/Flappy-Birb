import pygame as py

class Points:
    def __init__(self):
        py.font.init()

        self.value = 0
        self.font = py.font.SysFont('Commic Sans', 50)
        self.textSurface = self.font.render(str(self.value), False, (255, 255, 255))

    def update(self):
        self.textSurface = self.font.render(str(self.value), False, (255, 255, 255))