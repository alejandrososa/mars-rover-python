from mars_rover.domain.models.position import Position
from mars_rover.domain.models.plateau import Plateau

def test_position_holds_coordinates():
    p = Position(3, 4)
    assert p.x == 3
    assert p.y == 4

def test_plateau_inside_true_for_valid_cells():
    board = Plateau(5, 5, obstacles=set())
    assert board.inside(0, 0) is True
    assert board.inside(5, 5) is True  # inclusive upper bound

def test_plateau_inside_false_for_out_of_bounds():
    board = Plateau(5, 5, obstacles=set())
    assert board.inside(-1, 0) is False
    assert board.inside(0, 6) is False  # was 5; now 6
    assert board.inside(6, 0) is False  # was 5; now 6

def test_plateau_detects_obstacles():
    board = Plateau(5, 5, obstacles={(2, 2)})
    assert board.is_obstacle(2, 2) is True
    assert board.is_obstacle(1, 1) is False