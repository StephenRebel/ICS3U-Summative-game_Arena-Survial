import pygame
import random
pygame.init()

#Main game setup
bg = pygame.image.load('Learning and Practice/PygameTesting/Images/bg.jpg')
char1 = pygame.image.load('Learning and Practice/PygameTesting/Images/char1.png')
size = (1080, 720)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My First Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont('Arial', 30)
effect1 = pygame.mixer.Sound('Learning and Practice/PygameTesting/Sounds/randomsound.wav')
effect2 = pygame.mixer.Sound('Learning and Practice/PygameTesting/Sounds/soundeffect.wav')
pygame.mixer.music.load('Learning and Practice/PygameTesting/Sounds/musictest.mp3')

#Make Variables
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
BLUE = ( 0, 0, 225)
RED = ( 255, 0, 0)
BROWN = (210, 105, 30)

x1, y1, width1, height1, oldx1, oldy1 = 50, 50, 64, 64, 50, 50
x2, y2, width2, height2, oldx2, oldy2 = 850, 150, 64, 64, 150, 150
x, y, shootwidth, shootheight, shootdirection = -10, -10, 15, 10, 0
p1face, p2face = 0, 0
point1, point2 = 0, 0
can_shoot = False

#Draw things on screen procedure
def draw_objects():
    new_char1 = pygame.transform.rotate(char1, p1face)
    screen.blit(bg, (0, 0))
    screen.blit(new_char1, (x1, y1))
    pygame.draw.rect(screen, RED, (x2, y2, width2, height2))
    pygame.draw.rect(screen, BLACK, (x, y, shootwidth, shootheight))
    text1 = font.render("Shooting Player Points: " + str(point1), True, BLACK)
    text2 = font.render("Running Player Points: " + str(point2), True, BLACK)
    screen.blit(text1, (100 , 100))
    screen.blit(text2, (100 , 150))
    pygame.display.update()

#Main Loop
pygame.mixer.music.play(-1)
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
    oldx1, oldy1, oldx2, oldy2 = x1, y1, x2, y2
    if keys[pygame.K_LEFT]:
        p1face = 90
        if x1 - 1 <= 0:
            x1 = 0 
        else:
            x1 -= 2
    elif keys[pygame.K_RIGHT]:
        p1face = 270
        if x1 + 1 >= size[0] - width1:
            x1 = size[0] - width1
        else:
            x1 += 2
    elif keys[pygame.K_UP]:
        p1face = 0
        if y1 - 1 <= 0:
            y1 = 0 
        else:
            y1 -= 2
    elif keys[pygame.K_DOWN]:
        p1face = 180
        if y1 + 1 >= size[1] - height1:
            y1 = size[1] - height1
        else: 
            y1 += 2

    if keys[pygame.K_a]:
        p2face = 1
        if x2 - 1 <= 0:
            x2 = 0
        else:
            x2 -= 3
    elif keys[pygame.K_d]:
        p2face = 3
        if x2 + 1 >= size[0] - width2:
            x2 = size[0] - width2
        else:
            x2 += 3
    elif keys[pygame.K_w]:
        p2face = 4
        if y2 - 1 <= 0:
            y2 = 0
        else:
            y2 -= 3
    elif keys[pygame.K_s]:
        p2face = 2
        if y2 + 1 >= size[1] - height2:
            y2 = size[1] - height2
        else: 
            y2 += 3
    #Auto moving AI
    else:
        if (x2 + width2 / 2) - (x1 + width1 / 2) > 0:
            x2 -= 1
        elif (x2 + width2 / 2) - (x1 + width1 / 2) < 0:
            x2 += 1
        if (y2 + height2 / 2) - (y1 + height1 / 2) > 0:
            y2 -= 1
        elif (y2 + height2 / 2) - (y1 + height1 / 2) < 0:
            y2 += 1

    #Detects if there should be a bullet
    if keys[pygame.K_SPACE]:
        if can_shoot == False:
            can_shoot = True
            x, y, = int(x1 + width1 / 2), int(y1 + height1 / 2 - shootheight / 2)
            if p1face == 90:
                shootdirection = 2
                shootwidth = 20
                shootheight = 10
            elif p1face == 270:
                shootdirection = 0
                shootwidth = 20
                shootheight = 10
            elif p1face == 0:
                shootdirection = 3
                shootwidth = 10
                shootheight = 20
            elif p1face == 180:
                shootdirection = 1
                shootwidth = 10
                shootheight = 20
    
    #Controls direction of bullet
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

    #Collision between two characters
    for x1pos in range(x1, x1 + width1):
        if x2 + width2 >= x1pos >= x2:
            for y1pos in range(y1, y1 + height1):
                if y2 + height2 >= y1pos >= y2:
                    #x1, y1, x2, y2 = oldx1, oldy1, oldx2, oldy2
                    point2 += 1
                    x1, y1 = random.randrange(width1, size[0] - width1), random.randrange(height1, size[1] - height1)
                    effect1.play()
                    break
            break

    #Collision between character 2 and bullet
    for shootxpos in range(x, x + shootwidth):
        if x2 + width2 >= shootxpos >= x2:
            for shootypos in range(y, y + shootheight):
                if y2 + height2 >= shootypos >= y2:
                    x, y = -15, -15
                    x2, y2 = random.randrange(width2, size[0] - width2), random.randrange(height2, size[1] - height2)
                    effect2.play()
                    can_shoot = False
                    point1 += 1
                    break
            break

    draw_objects()
#Once we have exited the main program loop we can stop the game engine:
pygame.quit()