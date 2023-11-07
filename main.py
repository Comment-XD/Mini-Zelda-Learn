from src.level import Level
from src.map import Map
from src.game import Game
from src.player import Player
from src.item import*
import os

level_one = Level("Stone Valley", Map.level_one)
level_two = Level("Goblins Den", Map.level_two)

game = Game([level_one, level_two])

name = input("What do you want to name your character?\nName: ")
player = Player(name)
print("Welcome to Mini-Link!\n")

#starts the game
game.start(player)

# spawns the mobs, at the beginning
player.lvl.spawn_mobs()

while not game.status:
    player.lvl.display()
    # Generates Player Actions
    user_input = input(
f"""
{player.name}'s Options:
---------------
1. Move
2. Inventory
3. Consume Item
4. Player Stats 
5. Weapon Stats
6. Info Section

User Input: """)
    match user_input:
        case "1":
            
            # this is to apply the effects of the player and check how long it lasts
            player.effects_timer(1)
            
            actions = input(
f"""
What actions do you want to do?
{player.menu()}
""")        
            player.action(actions)
            
            if player.lvl.status:
                game.next_level(player)
            
            player.lvl.mob_pathfinding(player)
            
        case "2":
            print(player.inventory_str())
            
            inventory_choice = input("""Enter Nothing to skip>>>
1. Drop Item
Answer: """)
            match inventory_choice:
                case "1":
                    item_name = input("\nWhat item do you want to remove? ")
                    player.remove_item(item_name)
            input("Press Any Button to Continue...")
            os.system('cls')
        
        case "3":
            item = input(
f"""
Which Item do you want to consume?
{player.consumables_str()}
""")        
            player.consume(item)
        case "4":
            player.stats()
            input("Press Enter to Continue...")
            os.system('cls')
        
        case "5":
            player.weapon_stats()
            weapon_choice = input("""
Enter Nothing to skip>>>
1. Switch Weapon
2. Drop Weapon
Answer: """)
            match weapon_choice:
                case "1":
                    player.switch_weapon_slot()
                case "2":
                    weapon_name = input("\nWhat weapon do you want to remove? ")
                    player.remove_weapon(weapon_name)
                    
            input("Press Enter to Continue...")
            os.system('cls')
        case "6":
            print("""
Info Section
------------
>Objective is to unlock levers (/) which allow you to go through Gates (~)
Going through gates allow you to access the next level!

* - Player
Letters - Mobs Ex. (G- Golemn)
$ - Crates
# - Walls
~ - Gate
/ - Levers
+ - Healing Items
= - Strength Items
""")

            input("Press Enter to Continue...")
            os.system('cls')
    
    game.update_status()
print("You Win!")