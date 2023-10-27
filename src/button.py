class Button:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        self.pressed = False
        
    
    def update(self, box):
        if (self.x, self.y) == (box.x, box.y):
            self.pressed = True
        
    