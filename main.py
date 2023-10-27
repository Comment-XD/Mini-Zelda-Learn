from src.level import Level
from src.map import Map
from src.game import Game
from player import Player

level_one = Level(Map.level_one)
level_two = Level(Map.level_two)

game = Game([level_one, level_two])

name = input("What do you want to name your character?\nName: ")
player = Player(name)
print("Welcome to Mini-Link!")

#starts the game
game.start(player)

while True:
    # Generates Player Actions
    user_input = input(
"""
Player Options:
---------------
1. Move
2. Inventory
User Input: """)
    match user_input:
        case "1":
           move_option = input(
"""
Which direction you want to move?
-up
-down
-left
-right
stay
""")
           player.move(move_option)
        case "2":
            print(player.inventory_str())
    player.lvl.display()
