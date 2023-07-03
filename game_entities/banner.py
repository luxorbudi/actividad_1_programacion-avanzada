import pygame
from pygame.font import Font
from pygame.rect import Rect
from pygame.math import Vector2
from pygame.surface import Surface
import utils.constants as constants
import assets.asset_manager as assetmanager
import game_entities.gameobject as gameobject
import entities.configurations_entity as config

class Banner(gameobject.GameObject):
    def __init__(self, \
        configuration:config.Configurations):

        super().__init__(configuration)

        self.banner_index = 0

        self.font = configuration.font
        self.game = configuration.game
        self.debug = configuration.debug
        self.banner = configuration.banner
        self.activity = configuration.activity

        self.font:Font = self.__banner_font()
        self.area_rect:Rect = self.__alien_rect()
        self.render_rect:Rect = self.__alien_rect()
        self.position:Vector2 = self.__init_position()
        self.banner_surfaces:list[Surface] = self.__get_banner_surfaces()


    def __init_position(self):        
        return pygame.math.Vector2( \
            self.game.screen_size[0], \
                self.game.screen_size[1] / 4)
    

    def __alien_rect(self):
        return pygame.Rect(0, 0, \
            self.activity.alien.width, \
                self.activity.alien.height)


    def __banner_font(self):
        return \
            assetmanager.AssetManager \
                .instance().get(self.font.name)


    def __get_banner_characters(self):
        banner_text:str = self.banner.text

        banner_characters:list[str] = list()

        banner_words:list[str] = banner_text.split()

        for word in banner_words:
            for character in word:
                banner_characters.append(character)

            banner_characters.append(constants.STRING_EMPTY)

        return banner_characters[:-1]


    def __get_banner_surfaces(self):
        surfaces:list[Surface] = list()

        self.banner_characters:list[str] \
            = self.__get_banner_characters()

        for character in self.banner_characters:
            chr_surface:Surface = \
                self.font.render(character, \
                    True, self.game.foreground_color, None)

            surfaces.append(chr_surface)

        return surfaces


    def handle_input(self, key, is_pressed):
        """ Method empty """
        pass


    def update(self, delta_time):
        self.position.x -= self.banner.speed * delta_time

        self._center()


    def render(self, surface_dst:Surface):

        self.banner_index = 0

        alien_image:Surface = \
            assetmanager.AssetManager \
                .instance().get(self.activity.alien.name)
        
        alien_image.set_colorkey((82, 134, 2))
        
        surface_dst.blit(alien_image, \
            self.render_rect, self.area_rect)

        for surface in self.banner_surfaces:
            _, width = surface.get_size()

            surface_dst.blit(surface, (self.position.x + alien_image.get_width() * \
                self.activity.alien.text_separation + (self.banner_index * width), self.position.y))

            self.banner_index += 1

            if (self.banner_index == len(self.banner_surfaces)):
                if self.position.x + self.banner_index * width + \
                    alien_image.get_width() * self.activity.alien.text_separation < 0:
                    
                    self.position.x = self.game.screen_size[0]


    def release(self):
        """ Method empty """
        pass