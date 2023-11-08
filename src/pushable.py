from src.tile import Tile
from src.activator import*

# Could i make player inherit Pushable since it moves? nah...
class Pushable:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

        self.cache = [Tile()]
    
        self.movement = {"up":    (-1,0),
                         "down":  (1,0),
                         "left":  (0,-1),
                         "right": (0,1)}
    
    def get_tile(self, lvl, direction: str) -> Tile:
        
        #adds the movement vector onto the players position vector
        new_pos_x, new_pos_y = (self.x + self.movement[direction][0], self.y + self.movement[direction][1])
        map_dim_x, map_dim_y = (len(lvl.map), len(lvl.map[0]))
        
        # this shit be looking dodo be, ill find a way
        if new_pos_x < map_dim_x and new_pos_y < map_dim_y and new_pos_x >= 0 and new_pos_y >= 0 and (isinstance(lvl.map[new_pos_x][new_pos_y], Tile) or isinstance(lvl.map[new_pos_x][new_pos_y], Activator)):
            return lvl.map[new_pos_x][new_pos_y]

        return None
    
    def push(self, lvl, direction, cache_item):
        tile = self.get_tile(lvl, direction)

            
        if tile is not None:
            lvl.map[self.x][self.y] = self.cache[-1]
                    
            # Removes the previously saved tile
            self.cache.pop()
                    
            # Saves the tile the pushable is going towards
            self.cache.append(cache_item)
                
            # gets the player's new movement vector
            new_pos_x, new_pos_y = self.movement[direction]
                    
            #adds the movement vector onto the pushable position vector
            self.x += new_pos_x
            self.y += new_pos_y
            
            # sets the pushable on the level map
            lvl.map[self.x][self.y] = self
            
            #updates the level's map's floor tile
            lvl.floor_tiles = lvl.find_floor_tiles()
        

# used to be placed on buttons 
class Box(Pushable):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)
    
    def __str__(self) -> str:
        return ">"

# used to fill in holes
class Boulder(Pushable):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)
    
    def __str__(self) -> str:
        return "@"