import pygame
import states.state as state
from pygame.font import Font
import utils.messages as messages
from pygame.surface import Surface
import utils.constants as constants
import assets.asset_manager as assetmanager
import sounds.sounds_manager as soundsmanager
import entities.configurations_entity as config

class Intro(state.State):
    def __init__(self, \
        configuration:config.Configurations):

        super().__init__()

        self.next_state = \
            constants.GAMEPLAY_STATE

        self.font = configuration.font
        self.game = configuration.game
        self.intro = configuration.intro
        self.configuration = configuration


    def __set_game_music(self, ):
        sounds = soundsmanager. \
            SoundsManager(self.configuration)

        sounds.set_game_music()


    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            self.done = True

    def update(self, delta_time):
        """ Method empty """
        pass

    def render(self, surface_dst:Surface):
        surface_dst.blit(self.intro_title, (self.intro.pos_label[0], self.intro.pos_label[1]))
        surface_dst.blit(self.intro_press_key, (self.intro.pos_key[0], self.intro.pos_key[1]))

    def release(self):
        """ Method empty """
        pass

    def enter(self):
        self.done = False

        self.__set_game_music()

        font:Font = assetmanager.AssetManager.instance().get(self.font.name)

        self.intro_title:Surface = font.render(messages.ACTIVIDAD_FINAL, True, self.game.foreground_color, None)
        self.intro_press_key:Surface = font.render(messages.PRESS_ANY_KEY, True, self.game.foreground_color, None)

    def exit(self):
        """ Method empty """
        pass