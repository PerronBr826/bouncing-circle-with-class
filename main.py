# Pygame game template

import pygame
import sys
import config # Import the config module
import random
import draw # Import the drawing module

def init_game ():
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT)) # Use constants from config

    pygame.display.set_caption(config.TITLE)
    return screen


def main():

    screen = init_game()
    clock = pygame.time.Clock() # Initialize the clock here
    running = True

    class Circle():
        """Round Class for Cirular Applications or something"""
        def __init__(self, color=[155,255,155], size=50, position=[200,300], velocity=[2,2]):
            self.color = color
            self.size = size
            self.position = position
            self.velocity = velocity

        def move(self):
            self.position[0] += self.velocity[0]
            self.position[1] += self.velocity[1]

            draw.draw_circle(screen, {'color':self.color, 'position':self.position, 'radius':50})

    ball = Circle()


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        screen.fill(config.WHITE) # Use color from config


        ball.move()
    

        pygame.display.flip()
        # Limit the frame rate to the specified frames per second (FPS)
        clock.tick(config.FPS) # Use the clock to control the frame rate

    pygame.quit()

    sys.exit()

if __name__ == "__main__":
    main()