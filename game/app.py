import pygame
import assets.asset as asset_type
from pygame.surface import Surface
import stats.fps_stats as fps_stats
import configurations.config as config
import assets.asset_manager as asset_manager
import states.state_manager as state_manager

class App:
    def __init__(self):
        pygame.init()

        self.running = False

        self.config = config.Config()
        self.configurations = self.config.configurations

        self.screen = \
            self.__set_screen_mode()

        self.game = self.configurations.game
        self.debug = self.configurations.debug
        self.music = self.configurations.music
        self.timing = self.configurations.timing
        self.background = self.configurations.background

        self.__load_game_music()
        self.__load_font_assets()
        self.__load_background_assets()

        self.state_manager = state_manager \
            .StateManager(self.configurations)

        self.__set_game_background()

        if self.debug.is_debug:
            self.fps_stats = fps_stats\
                .FPSStats(self.configurations)

        pygame.display.set_caption(self.configurations.game.title)


    def __set_screen_mode(self):
        return pygame.display.set_mode( \
            self.configurations.game.screen_size, 0, 32)


    def __set_game_background(self):
        background:Surface = \
            asset_manager.AssetManager \
                .instance().get(self.background.name)

        background = \
            pygame.transform.scale( \
                background, tuple(self.game.screen_size))

        self.screen.blit(background, (0, 0))


    def run(self):
        self.__running = True

        time_since_last_update = 0
        last_time = pygame.time.get_ticks()

        while self.__running:
            delta_time, last_time = \
                self.__calc_delta_time(last_time)

            time_since_last_update += delta_time

            time_per_frame:int = self.timing.time_per_frame

            while time_since_last_update > time_per_frame:
                time_since_last_update -= time_per_frame

                self.__handle_input()
                self.__update(time_per_frame)

            self.__render()

        self.__release()


    def __handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.__running = False

                self.state_manager.handle_input(event)

            elif event.type == pygame.KEYUP:
                self.state_manager.handle_input(event)


    def __update(self, delta_time):
        self.state_manager.update(delta_time)

        if self.debug.is_debug:
            self.fps_stats.update(delta_time)


    def __render(self):
        self.__set_game_background()

        self.state_manager.render(self.screen)

        if self.debug.is_debug:
            self.fps_stats.render(self.screen)

        pygame.display.update()


    def __release(self):
        self.state_manager.release()
        self.__unload_assets()

        pygame.quit()


    def __calc_delta_time(self, last_time):
        current_time = pygame.time.get_ticks()
        delta_time = current_time - last_time

        return delta_time, current_time


    def __load_game_music(self):
        asset_manager.AssetManager.instance().load( \
            'game', asset_type.AssetType.Music, \
                self.configurations.music.name, self.configurations.music.file)


    def __load_font_assets(self):
        asset_manager.AssetManager.instance().load('game', \
            asset_type.AssetType.Font, self.configurations.font.name, \
                self.configurations.font.file, font_size = self.configurations.font.size)


    def __load_background_assets(self):
        asset_manager.AssetManager.instance()\
            .load('game', asset_type.AssetType.Image, \
                self.configurations.background.name, self.configurations.background.file)


    def __unload_assets(self):
        asset_manager.AssetManager.instance().clean('game')