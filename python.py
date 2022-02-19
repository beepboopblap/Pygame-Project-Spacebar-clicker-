from curses.ascii import ESC
import pygame
from pygame.locals import * 
from pygame import mixer

pygame.init()
fps = pygame.time.Clock()
window = pygame.display.set_mode((800,600))

#declare colours, images, sounds, fonts
blue = (0,0,255)
green = (0,255,0)
red = (255,0,0)
yellow = (255,255,0)
black = (0,0,0)
white = (255,255,255)
Calibri60 = pygame.font.SysFont("Calibri", 60)



#variables for keeping track of my game players etc.

quit = False

mouse_x = 0
mouse_y = 0
space = False
space_counter = 0

#main game loop
while  not quit:

    #process events
    for event in pygame.event.get():
        print(event)
        if event.type == QUIT:
            quit = True 
        elif event.type == MOUSEMOTION:
            (mouse_x,mouse_y) = event.pos
        elif event.type == KEYDOWN:
            if event.key == K_SPACE:
                space = True
                if space == True:
                    spacebar_sfx = mixer.Sound("spacebar_soundfx.mp3")
                    spacebar_sfx.play()
        elif event.type == KEYUP:
            if event.key == K_SPACE:
                space = False
            if event.key == K_ESCAPE:
                pygame.quit()
          
    

    #perform calculations

    #draw graphics
    window.fill(yellow)
    label = Calibri60.render("Hello Pygame!", 1, black,)
    window.blit(label, (258,100))
    label_coordinates = Calibri60.render("Mouse At " + str(mouse_x) + "," + str(mouse_y), 1, red)
    window.blit(label_coordinates, (258,180))

    if space:
        space_pressed = Calibri60.render("Spacebar",1, green)
    else:
        space_pressed = Calibri60.render("Spacebar",1, red)
    window.blit(space_pressed, (100,500))
    
    pygame.draw.line(window, black, (50,60), (50,200), 20)
    pygame.draw.rect(window, blue, (80,100,100,40), 7)
    pygame.draw.circle(window, white, (200,200), 50, 5)
    pygame.draw.ellipse(window, green, (150,300,100,50), 5)

    pygame.display.update()
    fps.tick(25)

#loop over, game over
pygame.quit()


