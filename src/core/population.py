# src/core/pop.py

class Pop:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        """Basic random movement logic for pop."""
        import random
        self.x += random.choice([-1, 1])
        self.y += random.choice([-1, 1])

    def get_position(self):
        return (self.x, self.y)
