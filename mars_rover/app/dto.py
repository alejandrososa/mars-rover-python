from dataclasses import dataclass
from mars_rover.domain.models.direction import Direction
from mars_rover.domain.models.position import Position
from mars_rover.domain.models.plateau import Plateau

@dataclass(frozen=True)
class ExecuteCommandsRequest:
    plateau: Plateau
    start_pos: Position
    heading: Direction
    commands: str  # sequence like "LMLMLMLMM"

@dataclass(frozen=True)
class ExecuteCommandsResponse:
    status: str  # "ok" | "obstacle"
    x: int
    y: int
    heading: str  # "N" | "E" | "S" | "W"