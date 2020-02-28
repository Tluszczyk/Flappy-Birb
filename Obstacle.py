import pygame

class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y, width, space, resolution):
        self.color = (0, 255, 0)
        self.pos = [[x, y-900], [x, y+100]]
        self.velocity = 10
        self.size = [
            [129, 800],
            [129, 800]
        ]

        self.body = [
            pygame.transform.scale(pygame.image.load('resources/ObstacleUp.png'), (129, 800)),
            pygame.transform.scale(pygame.image.load('resources/ObstacleDown.png'), (129, 800))
        ]

        self.rect = self.body[0].get_rect().union(self.body[1].get_rect())

        self.resolution = resolution

    def update(self):
        self.pos[0][0] = self.pos[0][0] - self.velocity
        self.pos[1][0] = self.pos[1][0] - self.velocity