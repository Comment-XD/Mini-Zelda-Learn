import numpy as np
from src.tile import Tile
from src.lever import Lever
from src.button import Button
from src.exit import Exit
from src.crate import Crate
from src.wall import Wall
from src.item import Item

levers_level_one = [Lever()]


class Map:
    """
    This is a static class with all the different maps for the levels
    """
    
    # find a way to link the lever to the exit 
    level_one = np.array([[Tile(), Wall(), Wall(), Tile()],
                          [Tile(), Crate(Item("Lighter", "It lights Things")), Wall(), Exit(levers_level_one)],
                          [Tile(), levers_level_one[0], Wall(), Tile()],
                          [Tile(), Tile(), Tile(), Tile()]])
    
    level_two = np.array([[None, Wall(), Crate("Loot"), None],
                          [None, Wall(), Wall(), Exit()],
                          [None, Lever(), Wall(), None],
                          [None, None, None, None]])