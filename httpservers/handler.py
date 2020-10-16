
class Handler:
    """

    """

    def handle(self, clientsocket, address):
        raise NotImplementedError

    def _send_hello_world(self, clientsocket):
        content = b"hello, world\r\n" 
        data = b"HTTP/1.1 200 OK\r\nConnection: close\r\nCONTENT-LENGTH: %d\r\n\r\n%s" % (len(content), content)
        clientsocket.send(data)
