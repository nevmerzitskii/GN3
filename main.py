import pygame

W = 800
H = 600
с = (250, 250, 250)

pygame.init()
pygame.display.set_caption('что')
pygame.mouse.set_visible(False)
screen = pygame.display.set_mode((W, H))

font = pygame.font.SysFont('Arial', 28, True, False)
font2 = pygame.font.SysFont('Arial', 14, True, False)
font_box = pygame.Surface((W - 30, font.get_height()))
font_box_rect = font_box.get_rect(center=(W // 2, H - 30))

screen.blit(font.render('Всем привет', True, BLACK)

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_ESCAPE:
               run = False
    pygame.display.update()
