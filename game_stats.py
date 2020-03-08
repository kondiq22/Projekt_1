class GameStats():
    """Monitorowanie danych statystycznych w grze "Inwaazja obcych"."""

    def __init__(self, ai_settings):
        """Inicjalizacjaa danych statystycznuch."""
        self.ai_settings = ai_settings
        self.reset_stats()

        #Uruchomienie gry w stanie nie aktywnym.
        self.game_active = False

        #Najlepszy wynik nigdy nie powinien zostać wyzerowany
        self.high_score = 0

    def reset_stats(self):
        """Inicjalizacja danych staatystycznych, które mogą mieniaać się
        w trakcie gry."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
        