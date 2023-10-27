from src.lever import Lever

class Exit:
    def __init__(self: str, connections: list[Lever]=[]) -> None:
        self.connections = connections
        self.status = False
    
    def update_status(self):
        new_status = True
        for lever in self.connections:
            if not lever.status:
                new_status = False
            
        self.status = new_status
    
    def __str__(self) -> str:
        return "~"    
            