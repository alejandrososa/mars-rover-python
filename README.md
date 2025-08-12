# Mars Rover Python

This project implements the classic **Mars Rover** challenge in Python, following a modular design inspired by hexagonal architecture (Ports and Adapters).

Currently, **only Phase 1** (core domain and main use case) is implemented.  
Phases 2 to 4 are planned and will be developed later.

---

## 🛰 Challenge Description

NASA has deployed a fleet of robotic rovers on a rectangular plateau on Mars.  
Each rover's state consists of:
- Its **position** `(X, Y)`
- Its **compass heading** (`N`, `S`, `E`, `W`)

### Commands:
- `L` → turn left 90°
- `R` → turn right 90°
- `M` → move forward one grid point in the direction it is currently facing.

### Rules:
- The plateau is represented as a grid.  
  - By default: **10×10** (valid coordinates from `0` to `width-1` / `height-1`).
  - The origin `(0,0)` is at the bottom-left corner.
- If a move would take the rover outside the grid, it is ignored.
- Obstacles can be placed on the plateau.  
  - If a rover encounters an obstacle, it stops immediately and outputs a result prefixed with `O:` (status `"obstacle"`).

---

## 📥 Input Format (Phase 1 example)

For **Phase 1**, input is handled programmatically (no CLI yet).  
A plateau, initial position, heading, and command sequence are passed to the `execute()` function.

Example:
```python
plateau = Plateau(5, 5, obstacles=set())
start_position = Position(1, 2)
heading = Direction.N
commands = "LMLMLMLMM"
```

📤 Expected Output

The program returns a dictionary with:
```json
{
  "status": "ok" | "obstacle",
  "x": <final_x>,
  "y": <final_y>,
  "heading": "N" | "E" | "S" | "W"
}