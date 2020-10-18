import os
from .exceptions import HandlerWriteError


class Handler:
    """

    """

    def __init__(self, socket):
        self.socket = socket

    def handle(self):
        raise NotImplementedError

    def cleanup(self):
        pass

    def _send_response(self, clientsocket):
        #                10240 is one chunk in requests library
        content = b"1" * 10240 * 10

        response = b"HTTP/1.1 200 OK\r\n"
        response += b"Connection: close\r\n"
        response += b"CONTENT-LENGTH: %d\r\n" % (len(content), )

        response += b"\r\n"
        response += b"%s" % (content, )

        result = clientsocket.sendall(response)

        if result is not None:
            raise HandlerWriteError(f'Failed to write: {result}')

    def _log(self, message):
        print(f'client - {os.getpid()} - {message}')

        return self
