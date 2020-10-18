#!/usr/bin/env python

import argparse
import sys
import logging
from httpservers import Server, HANDLERS


def main(args):
    handler_cls, *handler_args = HANDLERS[args.handler]

    server = Server(args.host, args.port, handler_cls, *handler_args)

    server.run()

    return 0


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('host')
    parser.add_argument('port', type=int)
    parser.add_argument('handler')


    args = parser.parse_args()

    sys.exit(main(args))
