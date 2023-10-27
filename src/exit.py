from src.lever import Lever
from src.button import Button

class Exit:
    def __init__(self: str, connections: list[Lever, Button]=[]) -> None:
        self.connections = connections
        self.status = False
    
    def update_status(self):
        new_status = True
        for lever in self.connections:
            if not lever.status:
                new_status = False
            
        self.status = new_status
        return self.status
    
    def __str__(self) -> str:
        return "~"    
            