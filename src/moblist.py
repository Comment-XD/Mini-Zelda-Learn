from src.mob import*
# how can i automate this 
# (everytime we create a new level, we save that name into the levels mob list as a key)

class Mob_List:
    mobs = {"Stone Valley": [Golem("Bob"), Golem("Gerrad"), Golem("Shlok")],
            "Goblins Den": [Goblin("David")]}
    
        