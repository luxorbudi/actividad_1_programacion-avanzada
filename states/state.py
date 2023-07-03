from abc import ABC
from abc import abstractmethod
import utils.constants as constants

class State(ABC):
    def __init__(self):
        self.done = False
        self.next_state = constants.STRING_EMPTY
        self.previous_state = constants.STRING_EMPTY

    @abstractmethod
    def handle_input(self, event):
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

    @abstractmethod
    def enter(self):
        pass

    @abstractmethod
    def exit(self):
        pass