from src.pushable import*

class Activator:
    def __init__(self, x: int=0, y: int=0, pushables: list=[]) -> None:
        self.x = x
        self.y = y
        self.status = False
        self.pushables = pushables
        
        # every object that passes through the button, button should store it in cache
        # when object is not on button anymore, remove it from the cache
    
    def update(self):
        for object in self.pushables:
            if (object.x, object.y) == (self.x, self.y):        
                self.status = True

class Hole(Activator):
    # Essentially should act as a wall until a boulder is place on it, 
    # when boulder is place on it, the boulder will be removed and the hole will be floor tile
    def __init__(self, x: int=0, y: int=0, pushables: list=[]) -> None:
        super().__init__(x, y, pushables)
    
    def __str__(self) -> str:
        return "0"
    

class Button(Activator):
    # Players can go on top of the button, and button should be true 
    # but once the player is off the button, status off the button should be False
    # maybe for cache check all the items positions? 
    # if the position is equal to the Button's position, set status = True
    
    def __init__(self, x: int=0, y: int=0, pushables: list=[]) -> None:
        super().__init__(x, y, pushables)
        
    
    def __str__(self) -> str:
        return "o"

class Lever:
    def __init__(self) -> None:
        self.status = False
        
    def __str__(self) -> str:
        return "/"

        
    
    
    