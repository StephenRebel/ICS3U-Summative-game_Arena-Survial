import pygame
pygame.init()

#Main game setup
bg = pygame.image.load('Learning and Practice/PygameTesting/bg.jpg')
char1 = pygame.image.load('Learning and Practice/PygameTesting/char1.png')
size = (1080, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My First Game")
clock = pygame.time.Clock()

#Make Variables
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
BLUE = ( 0, 0, 225)
RED = ( 255, 0, 0)
BROWN = (210, 105, 30)

x1, y1, width1, height1 = 50, 50, 64, 64
x2, y2, width2, height2 = 150, 150, 20, 20
x, y, shootwidth, shootheight, shootdistance, shootdirection = -10, -10, 15, 5, [-10, -10], 0
p1face, p2face = 0, 0

can_shoot = False

#Draw things on screen procedure
def draw_objects():

    new_char1 = pygame.transform.rotate(char1, p1face)

    screen.blit(bg, (0, 0))
    screen.blit(new_char1, (x1, y1))
    #pygame.draw.rect(screen, BLUE, (x1, y1, width1, height1))
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
        p1face = 90
        if x1 - 1 <= 0:
            x1 = 0 
        else:
            x1 -= 3
    elif keys[pygame.K_RIGHT]:
        p1face = 270
        if x1 + 1 >= size[0] - width1:
            x1 = size[0] - width1
        else:
            x1 += 3
    elif keys[pygame.K_UP]:
        p1face = 0
        if y1 - 1 <= 0:
            y1 = 0 
        else:
            y1 -= 3
    elif keys[pygame.K_DOWN]:
        p1face = 180
        if y1 + 1 >= size[1] - height1:
            y1 = size[1] - height1
        else: 
            y1 += 3

    if keys[pygame.K_a]:
        p2face = 1
        if x2 - 1 <= 0:
            x2 = 0
        else:
            x2 -= 1
    elif keys[pygame.K_d]:
        p2face = 3
        if x2 + 1 >= size[0] - width2:
            x2 = size[0] - width2
        else:
            x2 += 1
    elif keys[pygame.K_w]:
        p2face = 4
        if y2 - 1 <= 0:
            y2 = 0
        else:
            y2 -= 1
    elif keys[pygame.K_s]:
        p2face = 2
        if y2 + 1 >= size[1] - height2:
            y2 = size[1] - height2
        else: 
            y2 += 1
    else:
        if (x2 + width2 / 2) - (x1 + width1 / 2) > 0:
            x2 -= 0.5
        elif (x2 + width2 / 2) - (x1 + width1 / 2) < 0:
            x2 += 0.5
        if (y2 + height2 / 2) - (y1 + height1 / 2) > 0:
            y2 -= 0.5
        elif (y2 + height2 / 2) - (y1 + height1 / 2) < 0:
            y2 += 0.5

    if keys[pygame.K_SPACE]:
        if can_shoot == False:
            can_shoot = True
            x, y, = x1 + width1 / 2, y1 + height1 / 2 - shootheight / 2
            if p1face == 90:
                shootdirection = 2
                shootwidth = 15
                shootheight = 5
            elif p1face == 270:
                shootdirection = 0
                shootwidth = 15
                shootheight = 5
            elif p1face == 0:
                shootdirection = 3
                shootwidth = 5
                shootheight = 15
            elif p1face == 180:
                shootdirection = 1
                shootwidth = 5
                shootheight = 15
    
    if can_shoot == True:
        if shootdirection == 2:
            if x > -15:
                x -= 10
            else:
                can_shoot = False
        elif shootdirection == 0:
            if x < size[0]:
                x += 10
            else:
                can_shoot = False
        elif shootdirection == 3:
            if y > -15:
                y -= 10
            else:
                can_shoot = False
        elif shootdirection == 1:
            if y < size[1]:
                y += 10
            else:
                can_shoot = False
                
    draw_objects()
#Once we have exited the main program loop we can stop the game engine:
pygame.quit()