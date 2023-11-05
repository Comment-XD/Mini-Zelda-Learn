from src.level import Level
from src.item import Item
from src.tile import Tile
from src.lever import Lever
from src.button import Button
from src.exit import Exit
from src.crate import Crate
from src.wall import Wall
from src.item import*
from src.weapon import*

class Player:
    def __init__(self, name: str, lvl: Level=None, x: int=0, y: int=0) -> None:
        """This is a player class that does adventurous stuff

        Args:
            name (str): name of the player
            lvl (Level, optional): what level the player is currently in
        """
        
        self.x = x
        self.y = y
        
        self.name = name
        
        self.health = 5
        self.maxHealth = 5
        
        
        self.inventory = [Item("Lighter")]
        
        self.weapon_list = [Melee("Sword", 2), None]
        self.weapon_slot = 0
        self.weapon = self.weapon_list[self.weapon_slot]
        self.dmg = self.weapon.dmg
        
        self.cache = [Tile()]
        
        self.lvl = lvl
        
        # controls how fast the player can move around the map 
        # (this is going to be tweaked later as the 
        # player should still have the option to move one tile)
        
        self.speed = 1
        self.movement = {"up":    (-self.speed,0),
                         "down":  (self.speed,0),
                         "left":  (0,-self.speed),
                         "right": (0,self.speed)}
    
    def stats(self):
        print(f"""
{self.name}
---------------------
Health: {self.health}
Max Health: {self.maxHealth}
Equipped Weapon: {self.weapon.name}
Damage: {self.dmg}
Movement Speed: {self.speed}
""")
    
    def weapon_stats(self):
        
        weapon_one_name = self.weapon_list[0].name if self.weapon_list[0] is not None else "Empty"
        weapon_two_name = self.weapon_list[1].name if self.weapon_list[1] is not None else "Empty"
        weapon_one_pointer = ">" if self.weapon_slot == 0 else ""
        weapon_two_pointer = ">" if self.weapon_slot == 1 else ""

        
        weapon_stats = "You are currently equipping Nothing"
        if self.weapon is not None:
            weapon_stats = f"""{self.weapon.name}
> {self.weapon.desc}
---------------------
Durability: {self.weapon.durability}
Range: {self.weapon.range}
Damage: {self.weapon.dmg}
Durability Loss: {self.weapon.durability_loss}"""
        print(f"""
[{weapon_one_pointer}{weapon_one_name}|{weapon_two_pointer}{weapon_two_name}]

{weapon_stats}""")
    
    def inventory_str(self):
        
        # returns the inventory in a string form
        inventory_str = "\nInventory\n"
        for item in self.inventory:
            inventory_str += f"{item.name}: {item.count}\n> {item.desc}\n"

        return inventory_str
    
    def consumables_str(self):
        
        # returns the inventory in a string form
        consumable_str = "Consumables\n"
        for item in self.inventory:
            if isinstance(item, Consumable):
                consumable_str += f"{item.name}: {item.count}\n> {item.desc}\n"

        return consumable_str
        
    def is_dead(self) -> bool:
        #returns a boolean value depending on if the player's health is less than equal to 0
        return self.health <= 0
    
    def find_weapon(self, name):
        for weapon in self.weapon_list:
            if name.lower() == weapon.name.lower():
                return weapon
            
        return None
    
    def add_weapon(self, weapon: Weapon):
        #checks to see if there is any empty space, 
        # if so replace that empty space with the weapon you want to add
        
        if None in self.weapon_list:
            self.weapon_list.remove(None)
            self.weapon_list.append(weapon)
            
    def remove_weapon(self, name: str):
        # checks to see if the weapon exists
        weapon = self.find_weapon(name)
        
        # if so, remove the weapon and replace it with a None
        if weapon is not None:
            self.weapon_list.remove(weapon)
            self.weapon_list.append(None)
            
            self.weapon = self.weapon_list[self.weapon_slot]
    
    def switch_weapon_slot(self):
        # switches the weapon_slot
        match self.weapon_slot:
            case 0: self.weapon_slot = 1
            case 1: self.weapon_slot = 0

        self.weapon = self.weapon_list[self.weapon_slot]
    
    def attack(self, mob) -> None:
        # just decreases the mobs health, can be improved later on
        
        # later on we are going to add range of the weapon, 
        # need to use distance formula to determine if the mob is within range of the player, 
        # if it is, add an option to the menu for attack specifically
        # the same is applied for mobs (I will test this mechanism in a seperate python file)
        
        #decreases the weapon durability after each attack
        if self.weapon is not None:
            self.weapon.durability -= self.weapon.durability_loss
            
            #checks to see if the weapon is broken, if it is replace that weapon with a None
            if self.weapon.is_broken():
                print(f"{self.weapon.name} has broken!")
                self.weapon_list[self.weapon_slot] = None
            
            mob.health -= self.dmg
        else:
            print("\n You currently are equipping nothing")
    
    def find_item(self, item_to_find: Item) -> Item: 
        # this way of finding the item is so ass
        
        item_type = type(item_to_find) #determines whether the item_to_find parameter is a string
        if item_type == str:
            
            # iterates through the inventory
            for item in self.inventory:
                # if the item's name is equal to the item you want to find, return the item
                if item.name.lower() == item_to_find.lower():
                    return item
        else:
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
            item.count -= 1
            
            if item.count <= 0:
                self.inventory.remove(item)
            
    def add_item(self, item_to_add: Item) -> None:
        # checks to see if there is any redundant items
        item = self.find_item(item_to_add)
        if item is not None:
            
            #if there is, just increase the count of the item by one (this can change later)
            item.count += item_to_add.count
        
        # if the item does not appear in the inventory, just add it into the inventory 
        # (eventually we need to set max inventory limits)
        else:
            self.inventory.append(item_to_add)
        
    def loot(self, obj) -> None:
         
        # for every item in the crates, go through the add_items method
        for item in obj.loot:
            if isinstance(item, Item):
                self.add_item(item)
            
            if isinstance(item, Weapon):
                self.add_weapon(item)
    
    def consume(self, item_to_consume: str):
        item = self.find_item(item_to_consume)
        print(item.__str__())
        if isinstance(item, Healing):
            self.health += item.heal
            self.remove_item(item)
            
            if self.health > self.maxHealth:
                self.health = self.maxHealth
            
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
            # there is probably a better method to get custom strings instead a bunch of if statements
            
            if isinstance(tile, Tile):
                menu_option_str += f"{key}: Move {key}\n"
            if isinstance(tile, Lever):
                menu_option_str += f"{key}: Lever Status -> {tile.status}\n"
            if isinstance(tile, Button):
                menu_option_str += f"{key}: Button Status -> {tile.status}\n"
            if isinstance(tile, Exit):
                menu_option_str += f"{key}: Exit Status -> {tile.status}\n"
            if isinstance(tile, Item):
                menu_option_str += f"{key}: Pickup {tile.name}\n"
            if isinstance(tile, Crate):
                menu_option_str += f"{key}: Crate\n"
            if isinstance(tile, Player):
                menu_option_str += f"{key}: {tile.name}: Health->{tile.health} Dmg->{tile.dmg}\n"
        
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
            # if the direction is stay, do nothing (this is not neccesary)
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
                    self.lvl.status = True
            
            if isinstance(tile, Item):
                print(tile.name)
                self.add_item(tile)
                
                self.move(direction, Tile())
                
            if isinstance(tile, Crate):
                self.loot(tile)
                self.move(direction, Tile())
                
            if isinstance(tile, Player):
                self.attack(tile) 
                
                if tile.is_dead():
                    self.loot(tile)
                    self.move(direction, Tile())
                               
            # if player hits the ending mark, player should go to the next lvl
            # but how...
                
    def __str__(self) -> str:
        return "*"
    