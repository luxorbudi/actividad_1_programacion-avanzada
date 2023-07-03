import pygame
from pygame.surface import Surface
from abc import ABC, abstractmethod
import entities.configurations_entity as config

class GameObject(pygame.sprite.Sprite, ABC):

    def __init__(self, \
        configuration:config.Configurations):

        super().__init__()

        self.debug = configuration.debug
        self.rect = pygame.Rect(0, 0, 0, 0)
        self.render_rect = pygame.Rect(0, 0, 0, 0)
        self.position = pygame.math.Vector2(0.0, 0.0)


    @abstractmethod
    def handle_input(self, key, is_pressed):
        pass


    @abstractmethod
    def update(self, delta_time):
        pass


    @abstractmethod
    def render(self, surface_dst):
        pass


    @abstractmethod
    def release(self):
        pass


    def _center(self):
        self.rect.center = self.position.xy
        self.render_rect.center = self.position.xy


    def _render_debug(self, surface_dst:Surface):
        pygame.draw.rect(surface_dst, self.debug.collider_color, self.rect, 1)
        pygame.draw.rect(surface_dst, self.debug.render_color, self.render_rect, 1)