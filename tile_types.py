from typing import Tuple
import numpy as np # type: ignore

# Tile graphics structured type compatible with Console.tiles_rgb.
graphic_dt = np.dtype(
    [
        ("ch", np.int32),  # Unicode codepoint.
        ("fg", "3B"),  # 3 unsigned bytes, for RGB colors.
        ("bg", "3B"),
    ]
)

#Tile strut for used static tile data
tile_dt = np.dtype(
    [
        ("walkable", np.bool_),  # True if this tile can be walked over.
        ("transparent", np.bool_),  # True if this tile doesn't block FOV.
        ("dark", graphic_dt),  # Graphic for when the tile is not in FOV.
    ]
)

def new_tile(
        *, #Enforce keyword-only arguments
        walkable: int,
        transparent: int,
        dark: tuple[int, Tuple[int, int, int], Tuple[int, int, int]], # dark - (characterr, foreground, background)
) -> np.ndarray:
    """Helper function to create a new tile."""
    return np.array((walkable, transparent, dark), dtype=tile_dt)


floor = new_tile(
    walkable=True, transparent=True, dark=(ord(" "), (255, 255, 255), (50, 50, 150)),
)

wall = new_tile(
    walkable=False, transparent=False, dark=(ord(" "), (255, 255, 255), (0, 0, 100)),
)