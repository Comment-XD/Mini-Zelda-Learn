from src.level import Level
from src.item import Item
from src.tile import Tile

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
    
    def find_item(self, item_to_find) -> Item: 
        # iterates through the inventory
        for item in self.inventory:
            # if the item's name is equal to the item you want to find, return the item
            if item.name == item_to_find.name:
                return item
        
        return None
    
    def remove_item(self, item_to_remove) -> None:
        # checks to see if there is an item to remove
        item = self.find_item(item_to_remove)
        
        if item is not None:
            # simply removes the item from the inventory
            self.inventory.remove(item)
            
        
    def add_item(self, item_to_add) -> None:
        # checks to see if there is any redundant items
        item = self.find_item(item_to_add)
        if item is not None:
            
            #if there is, just increase the count of the item by one (this can change later)
            item.count += 1
        
        # if the item does not appear in the inventory, just add it into the inventory 
        # (eventually we need to set max inventory limits)
        self.inventory.append(item)
    
    def open_crate(self, crate):
         
        # for every item in the crates, go through the add_items method
        for item in crate.loot:
            self.add_item(item)
    
    def move(self, direction):
        # sets the player's original position as "None"
        self.lvl.map[(self.x, self.y)] = Tile()
        
        # gets the player's new movement vector
        new_pos_x, new_pos_y = self.movement[direction]
        
        #adds the movement vector onto the players position vector
        self.x += new_pos_x
        self.y += new_pos_y
        
        
        # sets the player's new position as player
        self.lvl.map[(self.x, self.y)] = self
    
    def __str__(self) -> str:
        return "*"
    