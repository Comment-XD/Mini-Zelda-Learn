class Effect:
    def __init__(self, time: int=2) -> None:
        self.time = time

class Regeneration(Effect):
    def __init__(self, time: int=2) -> None:
        super().__init__(time)
        self.name = "Regeneration"
        self.heal = 1
    
    def __str__(self) -> str:
        return "+"

class Strength(Effect):
    def __init__(self, time: int=2) -> None:
        super().__init__(time)
        self.name = "Strength"
        self.dmg = 1
    
    def __str__(self) -> str:
        return "="

class Poison(Effect):
    def __init__(self, time: int=2) -> None:
        super().__init__(time)
        self.name = "Poison"
        self.poison = 1
    
    def __str__(self) -> str:
        return "-"

class Burned(Effect):
    def __init__(self, time: int = 2) -> None:
        super().__init__(time)
        self.name = "Burned"
        self.burned = 1