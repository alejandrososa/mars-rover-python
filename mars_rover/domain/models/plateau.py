from dataclasses import dataclass

@dataclass
class Plateau:
    # Inclusive maximum coordinates (e.g., max_x=5 allows 0..5)
    max_x: int
    max_y: int
    obstacles: set[tuple[int, int]]

    def inside(self, x: int, y: int) -> bool:
        """Return True if (x, y) is within [0..max_x] x [0..max_y]."""
        return 0 <= x <= self.max_x and 0 <= y <= self.max_y

    def is_obstacle(self, x: int, y: int) -> bool:
        """Return True if there is an obstacle at (x, y)."""
        return (x, y) in self.obstacles

    @staticmethod
    def factory_default() -> "Plateau":
        """Create a default 10x10 plateau (valid coords 0..9)."""
        return Plateau(9, 9, obstacles=set())