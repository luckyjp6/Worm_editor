import tkinter as tk
from tkinter import scrolledtext, messagebox
from enum import Enum

class File_status(Enum):
    empty = "empty"         # not yet started editting
    changed = "changed"     # already changed content
    saved = "saved"         # saved to file_path
    error = "error"         # error, please discard or handle it

class File():
    def __init__(self, parent, name, open=False):
        self.name = name
        self.file_path = None
        self.text_area = scrolledtext.ScrolledText(parent, undo=True, wrap=tk.WORD)
        self.text_area.pack(expand=True, fill='both', padx=10, pady=10)
        self.status = File_status.empty

        if open:
            self.file_path = self.name
            self.name = self.file_path.split('/')[-1]
            self.update_content()
            
    def update_content(self):
        if self.status == File_status.error: return

        # TODO: priority of read and write
        f = ''
        try:
            f = open(self.file_path)
        except:
            messagebox.showerror("Error", f"Fail to open {self.name}")
            self.status = File_status.error
            return
        
        self.text_area.insert(tk.INSERT, f.read())
        self.status = File_status.saved
