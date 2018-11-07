import importlib

class BaseParser:
    def preprocess(self, payload):
        return [None]
    pass

    def insertItems(self, items):
        pass

PARSERS = {
    '1': 'otp',
    '2': 'regular',
    '3': 'mixed',
    '4': 'raw'
}

def dispatch(type):
    type = str(type)
    if type not in PARSERS:
        return None
    module = importlib.import_module('smartimport.processors.' + PARSERS[type])
    return module.dispatch()
