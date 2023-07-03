import time
import pygame
from pygame.rect import Rect
from pygame.math import Vector2
from pygame.surface import Surface
import assets.asset_manager as assetmanager
import game_entities.gameobject as gameobject
import entities.configurations_entity as config

class Girl(gameobject.GameObject):
    def __init__( \
        self, configuration: \
            config.Configurations):

        super().__init__(configuration)

        self.game = configuration.game
        self.debug = configuration.debug
        self.activity = configuration.activity
        self.rest_time = self.activity.girl.rest_time
        self.position:Vector2 = self.__init_position()

        self._center()

        self.sprite_counter = 0

        self.is_moving_left = False
        self.is_moving_right = True

        self.render_rect:Rect = self.__girl_rect()
        self.left_girl_rects:list[Rect] = self.__get_left_rects()
        self.right_girl_rects:list[Rect] = self.__get_right_rects()


    def __init_position(self):
        return pygame.math.Vector2(0, \
            self.game.screen_size[1] - self.activity.girl.width)


    def __girl_rect(self):
        return pygame.Rect(0, 0, \
            self.activity.girl.width, \
                self.activity.girl.height)


    def handle_input(self, key, is_pressed):
        """ Method empty """
        pass

    def __get_right_rects(self):
        position_x:int = 64
        position_y:int = 0

        new_position_x:int = 64

        right_rects:list[Rect] = []

        width:int = self.activity.girl.width
        height:int = self.activity.girl.height

        for i in range(1, 9):
            right_rects.append( \
                Rect(new_position_x, position_y, width, height))

            new_position_x = position_x + (i * self.activity.girl.width)

        return right_rects
    

    def __get_left_rects(self):
        position_x:int = 512
        position_y:int = 128

        new_position_x:int = 64

        left_rects:list[Rect] = []

        width:int = self.activity.girl.width
        height:int = self.activity.girl.height

        for i in range(1, 9):
            left_rects.append( \
                Rect(new_position_x, position_y, width, height))

            new_position_x = position_x - (i * self.activity.girl.width)

        return left_rects


    def update(self, delta_time):
        velocity = pygame.math.Vector2(0.0, 0.0)

        if self.is_moving_left:
            velocity.x -= self.activity.girl.speed

        if self.is_moving_right:
            velocity.x += self.activity.girl.speed

        distance = velocity * delta_time

        self.position += distance

        self._center()


    def render(self, surface_dst:Surface):
        girl_rect:Rect = Rect(0, 0, 0, 0)
        
        if (self.sprite_counter == 8):
            self.sprite_counter = 0

        if self.is_moving_left:
            girl_rect = self. \
                left_girl_rects \
                    [self.sprite_counter]

            if self.position.x - self.render_rect.width / 4 <= 0:
                self.is_moving_left = False
                self.is_moving_right = True

                self.sprite_counter = 0

            else:
                self.sprite_counter += 1

        if self.is_moving_right:
            girl_rect = self. \
                right_girl_rects \
                    [self.sprite_counter]
            
            if self.position.x + self.render_rect.width / 4 >= self.game.screen_size[0]:
                self.is_moving_left = True
                self.is_moving_right = False

                self.sprite_counter = 0

            else:
                self.sprite_counter += 1

        image = assetmanager.AssetManager. \
            instance().get(self.activity.girl.name)

        surface_dst.blit(image, self.render_rect, girl_rect)

        if self.debug.is_debug:
            self._render_debug(surface_dst)

        time.sleep(self.rest_time)


    def release(self):
        """ Method empty """
        pass
        