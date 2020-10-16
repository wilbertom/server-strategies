from socket import SHUT_RDWR
from .handler import Handler


class SerialHandler(Handler):

    def handle(self, clientsocket, address):
        # print(f"{id(clientsocket)} {address} - handling request from")

        self._send_hello_world(clientsocket)

        clientsocket.shutdown(SHUT_RDWR)
        clientsocket.close()

        # print(f"{id(clientsocket)} {address} - handled")
