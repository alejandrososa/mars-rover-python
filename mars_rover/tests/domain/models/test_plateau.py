from mars_rover.domain.models.plateau import Plateau

def test_inside_true_for_valid_cells():
    board = Plateau(5, 5, obstacles=set())
    assert board.inside(0, 0)
    assert board.inside(4, 4)

def test_inside_false_for_out_of_bounds():
    board = Plateau(5, 5, obstacles=set())
    assert not board.inside(-1, 0)
    assert not board.inside(0, 5)

def test_obstacle_detection():
    board = Plateau(5, 5, obstacles={(2, 2)})
    assert board.is_obstacle(2, 2)
    assert not board.is_obstacle(1, 1)