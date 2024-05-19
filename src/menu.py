import tkinter as tk

class ScrollableMenu(tk.Menu):
    def __init__(self, master, **kwargs):
        tk.Menu.__init__(self, master, **kwargs)
        self.bind('<MouseWheel>', self.on_mouse_wheel)

        self.start_idx = 0
        self.range = 15

        self.menu_items = []
    
    def add_command(self, label, command):
        self.menu_items.append((label, command))
        self.refresh()

    def on_mouse_wheel(self, event):
        print("on_mouse_wheel")
        if event.delta > 0:
            # if self.start_idx <= 0: return
            self.start_idx -= 1
        else:
            # if self.start_idx + self.range > len(self.menu_items): return
            self.start_idx += 1
        self.refresh()
    
    def refresh(self):
        self.delete(0, tk.END)
        end_idx = self.start_idx + self.range
        visible_items = self.menu_items[self.start_idx:end_idx]

        for label, command in visible_items:
            tk.Menu.add_command(self, label=label, command=command)