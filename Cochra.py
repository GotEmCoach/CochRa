#!/usr/bin/env python3
# coding=utf-8
"""

"""
import argparse
import random
import ssl_socket
import yeetshell

import parsers
import cmd2


class Cochra(cmd2.Cmd):
    """ Main Platform for Cochra """

    # Setting this true makes it run a shell command if a cmd2/cmd command doesn't exist
    # default_to_shell = True

    def __init__(self):
        shortcuts = cmd2.DEFAULT_SHORTCUTS
        super().__init__(shortcuts=shortcuts)
        self.prompt = 'Cochra#$!>> '
        self.persistent_history_file = '~/.cochra_hist'
        self._persistent_history_length = '400000000000'
        


    @cmd2.with_argparser(parsers.ssl_listener)
    def do_ssl_listener(self, args: argparse.Namespace):
        """ think ncat like session """
        ssl_socket.startlistener(args.listenport, args.verbose, args.listenaddress)


    @cmd2.with_argparser(parsers.yeetshell)
    def do_yeetshell(self, args: argparse.Namespace):
        """ Need to implement session like objects to hook into. """
        yeetshell.hooksession(args.session)

if __name__ == '__main__':
    import sys
    c = Cochra()
    sys.exit(c.cmdloop())
