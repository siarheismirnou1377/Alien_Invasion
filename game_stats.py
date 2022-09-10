class GameStats():
    """Отслеживает статистику для игры Alien Invasion."""

    def __init__(self, ai_game):
        """Инициализирует статистику."""
        self.settings = ai_game.settings
        self.reset_stats()

        # Игра Alien Invasion запускается в активном состоянии.
        self.game_active = True
        
    def reset_stats(self):
        """Инициализирует статистику, изменяющуюся в ходу игры."""
        self.ship_left = self.settings.ship_limit