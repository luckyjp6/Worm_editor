import tkinter as tk
import ttkbootstrap as ttkb

class Root_window():
    def __init__(self):
        self.default_weight = 800
        self.default_height = 600
        self.default_x_pad = 10
        self.default_y_pad = 10
        self.default_font = ('Consolas', 16)

        # default setting
        style = ttkb.Style(theme='minty') # minty, vapor, morph
        self.root = style.master
        self.root.title('Worm Simple Text Editor')
        self.root.iconbitmap('D:/repo/text_editor_python/img_src/icon.ico')
        self.root.geometry(f'{self.default_weight}x{self.default_height}+{self.default_x_pad}+{self.default_y_pad}') # TODO: full-screen or 

