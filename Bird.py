import pygame

GRAVITY = 1.5

class Bird(pygame.sprite.Sprite):
    def __init__(self, width, height, x, y, img):
        pygame.sprite.Sprite.__init__(self)
        self.color = (229, 193, 13)
        self.pos = [x, y]
        self.velocity = [10, 0]
        self.size = [width, height]
        self.image0 = pygame.Surface([width, height])
        self.image0 = pygame.transform.scale(pygame.image.load(img), (100, 60))

        self.image = self.image0
        self.rect = self.image.get_rect()
        pygame.draw.rect(self.image, self.color, [self.pos[0]-self.size[0]/2, self.pos[1]-self.size[1]/2, width, height])
        self.angle = 0

    def fall(self):
        self.velocity[1] -= GRAVITY
        self.pos[1] -= self.velocity[1]
        if self.velocity[1] < 0 and self.angle > -45:
            self.angle -= 2
        elif self.velocity[1] > 0 and self.angle < 45:
            self.angle += 2

        self.image = pygame.transform.rotate(self.image0, self.angle)

        self.rect.left = self.pos[0]
        self.rect.top = self.pos[1]

    def fly(self):
        self.velocity[1] = 15

    def begin(self):
        self.pos = self.pos0
        self.velocity = [10, 0]
