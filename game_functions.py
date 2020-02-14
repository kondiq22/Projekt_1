import sys
import pygame
from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Reakcja na naciśnięcie klawisza."""
    if event.key == pygame.K_RIGHT:
        #Przesunięcie statku w prawą stronę.
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)

def fire_bullet(ai_settings, screen, ship, bullets):
    """Wystrzelenie pocisku, jeśli nie przekroczono ustalonego limitu."""
    #Utworzenie nowego pocisku i dodanie go do grupy pocisów.
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)
def check_keyup_events(event, ship):
    """Reakcja na zwolnienie klawisza."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):
    """Reakcja na zdarzenia w generowane przez klawiaturę i mysz."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, 
            bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship, bullets):
    """Uaktualnienie obrazów na ekranie i przejście do nowego ekranu."""
    #Odświeżanie ekranu w trakcie każdej iteracji pętli. 
    screen.fill(ai_settings.bg_color)
    #Ponowne wyświetlenie wszystkich pocisów pod warstwami statku kosmicznego
    # i obcych.
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()

    #Wyświetlenie ostatnio zmodyfikowanego ekranu. 
    pygame.display.flip()

def update_bullets(bullets):
    """Uaktualnienie położenia pocisków i usunięcie tych niewidocznych
    na ekranie."""
    #Uaktualnianie położenia pocisków
    bullets.update()

    #Usuwanie pocisków, które znajdują się poza ekranem.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
