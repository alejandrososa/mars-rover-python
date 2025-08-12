from mars_rover.domain.models.direction import Direction
from mars_rover.domain.models.position import Position
from mars_rover.domain.models.plateau import Plateau
from mars_rover.domain.models.rover import Rover
from mars_rover.domain.services.navigator import Navigator


def test_turns_left_and_right():
    """Turning left/right should only change heading, not position."""
    nav = Navigator(Plateau(5, 5, obstacles=set()))
    r = Rover(Position(0, 0), Direction.N)

    r_left = nav.turn_left(r)
    r_right = nav.turn_right(r)

    assert r_left.dir == Direction.W
    assert r_right.dir == Direction.E
    assert r_left.pos == r.pos == r_right.pos  # position is unchanged


def test_move_forward_basic():
    """Moving forward should advance one cell in the current heading."""
    nav = Navigator(Plateau(5, 5, obstacles=set()))
    r = Rover(Position(0, 0), Direction.N)

    moved, r2 = nav.move(r)

    assert moved is True
    assert r2.pos == Position(0, 1)
    assert r2.dir == Direction.N  # heading is unchanged


def test_move_ignored_when_out_of_bounds():
    """If the next cell is out of bounds, movement is ignored (returns False)."""
    nav = Navigator(Plateau(2, 2, obstacles=set()))  # valid coords: 0..1
    r = Rover(Position(1, 1), Direction.N)

    moved, r2 = nav.move(r)

    assert moved is False
    assert r2 is r  # same instance, no movement


def test_move_stops_on_obstacle():
    """If an obstacle is ahead, movement is blocked (returns None)."""
    nav = Navigator(Plateau(5, 5, obstacles={(0, 1)}))
    r = Rover(Position(0, 0), Direction.N)

    moved, r2 = nav.move(r)

    assert moved is None
    assert r2 is r  # same instance, no movement