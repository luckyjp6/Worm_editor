import tkinter as tk

def set_font(input_target, font):
    wait_list = [input_target]
    while wait_list:
        target = wait_list.pop()
        for widget in target.winfo_children():
            try:
                widget.configure(font=font)
                wait_list.append(widget)
            except tk.TclError:
                pass