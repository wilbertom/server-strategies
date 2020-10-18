from socket import SHUT_RDWR
from .handler import Handler
import os
import sys


class ForkingHandler(Handler):

    def __init__(self, socket):
        super().__init__(socket)
        self._pids = []

    def cleanup(self):
        while self._pids:
            pid = self._pids.pop()
            os.waitpid(pid, 0)

    def handle(self):
        (clientsocket, address) = self.socket.accept()
        clientsocket.settimeout(60)

        try:
            pid = os.fork()

            if pid == 0:
                self._send_response(clientsocket)

                clientsocket.shutdown(SHUT_RDWR)
                clientsocket.close()

                sys.exit(0)

            else:
                self._pids.append(pid)

        except OSError as e:
            print(str(e))
            print('x')
