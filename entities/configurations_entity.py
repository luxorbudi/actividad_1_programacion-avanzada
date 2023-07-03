import entities.font_entity as Font
import entities.game_entity as Game
import entities.debug_entity as Debug
import entities.intro_entity as Intro
import entities.music_entity as Music
import entities.banner_entity as Banner
import entities.timing_entity as Timing
import entities.activity_entity as Activity
import entities.gameplay_entity as Gameplay
import entities.background_entity as Background

class Configurations:

    def __init__(self):
        self.font = Font.Font()
        self.game = Game.Game()
        self.debug = Debug.Debug()
        self.intro = Intro.Intro()
        self.music = Music.Music()
        self.banner = Banner.Banner()
        self.timing = Timing.Timing()
        self.activity = Activity.Activity()
        self.gameplay = Gameplay.GamePlay()
        self.background = Background.Background()