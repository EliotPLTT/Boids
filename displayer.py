from agents import *

import pygame, sys, random
from pygame.locals import *

def convertRealToScreen(vecteur):
    vecteur = vecteur * (WINDOW_SIZE / areaRadius)
    return vecteur


def main () :

    boids = initAgents(N, vec2(areaRadius//4,areaRadius//4), spawnRadius, "A")
    boids += initAgents(N, vec2(areaRadius//2,areaRadius//2), spawnRadius, "B")
    boids += initAgents(2, vec2(areaRadius//2,areaRadius//2), spawnRadius, "C")
    
    looping = True

    WINDOW.fill(BACKGROUND)
    while looping :
        WINDOW.fill(BACKGROUND)
        
        for event in pygame.event.get() :
            if event.type == QUIT :
                pygame.quit()
                sys.exit()

        for boid in boids:
            boid.updAgent(boids)
            pygame.draw.circle(WINDOW,boid.color,convertRealToScreen(boid.pos).tup(),5)    

    
        pygame.display.update()
        fpsClock.tick(FPS)

        

#INIT
pygame.init()


# Game Setup
BACKGROUND = (255, 255, 255)
FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_SIZE = 600
 
WINDOW = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
pygame.display.set_caption('Boids!')
 
main()

