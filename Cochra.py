#!/usr/bin/env python3
from prompt_toolkit import Application
from prompt_toolkit.key_binding import KeyBindings
import keybinds

def main():
    cochra = Application(key_bindings=keybinds.mainkeybinds, full_screen=True)
    cochra.run()


if __name__ == '__main__':
    import sys
    main()
