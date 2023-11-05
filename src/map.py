import numpy as np
from src.tile import Tile
from src.lever import Lever
from src.button import Button
from src.exit import Exit
from src.crate import Crate
from src.wall import Wall
from src.spawn import Spawn

from src.item import*

levers_1 = [Lever()]

class Map:
    """
    This is a static class with all the different maps for the levels
    """
    
    # find a way to link the lever to the exit 
    level_one = [[Tile(), Tile(), Wall(), Tile()],
                [Spawn(), Crate(Item("Lighter")), Wall(), Tile()],
                [Tile(), levers_1[0], Wall(), Tile()],
                [Healing("Goblin Heart"), Tile(), Tile(), Tile()],
                [Tile(), Crate(Item("Lighter")), Exit(levers_1), Tile()]]
    
    level_two = [[Tile(), Wall(), Crate("Loot"), Tile()],
                [Tile(), Wall(), Wall(), Exit()],
                [Tile(), Lever(), Wall(), Tile()],
                [Spawn(), Tile(), Tile(), Tile()]]