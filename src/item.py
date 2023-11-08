from src.desc import Desc
from src.effect import*

class Item:
    def __init__(self, name: str, count: int=1, effects=None) -> None:
        self.name = name
        self.desc = Desc.item[name]
        self.count = count
        self.effects = effects
    
        
class Consumable(Item):
    def __init__(self, name: str, count: int = 1, effects=None) -> None:
        super().__init__(name, count, effects)

class Healing(Consumable):
    def __init__(self, name: str, heal: int=1, count: int=1, effects=None) -> None:
        super().__init__(name, count, effects)
        self.heal = heal
    
    def __str__(self) -> str:
        return "+"
        
class Damage(Consumable):
    def __init__(self, name: str, dmg: int=1, count: int=1, effects=None) -> None:
        super().__init__(name, count, effects)
        self.dmg = dmg
    
    def __str__(self) -> str:
        return "="

# Items that can increase inventory space or weapon slots or disables traps(COMING SOON!)
class Utility(Item):
    def __init__(self, name: str, count: int = 1, effects=None) -> None:
        super().__init__(name, count, effects)
        
# Effect Timer, Adds effects on players for a certain time 
