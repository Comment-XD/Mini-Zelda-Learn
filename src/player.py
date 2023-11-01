from src.level import Level
from src.item import Item
from src.tile import Tile
from src.lever import Lever
from src.button import Button
from src.exit import Exit
from src.crate import Crate
from src.wall import Wall
from src.item import Item

class Player:
    def __init__(self, name: str, lvl: Level=None) -> None:
        """This is a player class that does adventurous stuff

        Args:
            name (str): name of the player
            lvl (Level, optional): what level the player is currently in
        """
        
        self.x = 0
        self.y = 0
        
        self.name = name
        self.health = 5
        self.dmg = 1
        
        self.inventory = [Item("Lighter", "its a Lighter")]
        self.weapon_list = []
        self.weapon_slot = 0
        
        self.cache = [Tile()]
        
        self.lvl = lvl
        
        self.movement = {"up":    (-1,0),
                         "down":  (1,0),
                         "left":  (0,-1),
                         "right": (0,1),
                         "stay":  (0,0)}
        
    def inventory_str(self):
        
        # returns the inventory in a string form
        inventory_str = "\nInventory\n"
        for item in self.inventory:
            inventory_str += f"{item.name}: {item.count}"

        return inventory_str + "\n"
        
    def is_dead(self) -> bool:
        #returns a boolean value depending on if the player's health is less than equal to 0
        return self.health <= 0
    
    def attack(self, mob) -> None:
        # just decreases the mobs health, can be improved later on
        mob.health -= self.dmg
    
    def find_item(self, item_to_find: Item) -> Item: 
        # iterates through the inventory
        for item in self.inventory:
            # if the item's name is equal to the item you want to find, return the item
            if item.name == item_to_find.name:
                return item
        
        return None
    
    def remove_item(self, item_to_remove: Item) -> None:
        # checks to see if there is an item to remove
        item = self.find_item(item_to_remove)
        
        if item is not None:
            # simply removes the item from the inventory
            self.inventory.remove(item)
            
    def add_item(self, item_to_add: Item) -> None:
        # checks to see if there is any redundant items
        item = self.find_item(item_to_add)
        if item is not None:
            
            #if there is, just increase the count of the item by one (this can change later)
            item.count += 1
        
        # if the item does not appear in the inventory, just add it into the inventory 
        # (eventually we need to set max inventory limits)
        else:
            self.inventory.append(item)
        
    def open_crate(self, crate: Crate) -> None:
         
        # for every item in the crates, go through the add_items method
        for item in crate.loot:
            self.add_item(item)
        
        #sets the crate loot to empty
        crate.loot = []
    
    def get_tile(self, direction: str) -> Tile:
        
        #adds the movement vector onto the players position vector
        new_pos_x, new_pos_y = (self.x + self.movement[direction][0], self.y + self.movement[direction][1])
        map_dim_x, map_dim_y = (len(self.lvl.map), len(self.lvl.map[0]))
        
        # this shit be looking dodo be, ill find a way
        if new_pos_x < map_dim_x and new_pos_y < map_dim_y and new_pos_x >= 0 and new_pos_y >= 0 and not isinstance(self.lvl.map[new_pos_x][new_pos_y], Wall):
            return self.lvl.map[new_pos_x][new_pos_y]

        return None
        
    def menu(self) -> str:
        menu_option_str = "stay: do nothing\n"
        
        # gets the keys from the movement dictionary
        for key in self.movement.keys():
            
            # gets the tile using the get_tile method
            tile = self.get_tile(key)
            
            #checks which class tile belongs to and sets a string to that option it sees
            if isinstance(tile, Tile):
                menu_option_str += f"{key}: move {key}\n"
            if isinstance(tile, Lever):
                menu_option_str += f"{key}: Lever Status -> {tile.status}\n"
            if isinstance(tile, Button):
                menu_option_str += f"{key}: Button Status -> {tile.status}\n"
            if isinstance(tile, Exit):
                menu_option_str += f"{key}: Exit Status -> {tile.status}\n"
            if isinstance(tile, Crate):
                menu_option_str += f"{key}: Crate\n"
        
        return menu_option_str
    
    def key_options(self) -> list[str]:
        # returns a list of keys that can be used for the move method
        key_options = []
        for key in self.movement.keys():
            tile = self.get_tile(key)
            if tile is not None:
                key_options.append(key)

        return key_options
    
    def move(self, direction: str, cache_item) -> None:
        
        self.lvl.map[self.x][self.y] = self.cache[-1]
                
        # Removes the previously saved tile
        self.cache.pop()
                
        # Saves the tile you are going towards
        self.cache.append(cache_item)
                
        # gets the player's new movement vector
        new_pos_x, new_pos_y = self.movement[direction]
                
        #adds the movement vector onto the players position vector
        self.x += new_pos_x
        self.y += new_pos_y
        
        # sets the player on the level map
        self.lvl.map[self.x][self.y] = self
    
    def action(self, direction: str) -> None:
        if direction == "stay":
            # if the direction is stay, do nothing
            return
        
        if direction in self.key_options():
            
            tile = self.get_tile(direction)
            
            if isinstance(tile, Tile):
                self.move(direction, tile)
                
            if isinstance(tile, Lever):
                tile.status = True # should set the lever's activated state to True
                for exit in self.lvl.exits:
                    exit.update_status()
                
            if isinstance(tile, Exit):
                if tile.status:
                    self.move(direction, Tile())
                    print("testing")
                    self.lvl.status = True
                
            if isinstance(tile, Crate):
                self.open_crate(tile)
                self.move(direction, Tile())
            
            # if player hits the ending mark, player should go to the next lvl
            # but how...
                
    def __str__(self) -> str:
        return "*"
    