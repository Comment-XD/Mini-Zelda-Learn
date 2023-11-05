import random

from src.level import Level
from src.player import Player
from src.weapon import*
from src.item import*

class Mob(Player):
    def __init__(self, name: str, lvl: Level = None, x: int=0, y: int=0) -> None:
        super().__init__(name, lvl, x, y)
        self.loot = []
        
    
    def follow_player(self):
        # Later on we can add a pathfinder where the mobs will go towards the players
        # coming soon...
        pass
        
class Golem(Mob):
    def __init__(self, name: str, lvl: Level = None, x: int=0, y: int=0) -> None:
        super().__init__(name, lvl, x, y)
        
        self.health = 5
        self.weapon_list = [Melee("Hammer", 5)]
        
        # randomly choices an item for the player to obtain from the mob
        self.loot = [Healing("Rock Crystals", count=2)] + self.weapon_list
    
    def __str__(self) -> str:
        return "G"

class Goblin(Mob):
    def __init__(self, name: str, lvl: Level = None, x: int=0, y: int=0) -> None:
        super().__init__(name, lvl, x, y)
        self.health = 2
        self.weapon_list = [Melee("Dagger", 2)]
        
        # randomly choices an item for the player to obtain from the mob
        self.loot = random.choice([Healing("Goblin Heart", count=1)] + self.weapon_list)
        