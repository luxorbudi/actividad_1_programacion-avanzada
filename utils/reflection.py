import copy
from typing import TypeVar
import exceptions.reflection_exception as exception

class Reflection:
    T = TypeVar("T")

    def class_properties(self, t: T):
        properties = []

        if hasattr(t, '__annotations__'):
            for attribute in t.__annotations__:
                properties.append(attribute)

            for property, value in vars(t).items():
                properties.append(property)

            properties = list(dict.fromkeys(properties))

        else:
            for property, value in vars(t).items():
                properties.append(property)

        return properties
    
    def is_class(self, clazz):
        return str(type(clazz)).startswith("<class") and hasattr(clazz, '__weakref__')

    def get_class_attribute(self, t:T, object_property):
        try:
            return getattr(t, object_property)
        except Exception:
            return None

    def map_class(self, dict_data, t:T):
        object_properties = self.class_properties(t)

        for object_property in object_properties:
            property_entity = self. \
                get_class_attribute(t, object_property)

            if property_entity is None:
                setattr(t, \
                    object_property, \
                        dict_data[object_property])

            else:
                if self.is_class(property_entity):
                    self.map_class(dict_data[object_property], property_entity)

        return t