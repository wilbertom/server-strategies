from socket import SHUT_RDWR
from .handler import Handler
import os
import sys
from .thread_pool import ThreadPool


class ThreadPoolHandler(Handler):

    def __init__(self, socket, size):
        super().__init__(socket)
        self._thread_pool = ThreadPool(size, self._handle)

    def handle(self):
        (clientsocket, address) = self.socket.accept()
        clientsocket.settimeout(60)
        self._thread_pool.put((clientsocket, address))

    def _handle(self, item):
        (clientsocket, address) = item

        self._send_response(clientsocket)

        clientsocket.shutdown(SHUT_RDWR)
        clientsocket.close()

    def cleanup(self):
        # can't clean up threadpool since we can cleanup multiple times
        pass