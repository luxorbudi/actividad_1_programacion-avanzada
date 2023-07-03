import utils.constants as constants

class ReflectionException(Exception):
    def __init__(self):
        super().__init__(constants.STRING_EMPTY)