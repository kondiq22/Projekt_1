class Settings():
    """Klasa przeznaczona do przechowywania wsazystkich ustawień gry."""

    def __init__(self):
        """Inicjalizacja daanych statystycznych gry."""
        #Ustawienia ekranu. 
        self.screen_width = 1600
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        #Ustawienia dotyczące statku.
        self.ship_speed_factor = 51
        self.ship_limit = 2
        #Ustawienia dotyczące pocisku
        self.bullet_speed_factor = 31
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 333
        #Ustalenia dotyczące obcego.
        self.alien_speed_factor = 5
        self.fleet_drop_speed = 30
        #Wartość fleet_direction wynosząca 1 oznacza w prawo, natomiast -1 oznacza w lewo.
        self.fleet_direction = 10
        #Łatwa zmiana szybkości gry
        self.speedup_scale = 1.3
        #Łatwa zamina liczby punktów przyznawanych za zestrzelenie obcego.
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Inicjalizacja ustaawień, które ulegają zmianie w trakcie gry."""
        self.ship_speed_factor = 5
        self.bullet_speed_factor = 5
        self.alien_speed_factor = 2

        #Wartość fleet_direction wynosząca 1 oznacza prawo, natomiast -1 oznacza lewo.
        self.fleet_direction = 1

        #Punktacja.
        self.alien_points = 50

    def increase_speed(self):
        """Zmiana ustawień dotyczących szybkości i liczby przyznawanych punktów."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)
        