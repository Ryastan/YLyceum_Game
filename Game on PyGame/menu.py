import pygame
import pygame_menu
pygame.init()

class Menu:
    def __init_(self):
        pass

    @classmethod
    def start_the_game(self):
        pass
    
    @classmethod
    def load_menu(self, surface, W, H):
        menu = pygame_menu.Menu('FATED SOUL ADVENTURE',W, H, theme=pygame_menu.themes.THEME_DARK)

        menu.add.button('Play', self.start_the_game)
        self.level = menu.add.selector('Choose level', [('level1', 'a'), ('level2', 'a'), ('level3', )])
        menu.add.button('Quit', pygame_menu.events.EXIT)

        bg = pygame_menu.baseimage.BaseImage(
                        image_path="sprites/menu_back.png",
                        drawing_mode=pygame_menu.baseimage.IMAGE_MODE_FILL)

        menu.background_color = bg  
        
        menu.mainloop(surface)

# surface = pygame.display.set_mode((600, 500))
# pygame.display.set_caption('menu')

# while 1:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             run_game = False

#     menu = Menu
#     menu.load_menu(surface, 600, 500)