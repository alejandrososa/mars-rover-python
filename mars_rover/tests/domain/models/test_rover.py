from mars_rover.domain.models.rover import Rover
from mars_rover.domain.models.position import Position
from mars_rover.domain.models.direction import Direction

def test_rover_holds_position_and_direction():
    r = Rover(pos=Position(1, 2), dir=Direction.N)
    assert r.pos.x == 1 and r.pos.y == 2
    assert r.dir == Direction.N