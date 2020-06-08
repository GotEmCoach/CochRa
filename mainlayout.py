#!/usr/bin/env python3

from prompt_toolkit.layout.containers import VSplit, HSplit, Window, WindowAlign
from prompt_toolkit.buffer import Buffer
from prompt_toolkit.layout.controls import BufferControl, FormattedTextControl
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.layout.layout import UIControl
from prompt_toolkit import PromptSession, prompt
import styleguide
import pygments
import yaml



def buildapp():
    colors = themeselection()
    prompts = createprompts(theme)
    buffers = assignbufs(prompts)
    wins = assignwins(buffers)
    containers = buildcontainers(wins)
    return containers

def themeselection():
    with open('themes.yml', 'r') as themes:
        themenames = yaml.load_all(themes, Loader=yaml.FullLoader)
        for themenum in themenames:
            themeselection = input('Enter the number selection for the theme: ')

def createstyle(colors):
    currenttheme = Style([
        ('TabTitle', 'Color1'),
        ('TabBack', 'Color3'),
        ('WinMainWords', 'Color3'),
        ('WinMainBack','Color1'),
        ('WinFirstWords', 'Color2'),
        ('Output', 'Color6'),
        ('HelpBack', 'Color5'),
        ('HelpWords', 'Color4'),
        ('EditorBack', 'Color3'),
        ('EditorWord', 'Color1'),
        ('CommandMode', 'Color2')
    ])


def createprompts():
    Title = prompt('Enter the Title for the Main Window', )
    leftprompt = PromptSession('MainCochra>> ')
    leftprompt.style_transformation.transform_attrs()

def assignbufs(prompts):
    top_right_buf = Buffer(),
    bottom_right_buf = Buffer(),
    left_buf = Buffer()
    buffers = [
        top_right_buf,
        bottom_right_buf,
        left_buf    
    ]
    return buffers

def assignwins():
    left_win = Window(BufferControl(buffer=buffers), FormattedTextControl())
    top_right_win = Window(BufferControl(buffer=top_right_buf))
    bottom_right_win = Window(BufferControl(buffer=bottom_right_buf))
    wins = [
        left_win,
        top_right_win,
        bottom_right_win    
    ]
    return wins 

def buildcontainers():
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
    return initiallayout





        