from socket import SHUT_RDWR
from .handler import Handler
import os
import sys


class PreForkingHandler(Handler):

    def __init__(self, socket, size):
        super().__init__(socket)

        self._size = size

        self._pids = []

        self._in_parent = None
        self._in_child = None

        for _ in range(size):
            pid = os.fork()
            self._in_parent = pid != 0
            self._in_child = not self._in_parent

            if self._in_parent:
                self._pids.append(pid)

            if self._in_child:
                break

    def handle(self):
        if self._in_child:
            (clientsocket, address) = self.socket.accept()
            clientsocket.settimeout(60)

            try:
                self._send_hello_world(clientsocket)

                clientsocket.shutdown(SHUT_RDWR)
                clientsocket.close()

            except OSError as e:
                self._log(str(e))
                sys.exit(1)

        else:
            self.cleanup()

    def cleanup(self):
        if self._in_parent:
            self._log('cleaning up')
            while self._pids:
                pid = self._pids.pop()
                self._log(f'waiting to finish - {pid}')
                os.waitpid(pid, 0)
        else:
            self._log('tried to cleanup in child')
