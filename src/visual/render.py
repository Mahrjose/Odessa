# src/visual/render.py
import pygame
from src.core.simulation import Simulation

class Renderer:
    def __init__(self, width=800, height=600, grid_size=10):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        self.clock = pygame.time.Clock()
        self.grid_size = grid_size
        self.simulation = Simulation(pop_count=12)

    def draw_pops(self):
        """Draw all pops as circles."""
        for pop_pos in self.simulation.get_pops():
            pygame.draw.circle(self.screen, (0, 255, 0), pop_pos, 5)

    def update(self):
        """Update the game and simulation."""
        self.screen.fill((0, 0, 0))  # Clear screen
        self.simulation.update()     # Update simulation logic
        self.draw_pops()             # Draw the pops on the screen
        pygame.display.flip()        # Refresh display
        self.clock.tick(30)          # Limit to 30 frames per second
