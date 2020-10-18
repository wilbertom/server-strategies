import threading
from socket import SHUT_RDWR
from .handler import Handler
import os
import sys


def _target(handler, clientsocket, address):
    # handler._log(f'{threading.get_native_id()} - handling request')
    clientsocket.settimeout(60)

    try:
        handler._send_response(clientsocket)

        clientsocket.shutdown(SHUT_RDWR)
        clientsocket.close()

        sys.exit(0)

    except OSError as e:
        print(str(e))
        print('x')


class ThreadHandler(Handler):

    def handle(self):
        (clientsocket, address) = self.socket.accept()

        thread = threading.Thread(target=lambda: _target(self, clientsocket, address))
        thread.start()
