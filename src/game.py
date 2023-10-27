from src.level import Level

class Game:
    def __init__(self, levels: list[Level]) -> None:
        """
        This is the game class

        Args:
            levels (list[Level]): a list of levels for the player to complete
        """
        self.levels = levels
        self.status = False
        self.player_level = 0 
        # player starts at the first level which in this case it 0
        
    def start(self, player) -> None:
        player.lvl = self.levels[self.player_level]
        self.levels[self.player_level].spawn_player(player)
    
    def next_level(self) -> None:
        self.player_level += 1
    
    def victory(self) -> bool:
        # this code will not work as we are checking self.status to see if player has completed the game
        for level in self.levels:
            if level.status is False:
                return False
        
        return True
        
        
        