from src.map import Map

class Level:
    def __init__(self, map: Map) -> None:
        """
        The Level class is where the player will interact with mobs, puzzles, etc.

        Args:
            map (Map): the map of the level
        """
        self.map = map
        self.status = False
    
    def spawn_player(self, player):
        # find the spawn spot obj and replace it with player, sets the player's position to that spot
        self.map[(player.x, player.y)] = player
    
    def update_status(self):
        pass
        
    def display(self):
        for row in self.map:
            for tile in row:
                print(f"{tile} ", end="")
            print("\n")
    
    
    
    
    
        