from socket import SHUT_RDWR
from .handler import Handler
import os
import sys


class ForkingHandler(Handler):

    def __init__(self):
        self._pids = []

    def cleanup(self):
        while self._pids:
            pid = self._pids.pop()
            os.waitpid(pid, 0)

    def handle(self, clientsocket, address):
        try:
            pid = os.fork()

            if pid == 0:
                self._log('handling request')
                self._send_hello_world(clientsocket)

                clientsocket.shutdown(SHUT_RDWR)
                clientsocket.close()
                self._log('handled request')

                sys.exit(0)

            else:
                self._pids.append(pid)

        except OSError as e:
            print(str(e))
            print('x')
