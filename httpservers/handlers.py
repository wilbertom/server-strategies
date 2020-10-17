from .serial_handler import SerialHandler
from .forking_handler import ForkingHandler
from .pre_forking_handler import PreForkingHandler


HANDLERS = {
    'serial': (SerialHandler, ),
    'forking': (ForkingHandler, ),
    'pre-forking': (PreForkingHandler, 4),
}
