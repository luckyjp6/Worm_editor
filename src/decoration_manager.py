import ttkbootstrap as ttk

class Decoration_manager():
    def __init__(self, root):
        self.style = ttk.Style(root)
    def change_theme(self, theme_name):
        self.style.theme_use(theme_name)
    