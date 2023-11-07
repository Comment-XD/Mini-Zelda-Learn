import random
import copy

from src.map import Map
from src.exit import Exit
from src.spawn import Spawn
from src.tile import Tile
from src.moblist import Mob_List

class Level:
    def __init__(self, name: str, map: Map, difficulty=1) -> None:
        """
        The Level class is where the player will interact with mobs, puzzles, etc.

        Args:
            map (Map): the map of the level
        """
        self.name = name
        self.map = map
        
        self.difficulty = difficulty
        self.status = False
        # each level should have a spawning location
        self.spawn = self.find_spawn()
        
        # Level should keep track of where the exit is
        self.exits = self.find_exit()
        self.floor_tiles = self.find_floor_tiles()
        
        self.mob_list = Mob_List.mobs[name]
        self.active_mob_list = []
        self.total_active_mobs = difficulty

    def find_spawn(self):
        for i, row in enumerate(self.map):
            for j, tile in enumerate(row):
                if isinstance(tile, Spawn):
                    return (i, j)
        
    def find_exit(self):
        exits = []
        
        # this shit ugly as hell
        for row in self.map:
            for tile in row:
                if isinstance(tile, Exit):
                    exits.append(tile)
        
        return exits

    def find_floor_tiles(self):
        # needs to be dynamic as the player moves around and screws up the 
        
        # Returns all the floor tiles of the level
        floor_tiles = []
        
        # this shit ugly as hell
        for i, row in enumerate(self.map):
            for j, tile in enumerate(row):
                if isinstance(tile, Tile):
                    floor_tiles.append((i,j))
        
        return floor_tiles

    
    def spawn_player(self, player):
        # find the spawn spot obj and replace it with player, sets the player's position to that spot
        player.x, player.y = self.spawn
        self.map[player.x][player.y] = player
    
    def spawn_mobs(self):
        copy_floor_tiles = copy.deepcopy(self.floor_tiles)
        self.total_active_mobs = self.difficulty
        
        for _ in range(self.difficulty):
            
            mob = copy.deepcopy(random.choice(self.mob_list))
            
            self.active_mob_list.append(mob)
            
            mob_spawn = random.choice(copy_floor_tiles)
            mobSpawnX, mobSpawnY = mob_spawn
            
            # sets the mob's x and y positions and the level itself
            mob.x = mobSpawnX
            mob.y = mobSpawnY
            mob.lvl = self
            
            self.map[mobSpawnX][mobSpawnY] = mob
            copy_floor_tiles.remove(mob_spawn)
     
    def mob_pathfinding(self, player):
        for mob in self.active_mob_list:
            mob.follow_player(player)
            mob.effects_timer(1)
            
    def display(self):
        
        # displays the level into a string form
        print(f"{self.name}") 
        for row in self.map:
            for tile in row:
                print(f"{tile} ", end="")
            print("\n")       