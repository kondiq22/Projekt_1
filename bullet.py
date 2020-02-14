import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Klasa przeznaczonaa do zarządzania pociskami wystrzeeliwanymi przez
    statek."""
    def __init__(self, ai_settings, screen, ship):
        """Utworzenie obiektu pocisku w aaaktualnym położeniu statku."""
        super(Bullet, self).__init__()
        self.screen = screen

        #Utworzenie prostokąta pocisku w punkcie (0,0), a następnie zdefiniowanie
        #dla niego odpowiedniego położenia.
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,
        ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        #Położenie pocisku jest zdefiniowane za pomocą wartości zmiennoprzecinkowej.
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor
    def update(self):
        """Poruszanie pociskiem po ekranie."""
        #Uaktualnienie położenia pocisku.
        self.y -= self.speed_factor
        #Uaktualnianie położenia prostokąta pocisku.
        self.rect.y = self.y
    
    def draw_bullet(self):
        """Wyświetalnie pocisku na ekranie."""
        pygame.draw.rect(self.screen, self.color, self.rect)