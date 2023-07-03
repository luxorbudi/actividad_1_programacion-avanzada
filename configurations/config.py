import json
import utils.path as path
import utils.reflection as reflection
import entities.configurations_entity as configurations

class Config:

    def __init__(self):
        self.path = path.Path()
        self.reflection = reflection.Reflection()
        self.configurations = configurations.Configurations()

        self.__load_config()


    def __load_config(self):
        json_configurations = self. \
            path.final_path(__file__, 'config.json')

        with open(json_configurations, 'r') as file:
            self.configurations = \
                self.reflection.map_class( \
                    json.load(file), self.configurations)