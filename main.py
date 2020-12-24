import pygame
pygame.init()

from menu_test import main_menu

window = 0
main_menu()

background = pygame.image.load("./Images/GameBackground.jpg")
BLACK = (0, 0, 0)
font = pygame.font.SysFont("cambria", 40)
res = (1280, 720)
screen = pygame.display.set_mode(res)


while True:

    pygame.time.delay(10)
    font1 = font.render(f"Window num: {window}", False, BLACK)

    # For exiting
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    if window == 0:
        main_menu()

    elif window == 1:
        screen.blit(background, (0, 0))
        screen.blit(font1, (125, 250))

    pygame.display.update()      