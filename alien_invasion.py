import pygame

from pygame.sprite import Group
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from ship import Ship
from alien import Alien
import game_functions as gf


def run_game():
    #Inicjalizacja gry i utworzenie obiektu ekaranu.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Inwazja obcych")

    #Utowrzenie przycisku Gra.
    play_button = Button(ai_settings, screen, "Gra")

    #Utworzenie egzemplarza przeznaczonego do przechowywania danych
    #statystycznych gry oraz utworzenie egzemplarza klasy Scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)


    #Utworzenie statku kosmicznego, grupy pocisków oraz grupy obcych.
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    #Utworzenie floty obcych.
    gf.create_fleet(ai_settings, screen, ship, aliens)

    #Rozpoczęcie pętli głównej gry.
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, 
bullets)
        ship.update()
        if stats.game_active:
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)      

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, 
        play_button)

run_game()