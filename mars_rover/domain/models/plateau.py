from dataclasses import dataclass

@dataclass
class Plateau:
    width: int
    height: int
    obstacles: set[tuple[int, int]]

    def inside(self, x: int, y: int) -> bool:
        return 0 <= x < self.width and 0 <= y < self.height

    def is_obstacle(self, x: int, y: int) -> bool:
        return (x, y) in self.obstacles