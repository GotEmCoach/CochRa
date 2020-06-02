#!/usr/bin/env python3
from prompt_toolkit.key_binding import KeyBindings


mainkeybinds = KeyBindings()

@mainkeybinds.add('escape', 'q')
def exit_(event):
    event.app.exit()
        
