import os
import pygame
from os import path
from pathlib import Path
import assets.asset as Asset
import exceptions.assets_exception as assetsexception

class AssetManager:

    __instance = None

    @staticmethod
    def instance():
        if AssetManager.__instance is None:
            AssetManager()
        return AssetManager.__instance

    def __init__(self):
        if AssetManager.__instance is None:
            AssetManager.__instance = self

            self.assets = {}

        else:
            raise assetsexception.AssetsException()


    def load(self, category, asset_type, asset_name, asset_filename_path, data_filename_path = None, font_size=0):
        parent_path:Path = Path(__file__).parent.parent

        asset_path:str = \
            os.path.join(parent_path, \
                os.path.join(*asset_filename_path))

        if path.isfile(asset_path) and asset_name not in self.assets:
            asset = Asset.Asset(asset_type, category)

            asset.load(asset_path, data_filename_path, font_size)

            self.assets[asset_name] = asset


    def get(self, asset_name, sheet_name = None):
        if sheet_name:
            if sheet_name in self.assets:
                return self.assets[sheet_name].payload.get_image(asset_name)

            return pygame.Surface((0, 0)), pygame.Rect(0, 0, 0, 0)

        else:
            if asset_name in self.assets:
                return self.assets[asset_name].payload

            else:
                return None


    def clean(self, category = None):
        if category:
            for k in list(self.assets.keys()):
                if self.assets[k].category == category:
                    del self.assets[k]
        else:
            self.assets = {}