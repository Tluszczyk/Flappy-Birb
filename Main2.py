import pygame
import ObstacleList
import Bird
import Points

pygame.init()

gameOn = True

resolution = (1000, 800)

screen = pygame.display.set_mode(resolution, pygame.FULLSCREEN)

bird = Bird.Bird(40, 30, 40, resolution[1] / 2, "resources/birdSprite.png")

obstacles = ObstacleList.ObstacleList(450, 180, resolution)

clock = pygame.time.Clock()

clock.tick()

points = Points.Points()

def check_death():
    obsUp = pygame.Rect(obstacles.obstacles[0].pos[0], obstacles.obstacles[0].size[0])
    obsDown = pygame.Rect(obstacles.obstacles[0].pos[1], obstacles.obstacles[0].size[1])
    birdR = bird.rect

    if birdR.colliderect(obsUp) or birdR.colliderect(obsDown) or birdR.bottom > resolution[1]-30:
        return True
    return False

def check_points(points):
    obsUp = pygame.Rect(obstacles.obstacles[0].pos[0], obstacles.obstacles[0].size[0])
    birdR = bird.rect

    if birdR.centerx - obsUp.centerx in range(0, bird.velocity[0]):
        points.value += 1
        points.update()
    return points


while gameOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOn = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.fly()
            elif event.key == pygame.K_ESCAPE:
                gameOn = False
            elif event.key == pygame.K_r:
                obstacles.begin()
                bird.begin()


    obstacles.create()

    for obstacle in obstacles.obstacles:
        obstacle.update()
        if obstacles.obstacles[0].pos[0][0] < -obstacles.obstacles[0].size[0][0]:
            obstacles.obstacles.pop(0)

    bird.fall()

    pygame.draw.rect(screen, (0, 0, 255), pygame.rect.Rect((0, 0), resolution))
    pygame.draw.rect(screen, (91, 64, 6), pygame.rect.Rect(0, resolution[1] - 30, resolution[0], 30))

    screen.blit(bird.image, bird.pos)

    for obstacle in obstacles.obstacles:
        screen.blit(obstacle.body[0], obstacle.pos[0])
        screen.blit(obstacle.body[1], obstacle.pos[1])

    screen.blit(points.textSurface, (10, 10))
    pygame.display.update()

    if check_death():gameOn = False
    points = check_points(points)

    pygame.time.wait(100//3 - clock.get_time())
    clock.tick()

pygame.quit()
quit()
