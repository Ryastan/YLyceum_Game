import pygame
from pygame import *
from hero import Hero
from portal import Portal
from blocks import Platforms
from blocks import Platforms1
from booster import coal
import os
import sys

def load_image(name, colorkey=None):
    fullname = os.path.join("sprites",name)
    # если файл не существует, то выходим
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        sys.exit()
    image = pygame.image.load(fullname)
    return image





class Levels:
    def __init__(self):
        pass

    def load(self, W, H, number):
        clock = pygame.time.Clock()
        FPS = 60  # ФПС игры

        # Цвета в RGB
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        RED = (255, 0, 0)
        GREEN = (0, 255, 0)
        BLUE = (0, 0, 255)
        left = False
        right = False
        up = False
        hero = Hero(550, 550)  # Класс героя
        entities = pygame.sprite.Group()  # Все объекты

        platforms = []  # Все Платформы
        bentities = pygame.sprite.Group()  # Обьекты заднего плана
        class backg(pygame.sprite.Sprite):
            def __init__(self):
                super().__init__(bentities)
                self.image = load_image("menu_back.png")
                self.rect = self.image.get_rect()
                self.rect.x = 0
                self.rect.y = 0
        backgr = backg()
        bentities.add(backgr)

        level1 = ["-------------------------",
                  "0                       0",
                  "0                       0",
                  "0                       0",
                  "0            -- ----33-00",
                  "0                       0",
                  "00                      0",
                  "0                       0",
                  "0       1               0",
                  "0                       0",
                  "0                       0",
                  "0      ---              0",
                  "0                       0",
                  "0                       0",
                  "0                       0",
                  "0   -------      -      0",
                  "0                       0",
                  "0             ----------0",
                  "0                       0",
                  "0-----------------------0"]
        #entities.add(hero)
        surface = pygame.display.set_mode((W, H))
        pygame.display.set_caption('Game')
        run_game = True
        bg = Surface((W, H))
        he = Surface((150, 150))
        bentities.draw(bg)
        x = 0
        y = 0
        for row in level1:
            for col in row:
                if col == "-":
                    platform = Platforms(x, y, W // 25, H // 20, 1)
                    entities.add(platform)
                    platforms.append(platform)
                if col == "1":
                    platform = coal(x, y)
                    entities.add(platform)
                if col == "0":
                    platform = Platforms(x, y, W // 25, H // 20, 0)
                    entities.add(platform)
                    platforms.append(platform)
                if col == "3":
                    platform = Platforms1(x, y, W // 25, H // 20, 0)
                    entities.add(platform)
                x += W // 25
            y += H // 20
            x = 0
        timing = 0
        while run_game:  # Главный цикл игры
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run_game = False
                elif event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        left = True
                    elif event.key == K_RIGHT:
                        right = True
                    elif event.key == K_UP:
                        up = True
                elif event.type == KEYUP:
                    if event.key == K_LEFT:
                        left = False
                    elif event.key == K_RIGHT:
                        right = False
                    elif event.key == K_UP:
                        up = False
            if hero.condition == 6 and hero.time < -100:
                run_game = False


            surface.blit(bg, (0, 0))
            timing += 1
            if timing == 3:
                hero.anim_time += 1
                timing = 0
            hero.update(left, right, up, platforms)  # передвижение
            surface.blit(hero.image, (hero.rect.centerx - 75, hero.rect.centery - 60))
            entities.draw(surface)
            bentities.draw(bg)
            hero.time -= 1
            pygame.display.update()
            pygame.display.flip()
            print(hero.time)
            clock.tick(60)


    def load_menu(self, W, H):
        clock = pygame.time.Clock()
        FPS = 60  # ФПС игры

        # Цвета в RGB
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        RED = (255, 0, 0)
        GREEN = (0, 255, 0)
        BLUE = (0, 0, 255)
        entities = pygame.sprite.Group()  # Все объекты
        backentities = pygame.sprite.Group()
        surface = pygame.display.set_mode((W, H))
        pygame.display.set_caption('Game')
        run_game = True
        bg = Surface((W, H))
        bg.fill(RED)
        x = 0
        y = 0
        class backg(pygame.sprite.Sprite):
            def __init__(self):
                super().__init__(backentities)
                self.image = load_image("menu_back.png")
                self.rect = self.image.get_rect()
                self.rect.x = 0
                self.rect.y = 0
        class textm(pygame.sprite.Sprite):
            def __init__(self, posx, posy):
                super().__init__(entities)
                self.image = load_image("menutext_sprite.png")
                self.rect = self.image.get_rect()
                self.rect.x = posx
                self.rect.y = posy


        text_in_m = textm(3, 300)
        back_ground_menu = backg()

        backentities.add(text_in_m)
        entities.add(back_ground_menu)


        while run_game:  # Главный цикл игры
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run_game = False
                if event.type == KEYDOWN:
                    run_game = False
            backentities.draw(bg)
            entities.draw(surface)
            surface.blit(bg, (0, 0))

            pygame.display.update()
            pygame.display.flip()
            clock.tick(60)
