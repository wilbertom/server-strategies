from socket import socket, AF_INET, SOCK_STREAM, SHUT_RDWR
import os
import signal
from .exceptions import HandlerException, HandlerStopped


class Server:

    def __init__(self, host, port, handler_cls, *handler_args):
        self._host = host
        self._port = port
        self._backlog = 0
        self._server_pid = os.getpid()
        self._socket = socket(AF_INET, SOCK_STREAM)

        self._handler_cls = handler_cls
        self._handler_args = handler_args
        self._handler = None

        signal.signal(signal.SIGUSR1, self._cleanup_signal)

    def run(self):
        if self._server:
            self._log(f'listening - http://{self._host}:{self._port}')

            self._socket.bind((self._host, self._port))
            self._socket.listen(self._backlog)

            self._log('starting handler')
            self._handler = self._handler_cls(self._socket, *self._handler_args)

        while True:
            try:
                self._handler.handle()

            except KeyboardInterrupt:
                self._log(f'keyboard interrupt')
                break
            except HandlerException as e:
                self._log(f'handler - {str(e)}')


        self.stop()

        return

    def stop(self):
        self._log(f'stopping')

        try:
            self._handler.cleanup()
        except HandlerStopped as e:
            self._log('handler - already cleaned up')

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
