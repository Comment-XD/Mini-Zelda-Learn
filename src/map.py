import numpy as np

from src.tile import Tile
from src.exit import Exit
from src.crate import Crate
from src.wall import Wall
from src.spawn import Spawn

from src.pushable import*
from src.activator import*

from src.item import*

pushables_1 = [Boulder(3,1)]
buttons_1 = [Hole(pushables_1)]

class Map:
    """
    This is a static class with all the different maps for the levels
    """
    
    # find a way to link the lever to the exit 
    level_one = [[Tile(), Tile(), Wall(), Tile()],
                [Spawn(), Tile(), Wall(), Tile()],
                [Tile(), buttons_1[0], Wall(), Tile()],
                [Tile(), pushables_1[0], Tile(), Tile()],
                [Tile(), Crate(Item("Lighter")), Exit(buttons_1), Tile()]]
    
    level_two = [[Tile(), Wall(), Crate("Loot"), Tile()],
                [Tile(), Wall(), Wall(), Exit()],
                [Tile(), Lever(), Wall(), Tile()],
                [Spawn(), Tile(), Tile(), Tile()]]