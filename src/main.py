# main.py
import pygame
from src.visual.render import Renderer

def main():
    renderer = Renderer()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        renderer.update()

    pygame.quit()

if __name__ == "__main__":
    main()
