from .serial_handler import SerialHandler
from .forking_handler import ForkingHandler
from .pre_forking_handler import PreForkingHandler
from .thread_handler import ThreadHandler
from .thread_pool_handler import ThreadPoolHandler


HANDLERS = {
    'serial': (SerialHandler, ),
    'forking': (ForkingHandler, ),
    'pre-forking-2': (PreForkingHandler, 2),
    'pre-forking-4': (PreForkingHandler, 4),
    'pre-forking-8': (PreForkingHandler, 8),
    'pre-forking-12': (PreForkingHandler, 12),
    'thread': (ThreadHandler, ),
    'thread-pool-2': (ThreadPoolHandler, 2),
    'thread-pool-12': (ThreadPoolHandler, 12),
}
