class HandlerException(Exception):
    pass


class HandlerStopped(HandlerException):
    pass


class HandlerWriteError(HandlerException):
    pass
