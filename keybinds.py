#!/usr/bin/env python3
from prompt_toolkit.key_binding import KeyBindings
'''from Cochra import hotdog_initiation'''

mainkeybinds = KeyBindings()

@mainkeybinds.add('escape', 'q')
def exit_(event):
    event.app.exit()
        
'''@mainkeybinds.add('c-h')
def hotdog_stand_(event):
    hotdog_initiation()'''