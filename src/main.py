import tkinter as tk

from menu import ScrollableMenu
from font_and_theme import add_all_fonts, add_all_themes
from root_window import Root_window
from file_manager import File_manager
from decoration_manager import Decoration_manager

# main window instance
root = Root_window()


# TODO: separate menu implementation
file_manager = File_manager(root.root, root.default_font)
# decoration_manager = Decoration_manager(root.root)

# setting menu
root_menu = tk.Menu(root.root, font=root.default_font)
root.root.config(menu=root_menu)
root.root.bind('<Control-w>', file_manager.close_file)
root.root.bind('<Control-n>', file_manager.new_file_event)
root.root.bind('<Control-r>', file_manager.refresh_file)
root.root.bind('<Control-s>', file_manager.save_file)
root.root.bind('<Control-+>', file_manager.increase_font_size)
root.root.bind('<Control-minus>', file_manager.decrease_font_size)
root.root.bind('<Control-MouseWheel>', file_manager.increase_or_decrease_font_size)

function_menu = tk.Menu()

file_menu = tk.Menu(root_menu)#, tearoff=1)
root_menu.add_cascade(label='File', menu=file_menu)
file_menu.add_command(label='New File', command=file_manager.new_file, accelerator='ctrl+n')
file_menu.add_command(label='Open File', command=file_manager.open_file)
file_menu.add_separator()

decoration_menu = tk.Menu(root_menu)#, tearoff=0)
root_menu.add_cascade(label='Decoration', menu=decoration_menu)

font_family_menu = tk.Menu(decoration_menu, tearoff=0)
font_size_menu = tk.Menu(decoration_menu, tearoff=0)
decoration_menu.add_cascade(label='Change Font Family', menu=font_family_menu)
decoration_menu.add_cascade(label='Change Font Size', menu=font_size_menu)
add_all_fonts(font_family_menu, font_size_menu, file_manager)

theme_menu = tk.Menu(decoration_menu, tearoff=0)
decoration_menu.add_cascade(label='Change Theme', menu=theme_menu)
add_all_themes(theme_menu, root)


# set_font(root.root, root.default_font)
file_manager.set_font(font=root.default_font)

# start displaying
root.root.mainloop()