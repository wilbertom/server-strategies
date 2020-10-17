import argparse
import sys
import logging
from httpservers import Server, HANDLERS


def main(args):
    handler_cls = HANDLERS[args.handler]
    handler = handler_cls()

    server = Server(args.host, args.port, handler)

    server.run()

    return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('host')
    parser.add_argument('port', type=int)
    parser.add_argument('handler')


    args = parser.parse_args()

    sys.exit(main(args))
