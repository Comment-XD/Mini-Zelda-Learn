from src.desc import Desc

class Item:
    def __init__(self, name: str, count: int=1) -> None:
        self.name = name
        self.desc = Desc.item[name]
        self.count = count
    
        
class Consumable(Item):
    def __init__(self, name: str, count: int = 1) -> None:
        super().__init__(name, count)
    

class Healing(Consumable):
    def __init__(self, name: str, heal: int=1, count: int=1) -> None:
        super().__init__(name, count)
        self.heal = heal
    
    def __str__(self) -> str:
        return "+"
        
class Damage(Consumable):
    def __init__(self, name: str, dmg: int=1, count: int=1) -> None:
        super().__init__(name, count)
        self.dmg = dmg
    
    def __str__(self) -> str:
        return "-"
    
        