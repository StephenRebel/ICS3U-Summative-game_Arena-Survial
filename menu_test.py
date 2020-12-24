import pygame
pygame.init()

background = pygame.image.load("./Images/GameBackground.jpg")
logo = pygame.image.load("./images/leagueofinvaders.png")

RED = (255, 0, 0)
font = pygame.font.SysFont("cambria", 40)
res = (1280, 720)
screen = pygame.display.set_mode(res)
font1 = font.render("This is going to go seriously wrong", False, RED)

print(pygame.font.get_fonts())

run = True
while run:

    pygame.time.delay(10)

    # For exiting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()

    screen.blit(background, (0, 0))
    screen.blit(logo, ((res[0]/2) - 403, 0))
    screen.blit(font1, (125, 250))

    pygame.display.update()

pygame.quit()    
