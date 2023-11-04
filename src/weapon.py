from src.desc import Desc

class Weapon:
    def __init__(self, name: str, dmg: int) -> None:
        """Class that is used to attack players or mobs

        Args:
            name (str): name of the weapon
        """
        self.name = name
        self.desc = Desc.weapon[name]
        
        self.dmg = dmg
        self.durability = 100
        self.broken = False
        
class Melee(Weapon):
    def __init__(self, name: str, dmg: int) -> None:
        super().__init__(name, dmg)
        self.durability_loss = 5
        self.range = 2
    
    def is_broken(self):
        return self.durability <= 0
    