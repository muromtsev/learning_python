import pygame

FPS = 60
W = 700
H = 300
WHITE = (255, 255, 255)
BLUE = (0, 70, 255)

RIGHT = 'to the right'
LEFT = 'to the left'
STOP = 'stop'
START = 'start'

pygame.init()
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

x = W//2
y = H//2
r = 50

motion = START

while True:
    sc.fill(WHITE)

    pygame.draw.circle(sc, BLUE, (x, y), r)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                motion = LEFT
            elif event.key == pygame.K_RIGHT:
                motion = RIGHT
        elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                motion = STOP

    if motion == LEFT:
        x -= 3
    elif motion == RIGHT:
        x += 3
    elif motion == STOP and x >= 351:
        x -= 3
    
clock.tick(FPS)