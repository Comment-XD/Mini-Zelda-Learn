import numpy as np
from src.tile import Tile
from src.lever import Lever
from src.button import Button
from src.exit import Exit
from src.crate import Crate
from src.wall import Wall
from src.item import Item
from src.spawn import Spawn

levers_1 = [Lever(), Lever()]


class Map:
    """
    This is a static class with all the different maps for the levels
    """
    
    # find a way to link the lever to the exit 
    level_one = [[Tile(), levers_1[0], Wall(), Tile()],
                [Spawn(), Crate(Item("Lighter", "It lights Things")), Wall(), Tile()],
                [Tile(), levers_1[1], Wall(), Tile(), Tile()],
                [Tile(), Tile(), Tile(), Tile(), Tile(), Tile()],
                [Tile(), Crate(Item("Lighter", "It lights Things")), Exit(levers_1), Tile(), Tile()],
                [Tile(), Tile(), Tile(), Tile()]]
    
    level_two = [[Tile(), Wall(), Crate("Loot"), Tile()],
                [Tile(), Wall(), Wall(), Exit()],
                [Tile(), Lever(), Wall(), Tile()],
                [Spawn(), Tile(), Tile(), Tile()]]