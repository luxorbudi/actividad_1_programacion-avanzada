import json
import pygame
from os import path

class SpriteSheet:
    def __init__(self, image_filename, data_filename):
        if path.isfile(image_filename) and path.isfile(data_filename):
            with open(data_filename) as file:
                self.dict = json.load(file)

            self.image = pygame.image.load(image_filename).convert_alpha()
        else:
            self.dict = {}
            self.image = pygame.Surface((0, 0))

    def get_image(self, name):
        if name in self.dict:
            return self.image, pygame.Rect(self.dict[name])

        return pygame.Surface((0, 0)), pygame.Rect(0, 0, 0, 0)