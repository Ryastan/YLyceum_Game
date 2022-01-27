import pygame
from pygame import *
from hero import Hero
from blocks import Platforms
from blocks import Platforms1
from blocks import life_bar
from booster import coal
from booster import spike
from booster import enter
from booster import exit
import os
import sys
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.init()

pygame.mixer.music.load("sounds/main_sound_game.wav")
pygame.mixer.music.play(-1)

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
        self.sound_death = pygame.mixer.Sound("sounds/death_soul.wav")
        self.sound_picked_up = pygame.mixer.Sound("sounds/picked_crystall.wav")
        self.sound_picked_up.set_volume(0.3)
        self.sound_walking = pygame.mixer.Sound("sounds/walking.wav")
        self.sound_walking.set_volume(0.5)
        self.sound_portal_shift = pygame.mixer.Sound("sounds/portal_shift.wav")
        self.sound_portal_shift.set_volume(0.3)
        self.sound_phase_shift = pygame.mixer.Sound("sounds/phase_shift2.wav")
        self.sound_phase_shift.set_volume(0.3)
        self.level = 0
        self.levels = [
                    [".........................",
                     "0                       0",
                     "0                      60",
                     "0                       0",
                     "0               --------0",
                     "0              -        0",
                     "0             -         0",
                     "0------      -          0",
                     "0           -           0",
                     "0          -            0",
                     "0         -             0",
                     "0      ---              0",
                     "0--                     0",
                     "0 --                    0",
                     "0  --                   0",
                     "0   -------      -      0",
                     "0                     --0",
                     "05            ----------0",
                     "0           --00000000000",
                     "0-----------------------0"],

                    ["                         ",
                     "0                       0",
                     "0                      60",
                     "0            --         0",
                     "0           --- --------0",
                     "0-                      0",
                     "00-                     0",
                     "000-                    0",
                     "0000-                   0",
                     "0                      10",
                     "0           --       ---0",
                     "0      ---              0",
                     "0--                     0",
                     "0 ---                   0",
                     "0  ---                  0",
                     "0   -------             0",
                     "0                     --0",
                     "05                  ----0",
                     "0                  -00000",
                     "0-----------------------0"],

                     ["                         ",
                     "0                       0",
                     "0                      60",
                     "0                       0",
                     "0              1----33-00",
                     "0                       0",
                     "00         -            0",
                     "0       1--             0",
                     "0                       0",
                     "0                       0",
                     "0                       0",
                     "0   1  ---              0",
                     "0                       0",
                     "0                       0",
                     "0                       0",
                     "0   -------             0",
                     "0                       0",
                     "05            ----------0",
                     "0                       0",
                     "0-----------------------0"],

                     ["                         ",
                      "0                       0",
                      "0                      60",
                      "0                  44   0",
                      "0              1----00-00",
                      "0                       0",
                      "00         -            0",
                      "0       1--             0",
                      "0                       0",
                      "0                       0",
                      "0                       0",
                      "0---1   1               0",
                      "0                       0",
                      "0                       0",
                      "0    4444               0",
                      "0   --------            0",
                      "0                       0",
                      "05            ----------0",
                      "0            -00000000000",
                      "0-----------------------0"],

                      ["                         ",
                      "0                       0",
                      "0                      60",
                      "0                       0",
                      "0              1----00-00",
                      "0                       0",
                      "00             1        0",
                      "0       1--             0",
                      "0                     440",
                      "0                   ----0",
                      "0                       0",
                      "0---1 1                 0",
                      "0        1              0",
                      "0           1   1       0",
                      "0                       0",
                      "0                       0",
                      "0                     --0",
                      "05                   -000",
                      "0       44          -0000",
                      "0-----------------------0"],

                      ["                         ",
                      "0                      60",
                      "0          1            0",
                      "0      1        44444   0",
                      "0               -------00",
                      "04     1   4444         0",
                      "00       44----         0",
                      "0       1--             0",
                      "0                       0",
                      "0     1                 0",
                      "0444                    0",
                      "0---     1              0",
                      "0           1           0",
                      "0              1        0",
                      "04444444444444    1     0",
                      "0-------------          0",
                      "0                       0",
                      "05                      0",
                      "0                44444440",
                      "0-----------------------0"]
        ]

    def load(self, W, H, number):
        clock = pygame.time.Clock()
        FPS = 60  # ФПС игры
        lifea = life_bar(0, 0, 1500, 1500)
        # Цвета в RGB
        WHITE = (255, 255, 255)
        BLACK = (0, 0, 0)
        RED = (255, 0, 0)
        GREEN = (0, 255, 0)
        BLUE = (0, 0, 255)
        left = False
        right = False
        up = False
        shift = False
        dead = False
        walking = True
        phase_shift = True
        counter = 0
        counter1 = 0
        hero = Hero(100, 900)  # Класс героя
        entities = pygame.sprite.Group()  # Все объекты
        crstals = pygame.sprite.Group() #Бустовые кристаллы
        platforms = []  # Все Платформы
        bentities = pygame.sprite.Group()  # Обьекты заднего плана
        enemies = pygame.sprite.Group()
        black = Surface((W, H))
        class backg(pygame.sprite.Sprite):
            def __init__(self):
                super().__init__(bentities)
                self.image = load_image("menu_back.png")
                self.rect = self.image.get_rect()
                self.rect.x = 0
                self.rect.y = 0


        class text4(pygame.sprite.Sprite):
            def __init__(self, posx, posy):
                super().__init__(entities)
                self.image = load_image("death.png")
                self.image = pygame.transform.scale(self.image, (1000, 400))
                self.rect = self.image.get_rect()
                self.rect.x = posx
                self.rect.y = posy
        

        backgr = backg()
        bentities.add(backgr)
        surface = pygame.display.set_mode((W, H))
        pygame.display.set_caption('Game')
        run_game = True
        bg = Surface((W, H))
        bentities.draw(bg)
        x = 0
        y = 0
        for row in self.levels[number]:
            for col in row:
                if col == "-":
                    platform = Platforms(x, y, W // 25, H // 20, 1)
                    entities.add(platform)
                    platforms.append(platform)
                if col == "1":
                    platform = coal(x, y)
                    entities.add(platform)
                    crstals.add(platform)
                if col == "0":
                    platform = Platforms(x, y, W // 25, H // 20, 0)
                    entities.add(platform)
                    platforms.append(platform)
                if col == "3":
                    platform = Platforms1(x, y, W // 25, H // 20, 0)
                    entities.add(platform)
                if col == "4":
                    platform = spike(x, y)
                    entities.add(platform)
                    enemies.add(platform)
                if col == "5":
                    platform = enter(x, y)
                    entities.add(platform)
                if col == "6":
                    self.exit1 = exit(x, y)
                    entities.add(self.exit1)
                x += W // 25
            y += H // 20
            x = 0
        timing = 0
        while run_game:  # Главный цикл игры
            up = False
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run_game = False
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_LEFT:
                        left = True
                        if walking == True and not dead:
                            walking = False
                            self.sound_walking.play(-1)
                    elif event.key == K_RIGHT:
                        right = True
                        if walking == True and not dead:
                            walking = False
                            self.sound_walking.play(-1)
                    elif event.key == K_UP:
                        up = True
                    elif event.key == K_LSHIFT:
                        shift = True
                    elif event.key == K_ESCAPE and dead:
                        self.load_menu(W, H)
                    elif event.key == K_LCTRL and dead:
                        self.level = 0
                        self.load(W, H, self.level)

                elif event.type == KEYUP:
                    if event.key == K_LEFT:
                        left = False
                        walking = True
                        self.sound_walking.stop()
                    elif event.key == K_RIGHT:
                        right = False
                        walking = True
                        self.sound_walking.stop()
                    elif event.key == K_UP:
                        up = False
                        prev_up = False
                    elif event.key == K_LSHIFT:
                        shift = False
            if hero.condition == 5 and not dead:
                dead = True
                self.sound_death.play()
                bentities.add(text4(250, 350))
            
            if hero.picked_up:
                self.sound_picked_up.play()
                hero.picked_up = False

            if hero.shift_used > 0:
                hero.shift_used -= 1

            if hero.shift_used > 80:
                hero.y_speed = 0
            
            if shift and hero.live == 1 and hero.shift_used == 0:
                self.sound_phase_shift.play()

            if hero.extra_jump > 0:
                hero.extra_jump -= 1
            surface.blit(bg, (0, 0))
            timing += 1
            if timing == 3:
                hero.anim_time += 1
                timing = 0
            hero.update(left, right, up, shift, platforms, crstals, enemies, self.exit1)  # передвижение
            surface.blit(hero.image, (hero.rect.centerx - 75, hero.rect.centery - 60))
            entities.draw(surface)
            bentities.draw(bg)
            if hero.live == 1:
                surface.blit(pygame.transform.scale(lifea.image, (0 + hero.time // 9, 0 + hero.time // 9)), (750, 10))
            hero.time -= 1
            if counter < 50:
                surface.blit(black, (0, counter * 20))
            if hero.condition == 7 and counter1 < 1:
                counter1 = 50
                if phase_shift == True:
                    phase_shift = False
                    self.sound_portal_shift.play()
            if counter1 > 0:
                print(counter1)
                surface.blit(black, (0, counter1 * 20))
                counter1 -= 1
            if counter1 == 1:
                self.level += 1
                if self.level <= 5:
                    self.load(W, H, self.level)
                else:
                    self.load_win_screen(W, H)
            pygame.display.update()
            pygame.display.flip()
            counter += 1
            clock.tick(FPS)

    def load_menu(self, W, H):
        clock = pygame.time.Clock()
        self.level = 0
        FPS = 60  # ФПС игры
        # Цвета в RGB
        RED = (255, 0, 0)
        entities = pygame.sprite.Group()  # Все объекты
        backentities = pygame.sprite.Group()
        surface = pygame.display.set_mode((W, H))
        black = Surface((W, H))
        black.fill((0, 0, 0))
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
        class text2(pygame.sprite.Sprite):
            def __init__(self, posx, posy):
                super().__init__(entities)
                self.image = load_image("menu_new_game.png")
                self.image = pygame.transform.scale(self.image, (1500, 75))
                self.rect = self.image.get_rect()
                self.rect.x = posx
                self.rect.y = posy

        class text3(pygame.sprite.Sprite):
            def __init__(self, posx, posy):
                super().__init__(entities)
                self.image = load_image("escape.png")
                self.image = pygame.transform.scale(self.image, (1500, 75))
                self.rect = self.image.get_rect()
                self.rect.x = posx
                self.rect.y = posy

        text_in_m = textm(3, 300)
        text_in_m2 = text2(0, 550)
        text_in_m3 = text3(0, 700)
        back_ground_menu = backg()

        backentities.add(text_in_m)
        backentities.add(text_in_m2)
        backentities.add(text_in_m3)
        entities.add(back_ground_menu)

        anim_timer = 0
        while run_game:  # Главный цикл игры
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run_game = False
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        run_game = False
                    elif event.key == K_RIGHT and anim_timer < 1:
                        anim_timer = 1
            backentities.draw(bg)
            entities.draw(surface)
            surface.blit(bg, (0, 0))
            print(anim_timer)
            if anim_timer > 0:
                anim_timer += 5
                surface.blit(black, (0, H - anim_timer * 2))
            if anim_timer > 500:
                self.load_tutorial(W, H)
            pygame.display.update()
            pygame.display.flip()
            clock.tick(FPS)
        
        pygame.quit()
        sys.exit()

    def load_tutorial(self, W, H):
        run_game = True
        clock = pygame.time.Clock()
        FPS = 60

        surface = pygame.display.set_mode((W, H))
        pygame.display.set_caption('Tutorial')
        backentities = pygame.sprite.Group()
        black = Surface((W, H))
        black.fill((0, 0, 0))


        class tutorial(pygame.sprite.Sprite):
            def __init__(self):
                super().__init__(backentities)
                self.image = load_image("tutorial.png")
                self.rect = self.image.get_rect()
                self.rect.x = 0
                self.rect.y = 0

        # img_tutorial = tutorial
        backentities.add(tutorial())
        anim_timer = 0

        while run_game:  # Главный цикл игры
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run_game = False
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_TAB and anim_timer < 1:
                        anim_timer = 1
            print(anim_timer)
            backentities.draw(surface)
            if anim_timer > 0:
                anim_timer += 5
                surface.blit(black, (0, H - anim_timer * 2))
            if anim_timer > 500:
                self.load(W, H, self.level)

            pygame.display.update()
            pygame.display.flip()
            clock.tick(FPS)

    def load_win_screen(self, W, H):
        run_game = True
        clock = pygame.time.Clock()
        FPS = 60

        surface = pygame.display.set_mode((W, H))
        pygame.display.set_caption('WIN')
        backentities = pygame.sprite.Group()
        black = Surface((W, H))
        black.fill((0, 0, 0))


        class win(pygame.sprite.Sprite):
            def __init__(self):
                super().__init__(backentities)
                self.image = load_image("win.png")
                self.rect = self.image.get_rect()
                self.rect.x = 0
                self.rect.y = 0

        # img_tutorial = tutorial
        backentities.add(win())
        anim_timer = 0

        while run_game:  # Главный цикл игры
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run_game = False
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE and anim_timer < 1:
                        anim_timer = 1
            print(anim_timer)
            backentities.draw(surface)
            if anim_timer > 0:
                anim_timer += 5
                surface.blit(black, (0, H - anim_timer * 2))
            if anim_timer > 500:
                self.load_menu(W, H)

            pygame.display.update()
            pygame.display.flip()
            clock.tick(FPS)