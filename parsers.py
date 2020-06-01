#!/usr/bin/env python3


import colored
import colorama
import argparse

ssl_listener = argparse.ArgumentParser()
ssl_listener.add_argument('-p', '--listenport', type=int, help='Port to listen on.')
ssl_listener.add_argument('-v', '--verbose', action='store_true', help='verbose_mode')
ssl_listener.add_argument('-a', '--listenaddress', default='127.0.0.1',type=str, help='listen ip address, default is loopback.')


yeetshell = argparse.ArgumentParser()
yeetshell.add_argument('-s', '--session', type=int, help='session to start yeeting things.')

colorscheme = argparse.ArgumentParser()
colorscheme.add_argument('-l', '--listschemes', type=str, help='list out possible colorschemes')
colorscheme.add_argument('-s', '--setscheme', type=int, help='Choose a number from list')
#colorscheme_list = 