class Crate:
    def __init__(self, *args) -> None:
        self.loot = args
    
    def __str__(self) -> str:
        return "$"