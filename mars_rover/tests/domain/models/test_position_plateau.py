from mars_rover.domain.models.position import Position
from mars_rover.domain.models.plateau import Plateau

def test_position_holds_coordinates():
    p = Position(3, 4)
    assert p.x == 3
    assert p.y == 4

def test_plateau_inside_true_for_valid_cells():
    board = Plateau(5, 5, obstacles=set())
    assert board.inside(0, 0) is True
    assert board.inside(4, 4) is True

def test_plateau_inside_false_for_out_of_bounds():
    board = Plateau(5, 5, obstacles=set())
    assert board.inside(-1, 0) is False
    assert board.inside(0, 5) is False
    assert board.inside(5, 0) is False

def test_plateau_obstacle_detection():
    board = Plateau(5, 5, obstacles={(2, 2)})
    assert board.is_obstacle(2, 2) is True
    assert board.is_obstacle(1, 1) is False