from src.desc import Desc
from src.effect import*

class Weapon:
    def __init__(self, name: str, dmg: int, effects=None) -> None:
        """Class that is used to attack players or mobs

        Args:
            name (str): name of the weapon
        """
        self.name = name
        self.desc = Desc.weapon[name]
        
        self.dmg = dmg
        self.durability = 100
        self.broken = False
        self.effects = effects
    
    def is_broken(self):
        return self.durability <= 0
        
class Melee(Weapon):
    def __init__(self, name: str, dmg: int, effects=None) -> None:
        super().__init__(name, dmg, effects)
        self.durability_loss = 5
        self.range = 1
        
        
class Ranged(Weapon):
    def __init__(self, name: str, dmg: int, effects=None) -> None:
        super().__init__(name, dmg, effects)
        self.durability_loss = 10
        self.range = 2
    