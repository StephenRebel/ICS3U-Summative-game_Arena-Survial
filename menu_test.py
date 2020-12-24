import pygame
pygame.init()

background = pygame.image.load("./Images/GameBackground.jpg")
logo = pygame.image.load("./images/leagueofinvaders.png")

RED = (255, 0, 0)
BLACK = (0, 0, 0)
LIGHT_GR = (211, 211, 211)
DARK_GR = (71, 71, 71)
font = pygame.font.SysFont("cambria", 40)
res = (1280, 720)
screen = pygame.display.set_mode(res)
font1 = font.render("This is going to go seriously wrong", False, RED)

run = True
while run:

    pygame.time.delay(10)
    mouse = pygame.mouse.get_pos()
    pressed = pygame.mouse.get_pressed()

    # For exiting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

    screen.blit(background, (0, 0))
    screen.blit(logo, ((res[0]/2) - 403, 0))
    if 446 <= mouse[0] <= 835 and 561 <= mouse[1] <= 675 and pressed[0] == True:
        pygame.draw.rect(screen, DARK_GR, ((res[0]/2) - 194, 561, 389, 114))
        window = 1
    elif 446 <= mouse[0] <= 835 and 561 <= mouse[1] <= 675:
        pygame.draw.rect(screen, DARK_GR, ((res[0]/2) - 194, 561, 389, 114))
    else:
        pygame.draw.rect(screen, LIGHT_GR, ((res[0]/2) - 194, 561, 389, 114))
    pygame.draw.rect(screen, BLACK, ((res[0]/2) - 200, 555, 400, 125), 7, 10)
    screen.blit(font1, (125, 250))

    pygame.display.update()

pygame.quit()    
