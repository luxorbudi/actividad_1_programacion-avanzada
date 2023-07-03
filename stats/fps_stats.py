from pygame.font import Font
import assets.asset_manager as assetmanager
import entities.configurations_entity as config

class FPSStats:
    def __init__(self, \
        configuration:config.Configurations):

        self.update_time = 0
        self.logic_frames = 0
        self.render_frames = 0

        self.font = configuration.font
        self.game = configuration.game
        self.timing = configuration.timing

        self.__set_fps_surface()


    def update(self, delta_time):
        self.logic_frames += 1
        self.update_time += delta_time

        if self.update_time >= self.timing.refresh_stats_time:
            self.__set_fps_surface()

            self.logic_frames = 0
            self.render_frames = 0
            self.update_time -= self.timing.refresh_stats_time


    def render(self, surface_dst):
        self.render_frames += 1
        surface_dst.blit(self.image, self.timing.fps_pos)


    def __set_fps_surface(self):
        font:Font = assetmanager.AssetManager.instance().get(self.font.name)        
        self.image = font.render(f'{self.logic_frames} - {self.render_frames}', True, self.game.foreground_color, None)