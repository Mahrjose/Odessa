# src/core/simulation.py
from src.core.population import Pop

class Simulation:
    def __init__(self, pop_count=10):
        self.pops = [Pop(100, 100) for _ in range(pop_count)]  # Start pops at position (100, 100)

    def update(self):
        """Update the simulation, e.g., move the pops."""
        for pop in self.pops:
            pop.move()

    def get_pops(self):
        """Return list of all pops with their positions."""
        return [pop.get_position() for pop in self.pops]
