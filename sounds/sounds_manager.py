import pygame
import assets.asset_manager as asset_manager
import entities.configurations_entity as config

class SoundsManager:
    def __init__(self, \
        configuration:config.Configurations):

        self.music = configuration.music
        self.gameplay = configuration.gameplay


    def set_game_music(self):
        music = \
            asset_manager.AssetManager \
                .instance().get(self.music.name)

        pygame.mixer.music.stop()
        pygame.mixer.music.load(music)
        pygame.mixer.music.set_volume(self.music.volume)

        pygame.mixer.music.play(-1)


    def set_gameplay_music(self):
        music = \
            asset_manager.AssetManager \
                .instance().get(self.gameplay.music.name)

        pygame.mixer.music.stop()
        pygame.mixer.music.load(music)
        pygame.mixer.music.set_volume(self.gameplay.music.volume)

        pygame.mixer.music.play(-1)