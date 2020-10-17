from socket import SHUT_RDWR
from .handler import Handler


class SerialHandler(Handler):

    def handle(self):
        (clientsocket, address) = self.socket.accept()
        clientsocket.settimeout(60)

        self._send_hello_world(clientsocket)

        clientsocket.shutdown(SHUT_RDWR)
        clientsocket.close()
