from mars_rover.app.dto import ExecuteCommandsRequest, ExecuteCommandsResponse
from mars_rover.domain.models.rover import Rover
from mars_rover.domain.services.navigator import Navigator

def execute_rover_commands(req: ExecuteCommandsRequest) -> ExecuteCommandsResponse:
    """
    Executes a sequence of rover commands (L/R/M) on a given plateau.

    - Ignores moves that go out of bounds
    - Stops on first obstacle and reports current position and heading
    """
    nav = Navigator(req.plateau)
    rover = Rover(pos=req.start_pos, dir=req.heading)

    for c in req.commands:
        if c == "L":
            rover = nav.turn_left(rover)
        elif c == "R":
            rover = nav.turn_right(rover)
        elif c == "M":
            moved, r2 = nav.move(rover)
            if moved is None:
                return ExecuteCommandsResponse(
                    status="obstacle",
                    x=rover.pos.x,
                    y=rover.pos.y,
                    heading=rover.dir.value,
                )
            elif moved is True:
                rover = r2
            # If moved is False (out of bounds), ignore and continue
        # Ignore any unknown commands

    return ExecuteCommandsResponse(
        status="ok",
        x=rover.pos.x,
        y=rover.pos.y,
        heading=rover.dir.value,
    )