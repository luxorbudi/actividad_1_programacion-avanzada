import pygame
from typing import Tuple
import assets.asset as asset
import states.state as state
import game_entities.girl as girl
import utils.constants as constants
import game_entities.banner as banner
import assets.asset_manager as assetmanager
import sounds.sounds_manager as soundsmanager
import game_entities.rendergroup as rendergroup
import entities.configurations_entity as config

class GamePlay(state.State):
    def __init__(self, \
        configurations:config.Configurations):

        super().__init__()

        self.next_state = \
            constants.INTRO_STATE

        self.activity = \
            configurations.activity

        self.configurations = configurations

        self.__girl = rendergroup.RenderGroup()
        self.__banner = rendergroup.RenderGroup()


    def __set_gameplay_music(self):
        sounds = soundsmanager. \
            SoundsManager(self.configurations)

        sounds.set_gameplay_music()


    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F1:
                self.done = True

            self.__girl.input(event.key, True)

        elif event.type == pygame.KEYUP:
            self.__girl.input(event.key, False)


    def update(self, delta_time):
        self.__banner.update(delta_time)
        self.__girl.update(delta_time)


    def render(self, surface_dst):
        self.__banner.draw(surface_dst)
        self.__girl.draw(surface_dst)


    def release(self):
        """ Method empty """
        pass


    def enter(self):
        self.done = False

        self.__load_gameplay_music()

        self.__set_gameplay_music()

        self.__load_activity_assets()

        self.__girl.add(girl.Girl(self.configurations))
        self.__banner.add(banner.Banner(self.configurations))


    def exit(self):
        self.__girl.empty()
        self.__banner.empty()
        self.__unload_assets()


    def __load_activity_assets(self):
        assetmanager.AssetManager.instance(). \
            load('gameplay', asset.AssetType.Image, \
                self.activity.girl.name, self.activity.girl.image_file)
        
        assetmanager.AssetManager.instance(). \
            load('gameplay', asset.AssetType.Image, \
                self.activity.alien.name, self.activity.alien.image_file)


    def __load_gameplay_music(self):
        assetmanager.AssetManager.instance().load('gameplay', asset.AssetType.Music, \
            self.configurations.gameplay.music.name, self.configurations.gameplay.music.file)


    def __unload_assets(self):
        assetmanager.AssetManager.instance().clean('gameplay')