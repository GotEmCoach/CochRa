#!/usr/bin/env python3
from prompt_toolkit import Application
from prompt_toolkit.key_binding import KeyBindings
import keybinds
import mainlayout
from prompt_toolkit.styles import Style, style_from_pygments_cls

def main():
    cochra = Application(
        layout=mainlayout.initiallayout,
        key_bindings=keybinds.mainkeybinds, 
        full_screen=True,
        mouse_support=True
        )
    cochra.run()

    

def hotdog_initiation():
    hdstyle = Style.from_dict({
        'bgcolor' : 'bg:#ff0000'
    })
    mainlayout.left_win.style=hdstyle

if __name__ == '__main__':
    import sys
    main()
