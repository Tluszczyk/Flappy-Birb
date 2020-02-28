import random
import Obstacle

class ObstacleList:
    def __init__(self, space, obstacleHole, resolution):
        self.space = space
        self.obstacleHole = obstacleHole
        self.obstacles = [Obstacle.Obstacle(resolution[0]+30, resolution[1]/2, 60, self.obstacleHole, resolution)]
        self.resolution = resolution

    def create(self):
        if self.obstacles[-1].pos[0][0] < self.resolution[0] - self.space:
            self.obstacles.append(Obstacle.Obstacle(self.resolution[0] + 30, random.randint(self.obstacleHole, self.resolution[1] - self.obstacleHole), self.obstacleHole, self.obstacleHole, self.resolution))

    def begin(self):
        self.obstacles = [Obstacle.Obstacle(self.resolution[0] + 30, self.resolution[1] / 2, 60, self.obstacleHole, self.resolution)]