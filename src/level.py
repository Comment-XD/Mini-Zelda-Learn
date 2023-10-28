from src.map import Map
from src.exit import Exit
from src.spawn import Spawn

class Level:
    def __init__(self, name: str, map: Map) -> None:
        """
        The Level class is where the player will interact with mobs, puzzles, etc.

        Args:
            map (Map): the map of the level
        """
        self.name = name
        self.map = map
        self.status = False
        # each level should have a spawning location
        self.spawn = self.find_spawn()
        
        # Level should keep track of where the exit is
        self.exits = self.find_exit()

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
    
    def spawn_player(self, player):
        # find the spawn spot obj and replace it with player, sets the player's position to that spot
        player.x, player.y = self.spawn
        self.map[player.x][player.y] = player
        
    
    def update_status(self):
        pass
        
    def display(self):
        print(f"Level {self.name}")
        for row in self.map:
            for tile in row:
                print(f"{tile} ", end="")
            print("\n")
    
    
    
    
    
        