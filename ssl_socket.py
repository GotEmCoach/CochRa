#!/usr/bin/env python3
import socketserver




def startlistener(port, verbose, ipaddr):
    with socketserver.ThreadingTCPServer((ipaddr, port), listenerhandler) as server:
        server.serve_forever()


class listenerhandler(socketserver.StreamRequestHandler):
    def handle(self):
        while True:
            print('not doe.')
        