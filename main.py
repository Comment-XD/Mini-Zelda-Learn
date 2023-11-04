from src.level import Level
from src.map import Map
from src.game import Game
from src.player import Player

level_one = Level("one", Map.level_one)
level_two = Level("two", Map.level_two)

game = Game([level_one, level_two])

name = input("What do you want to name your character?\nName: ")
player = Player(name)
print("Welcome to Mini-Link!")

#starts the game
game.start(player)

while True:
    player.lvl.display()
    # Generates Player Actions
    user_input = input(
"""
Player Options:
---------------
1. Move
2. Inventory
3. Consume Item
4. Player Stats 
5. Weapon Stats

User Input: """)
    match user_input:
        case "1":
            actions = input(
f"""
What actions do you want to do?
{player.menu()}
""")        
            player.action(actions)
            
            if player.lvl.status:
                game.next_level(player)
            
          
        case "2":
            print(player.inventory_str())
        
        case "3":
            item = input(
f"""
Which Item do you want to consume?
{player.consumables_str()}
""")  
            player.consume(item)
        case "4":
            player.stats()
        
        case "5":
            player.weapon_stats()
            
    
