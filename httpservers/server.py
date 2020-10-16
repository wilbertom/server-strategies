from socket import socket, AF_INET, SOCK_STREAM, SHUT_RDWR


class Server:
    
    def __init__(self, host, port, handler):
        self._host = host
        self._port = port
        self._handler = handler
        self._backlog = 0
        self._socket = socket(AF_INET, SOCK_STREAM)

    def run(self):
        print(f'server - running on http://{self._host}:{self._port}')

        self._socket.bind((self._host, self._port))
        self._socket.listen(self._backlog)

        while True:
            try:
                (clientsocket, address) = self._socket.accept()
                clientsocket.settimeout(60)
                # print(f"{id(clientsocket)} {address} - received connection")
                self._handler.handle(clientsocket, address)

            except KeyboardInterrupt:
                print("\nserver - keyboard interrupt")
                self._socket.close()
                break
            except ConnectionResetError:
                clientsocket.shutdown(SHUT_RDWR)
                clientsocket.close()
                print('x', end='')

        self._socket.close()

        return
