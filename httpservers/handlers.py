from .serial_handler import SerialHandler
from .forking_handler import ForkingHandler

HANDLERS = {
    'serial': SerialHandler,
    'forking': ForkingHandler,
}