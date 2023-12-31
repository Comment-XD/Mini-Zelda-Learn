import random
import numpy as np

# from src.level import Level
from src.player import Player
from src.tile import Tile
from src.weapon import*
from src.item import*

class Mob(Player):
    
    def __init__(self, name: str, lvl=None, x: int=0, y: int=0) -> None:
        super().__init__(name, lvl, x, y)
        self.loot = []
    
    def drop_loot(self, player: Player) -> None:
        player.loot(self)
        # This is eventually for if the mob were to die form effects 
        
    def follow_player(self, player: Player) -> None:
        playerX = player.x
        playerY = player.y
        
        
        best_key = list(self.movement.keys())[0]
        min_distance = np.sqrt((playerX - self.x)**2 + (playerY - self.y)**2)
        
        # goes through every single direction, 
        # (take its position and calculate the distance between the mob's position and the player's position)
        for key in self.movement.keys():

            tile = self.get_tile(key)
            
            changeX, changeY = self.movement[key]
            
            if isinstance(tile, Player):
                # if the bot sees the player, attack the player
                self.attack(player)
                return
            
            if isinstance(tile, Tile):
                # calculates the distance between the player and the person
                
                distance = np.sqrt((playerX - (self.x + changeX))**2 + (playerY - (self.y + changeY))**2)
                
                #atrocious, i will fix this eventually
                
                # checks to see if the distance is lower than the previous min_distance 
                # if so, set best key to key
                if min_distance > distance:
                    best_key = key
                    min_distance = distance
                
                # print(f"{key}: {min_distance}")
                # print(f"{key} {tile.__str__()}")

        # checks to make sure if the best key is actually a tile
        if not isinstance(self.get_tile(best_key), Tile):
            return
        
        self.move(best_key, Tile())  
       
class Golem(Mob):
    def __init__(self, name: str, lvl=None, x: int=0, y: int=0) -> None:
        super().__init__(name, lvl, x, y)
        
        self.health = 4
        
        self.effects = []
        self.weapon_list = [Melee("Hammer", 3)]
        
        self.weapon_slot = 0
        self.weapon = self.weapon_list[self.weapon_slot]
        self.dmg = self.weapon.dmg
        
        self.loot = [Healing("Rock Crystals", 2, 2)] + self.weapon_list
    
    def __str__(self) -> str:
        return "G"

class Goblin(Mob):
    def __init__(self, name: str, lvl=None, x: int=0, y: int=0) -> None:
        super().__init__(name, lvl, x, y)
        self.health = 2
        
        self.effects = []
        self.weapon_list = [Melee("Dagger", 2)]
        
        self.weapon_slot = 0
        self.weapon = self.weapon_list[self.weapon_slot]
        self.dmg = self.weapon.dmg
        
        self.loot = [Healing("Goblin Heart", count=1)] + self.weapon_list
    
    def __str__(self) -> str:
        return "N"

class Fire_Emblems(Mob):
    def __init__(self, name: str, lvl=None, x: int=0, y: int=0) -> None:
        super().__init__(name, lvl, x, y)
        self.health = 2
        
        self.effects = []
        self.weapon_list = [Melee("Dagger", 2)]
        
        self.weapon_slot = 0
        self.weapon = self.weapon_list[self.weapon_slot]
        self.dmg = self.weapon.dmg
        
        self.loot = [Item("Lighter", 1)] + self.weapon_list
    
    def __str__(self) -> str:
        return "N"
        