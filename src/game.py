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
    
    def next_level(self, player) -> None:
        self.player_level += 1
        if self.player_level >= len(self.levels):
            return
        
        player.lvl.status = True
        player.lvl = self.levels[self.player_level]
        player.lvl.spawn_mobs()
        self.levels[self.player_level].spawn_player(player)
    
    def update_status(self) -> bool:
        # this code will not work as we are checking self.status to see if player has completed the game
        for level in self.levels:
            if level.status is False:
                self.status = False
                return 
        
        self.status = True
        
        
        