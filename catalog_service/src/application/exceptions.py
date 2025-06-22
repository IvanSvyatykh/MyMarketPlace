

class ApplicationException(Exception):

    def __init__(self, code:int, message=None ):
        self.message = message
        self.code = code
