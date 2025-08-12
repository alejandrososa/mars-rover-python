from typing import Tuple, Optional
from mars_rover.domain.models.plateau import Plateau
from mars_rover.domain.models.rover import Rover
from mars_rover.domain.models.position import Position
from mars_rover.domain.models.direction import Direction

# Step offsets for each direction (dx, dy)
_STEP = {
    Direction.N: (0, 1),
    Direction.E: (1, 0),
    Direction.S: (0, -1),
    Direction.W: (-1, 0),
}

class Navigator:
    """Encapsulates the logic for turning and moving a rover on a Plateau."""

    def __init__(self, plateau: Plateau):
        self.plateau = plateau

    def turn_left(self, rover: Rover) -> Rover:
        """Return a new Rover instance after turning left 90°."""
        return Rover(pos=rover.pos, dir=rover.dir.left())

    def turn_right(self, rover: Rover) -> Rover:
        """Return a new Rover instance after turning right 90°."""
        return Rover(pos=rover.pos, dir=rover.dir.right())

    def move(self, rover: Rover) -> Tuple[Optional[bool], Rover]:
        """
        Move the rover forward by one cell if possible.

        Returns:
            Tuple:
                - True  -> moved successfully
                - False -> out of bounds (ignored move)
                - None  -> obstacle ahead (movement blocked)
            Rover: updated rover instance or the same if no movement
        """
        dx, dy = _STEP[rover.dir]
        nx, ny = rover.pos.x + dx, rover.pos.y + dy

        if not self.plateau.inside(nx, ny):
            return False, rover  # Out of bounds, ignore movement

        if self.plateau.is_obstacle(nx, ny):
            return None, rover  # Obstacle ahead, do not move

        return True, Rover(pos=Position(nx, ny), dir=rover.dir)