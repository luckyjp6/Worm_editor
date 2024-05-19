import tkinter as tk
import ttkbootstrap as ttkb

# def set_font(input_target, font):
#     wait_list = [input_target]
#     while wait_list:
#         target = wait_list.pop()
#         for widget in target.winfo_children():
#             try:
#                 widget.configure(font=font)
#                 wait_list.append(widget)
#             except tk.TclError:
#                 pass

font_size = [8, 9, 10, 11, 12, 14, 16, 18, 20, 22, 24, 26, 28, 36, 48, 72]
def add_all_fonts(font_family_menu, font_size_menu, file_manager):
    for f in tk.font.families():
        font_family_menu.add_command(label=f, command=lambda f=f: file_manager.set_font_family(f))
    
    for s in font_size:
        font_size_menu.add_command(label=s, command=lambda s=s: file_manager.set_font_size(s))

def add_all_themes(theme_menu, root):
    for tt in ttkb.Style().theme_names():
        theme_menu.add_command(label=tt, command=lambda t=tt: root.set_theme(t))
