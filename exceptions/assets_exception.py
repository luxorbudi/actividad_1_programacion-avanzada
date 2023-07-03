import utils.messages as messages

class AssetsException(Exception):
    def __init__(self):
        super().__init__(messages.SINGLETON_EXCEPTION % (messages.ASSETS_EXCEPTION))