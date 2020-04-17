#!/usr/bin/env python3

import argparse

ssl_listener = argparse.ArgumentParser()
ssl_listener.add_argument('-p', '--listenport', type=int, help='Port to listen on.')
ssl_listener.add_argument('-v', '--verbose', action='store_true', help='verbose_mode')
ssl_listener.add_argument('-a', '--listenaddress', default='127.0.0.1',type=str, help='listen ip address, default is loopback.')


yeetshell = argparse.ArgumentParser()
yeetshell.add_argument('-s', '--session', type=int, help='session to start yeeting things.')


