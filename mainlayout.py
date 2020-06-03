#!/usr/bin/env python3

from prompt_toolkit.layout.containers import VSplit, HSplit, Window, WindowAlign
from prompt_toolkit.buffer import Buffer
from prompt_toolkit.layout.controls import BufferControl, FormattedTextControl
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.layout.layout import UIControl
from prompt_toolkit import PromptSession, prompt
import styleguide


def main():
    Title = prompt('Enter the Title for the Main Window', )
    leftprompt = PromptSession('MainCochra>> ')
    prompts = createprompts()
    buffers = assignbufs(prompts)

    wins = assignwins(buffers)

def createprompts():
    


def assignbufs(prompts):
    buffers = [
        top_right_buf = Buffer()
        bottom_right_buf = Buffer()
        left_buf = Buffer()
    ]
    return buffers

def assignwins():
    wins = [
        left_win = Window(BufferControl(buffer=buffers), FormattedTextControl())
        top_right_win = Window(BufferControl(buffer=top_right_buf))
        bottom_right_win = Window(BufferControl(buffer=bottom_right_buf))
    ]
    return wins 

body_container = HSplit(
    [
        top_right_win,
        Window(height=1,char='-', style='class:line'),
        bottom_right_win
    ]
)

root_container = VSplit(
    [
        left_win,
        Window(width=1, char='|', style="class:line"),
        body_container

    ]
)



initiallayout = Layout(root_container, focused_element=left_win)



        