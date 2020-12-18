import pygame
pygame.init()

#Main game setup
bg = pygame.image.load('Pygame/bg.jpg')
screen = pygame.display.set_mode((700, 500))
pygame.display.set_caption("My First Game")
clock = pygame.time.Clock()

#Make Variables
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
BLUE = ( 0, 0, 225)
RED = ( 255, 0, 0)
BROWN = (210, 105, 30)

x1, y1, width1, height1 = 50, 50, 20, 20
x2, y2, width2, height2 = 150, 150, 20, 20
x, y, shootwidth, shootheight = -10, -10, 15, 5
p1face, p2face = 1, 1

can_shoot = False

#Draw things on screen procedure
def draw_objects():
    screen.blit(bg, (0, 0))
    pygame.draw.rect(screen, BLUE, (x1, y1, width1, height1))
    pygame.draw.rect(screen, RED, (x2, y2, width2, height2))
    pygame.draw.rect(screen, BLACK, (x, y, shootwidth, shootheight))
    pygame.display.update()

#Main Loop
carryOn = True
while carryOn:

    pygame.time.delay(10)

    #For exiting
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            carryOn = False 
 
    #Detect if player hit keys
    keys = pygame.key.get_pressed()

    #Movement for both players
    if keys[pygame.K_LEFT]:
        p1face = 1
        if x1 - 1 <= 0:
            x1 = 0 
        else:
            x1 -= 1

    if keys[pygame.K_RIGHT]:
        p1face = 3
        if x1 + 1 >= 700 - width1:
            x1 = 700 - width1
        else:
            x1 += 1

    if keys[pygame.K_UP]:
        p1face = 4
        if y1 - 1 <= 0:
            y1 = 0 
        else:
            y1 -= 1

    if keys[pygame.K_DOWN]:
        p1face = 2
        if y1 + 1 >= 500 - height1:
            y1 = 500 - height1
        else: 
            y1 += 1

    if keys[pygame.K_a]:
        p2face = 1
        if x2 - 1 <= 0:
            x2 = 0
        else:
            x2 -= 1

    if keys[pygame.K_d]:
        p1face = 3
        if x2 + 1 >= 700 - width2:
            x2 = 700 - width2
        else:
            x2 += 1

    if keys[pygame.K_w]:
        p1face = 4
        if y2 - 1 <= 0:
            y2 = 0
        else:
            y2 -= 1

    if keys[pygame.K_s]:
        p1face = 2
        if y2 + 1 >= 500 - height2:
            y2 = 500 - height2
        else: 
            y2 += 1

    if keys[pygame.K_SPACE]:
        if can_shoot == False:
            can_shoot = True
            x, y, = x1 + width1 / 2, y1 + height1 / 2 - shootheight / 2
    
    if can_shoot == True:
        if x < 700:
            x += 10
        else:
            can_shoot = False
 
    draw_objects()
#Once we have exited the main program loop we can stop the game engine:
pygame.quit()