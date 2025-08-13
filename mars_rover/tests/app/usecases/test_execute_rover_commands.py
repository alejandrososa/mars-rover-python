from mars_rover.app.dto import ExecuteCommandsRequest
from mars_rover.app.usecases.execute_rover_commands import execute_rover_commands
from mars_rover.domain.models.position import Position
from mars_rover.domain.models.direction import Direction
from mars_rover.domain.models.plateau import Plateau

def test_example_1_sequence():
    req = ExecuteCommandsRequest(
        plateau=Plateau(5, 5, obstacles=set()),
        start_pos=Position(1, 2),
        heading=Direction.N,
        commands="LMLMLMLMM",
    )
    res = execute_rover_commands(req)
    assert res.status == "ok"
    assert (res.x, res.y, res.heading) == (1, 3, "N")

def test_example_2_sequence():
    req = ExecuteCommandsRequest(
        plateau=Plateau(5, 5, obstacles=set()),
        start_pos=Position(3, 3),
        heading=Direction.E,
        commands="MMRMMRMRRM",
    )
    res = execute_rover_commands(req)
    assert res.status == "ok"
    assert (res.x, res.y, res.heading) == (5, 1, "E")

def test_out_of_bounds_moves_are_ignored():
    # On 1x1 board (valid 0..1), moving north at (1,1) is out of bounds and ignored
    req = ExecuteCommandsRequest(
        plateau=Plateau(1, 1, obstacles=set()),
        start_pos=Position(1, 1),
        heading=Direction.N,
        commands="M",
    )
    res = execute_rover_commands(req)
    assert res.status == "ok"
    assert (res.x, res.y, res.heading) == (1, 1, "N")

def test_stops_when_obstacle_detected():
    req = ExecuteCommandsRequest(
        plateau=Plateau(5, 5, obstacles={(0, 1)}),
        start_pos=Position(0, 0),
        heading=Direction.N,
        commands="MMM",
    )
    res = execute_rover_commands(req)
    assert res.status == "obstacle"
    assert (res.x, res.y, res.heading) == (0, 0, "N")