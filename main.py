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
        def __init__(self, color=[155,255,155], radius=50, position=[200,300], velocity=[2,2]):
            self.color = color
            self.radius = radius
            self.position = position
            self.velocity = velocity

        def move(self):
            self.position[0] += self.velocity[0]
            self.position[1] += self.velocity[1]

            # Bounce off the left and right walls
            if self.position[0] <= self.radius or self.position[0] >= config.WINDOW_WIDTH - self.radius:
                self.velocity[0] *= -1

            # Bounce off the top and bottom walls
            if self.position[1] <= self.radius or self.position[1] >= config.WINDOW_HEIGHT - self.radius:
                self.velocity[1] *= -1

            draw.draw_circle(screen, {'color':self.color, 'position':self.position, 'radius':self.radius})

    circles = []

    for i in range(random.randint(5,10)):
        circles.append(Circle(color=[random.randint(1,255),random.randint(1,255),random.randint(1,255)], radius=random.randint(5,20), position=[random.randint(30,200),random.randint(30,200)], velocity=[random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]), random.choice([-5, -4, -3, -2, -1, 1, 2, 3, 4, 5])]))
        

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False

        screen.fill(config.WHITE) # Use color from config

        for ball in circles:
            ball.move()


    

        pygame.display.flip()
        # Limit the frame rate to the specified frames per second (FPS)
        clock.tick(config.FPS) # Use the clock to control the frame rate

    pygame.quit()

    sys.exit()

if __name__ == "__main__":
    main()