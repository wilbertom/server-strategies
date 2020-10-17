from socket import socket, AF_INET, SOCK_STREAM, SHUT_RDWR
import os
import signal


class Server:

    def __init__(self, host, port, handler):
        self._host = host
        self._port = port
        self._handler = handler
        self._backlog = 0
        self._socket = socket(AF_INET, SOCK_STREAM)
        self._server_pid = os.getpid()

        signal.signal(signal.SIGUSR1, self._cleanup_signal)

    def run(self):
        self._log(f'running on http://{self._host}:{self._port}')

        self._socket.bind((self._host, self._port))
        self._socket.listen(self._backlog)

        while True:
            try:
                (clientsocket, address) = self._socket.accept()
                clientsocket.settimeout(60)
                self._handler.handle(clientsocket, address)

            except KeyboardInterrupt:
                self._log(f'keyboard interrupt')
                break

        self.stop()

        return

    def stop(self):
        self._log(f'stopping')
        self._handler.cleanup()
        self._socket.close()
        self._log(f'stopped')

    def _cleanup_signal(self, *args):
        self._log(f'cleaning up {args}')
        self._handler.cleanup()

    def _log(self, message):
        print(f'server - {os.getpid()} - {message}')

        return self

    @property
    def _server(self):
        return os.getpid() == self._server_pid
