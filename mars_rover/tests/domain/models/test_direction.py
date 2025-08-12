from mars_rover.domain.models.direction import Direction

def test_turn_left_cycle():
    assert Direction.N.left() == Direction.W
    assert Direction.W.left() == Direction.S
    assert Direction.S.left() == Direction.E
    assert Direction.E.left() == Direction.N

def test_turn_right_cycle():
    assert Direction.N.right() == Direction.E
    assert Direction.E.right() == Direction.S
    assert Direction.S.right() == Direction.W
    assert Direction.W.right() == Direction.N