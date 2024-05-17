import tkinter as tk

from font import set_font
from root_window import Root_window
from file_manager import File_manager

# style = ttkb.Style(theme='vapor')
# test = style.master
# test.title("Test for ttkb")
# test.geometry("800x600")
# test.minsize(300, 200)

# main window instance
root = Root_window()

file_manager = File_manager(root.root)

# setting menu
menu_bar = tk.Menu(root.root, font=root.default_font)
root.root.config(menu=menu_bar)
root.root.bind('<Control-w>', file_manager.close_file)
root.root.bind('<Control-n>', file_manager.new_file_event)
root.root.bind('<Control-r>', file_manager.refresh_file)
root.root.bind('<Control-s>', file_manager.save_file)

file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New File", command=file_manager.new_file)
file_menu.add_command(label="Open File", command=file_manager.open_file)
file_menu.add_separator()


# text_area1.insert(tk.INSERT, "test")



# set_font(menu_bar, root.default_font)
set_font(root.root, root.default_font)
file_manager.set_font(root.default_font)

# start displaying
root.root.mainloop()