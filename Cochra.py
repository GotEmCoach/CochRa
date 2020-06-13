#!/usr/bin/env python3
from prompt_toolkit import Application
from prompt_toolkit.key_binding import KeyBindings
import keybinds
import mainlayout
from prompt_toolkit.styles import Style, style_from_pygments_cls


class CochRa:
    def __init__(self):
        self.app = Application(
            layout=mainlayout.mainlay(),
            key_bindings=keybinds.mainkeybinds,
            full_screen=True,
            mouse_support=True,

        )

if __name__ == '__main__':
    import sys
    Cochra()
