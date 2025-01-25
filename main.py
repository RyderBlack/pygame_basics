import pygame
from sys import exit

WIDTH = 800
HEIGHT = 400

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT ))
pygame.display.set_caption('Intro Pygame')
# to control FPS
clock = pygame.time.Clock()

#create Text and font
test_font = pygame.font.Font('fonts/Pixeltype.ttf', 50)

#import images
sky_surface = pygame.image.load('graphics/Sky.png').convert()
ground_surface = pygame.image.load('graphics/ground.png').convert()
text_surface = test_font.render('My PyGame', False, 'Black')

snail_surface = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(bottomright=(600,300))

player_surface = pygame.image.load('graphics/Player/player_walk_1.png').convert_alpha()
player_rect = player_surface.get_rect(midbottom = (80,300))

while True:
    # draw all elements and update everything
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
    screen.blit(sky_surface, (0,0))
    screen.blit(ground_surface, (0,300))
    screen.blit(text_surface, (340, 50))
    
    snail_rect.x -= 3
    if snail_rect.right <=0: snail_rect.left = 800
    screen.blit(snail_surface, snail_rect)
    screen.blit(player_surface, player_rect)
    
    
    pygame.display.update()
    #for 60fps
    clock.tick(60)