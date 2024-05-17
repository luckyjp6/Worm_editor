import tkinter as tk
from tkinter import scrolledtext, messagebox
from enum import Enum

class File_status(Enum):
    empty = "empty"         # not yet started editting
    saved = "saved"         # saved to file_path
    changed = "changed"     # already changed content
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

    def refresh(self):
        f = ''
        try:
            f = open(self.file_path)
        except:
            messagebox.showerror("Error", f"Fail to open {self.name}")
            self.status = File_status.error
            return
        
        now_cursor = self.text_area.index('insert')
        self.text_area.delete(1.0, 'end')
        self.text_area.insert(tk.INSERT, f.read())
        self.text_area.mark_set('insert', now_cursor)

    def save(self):
        if self.file_path is None:
            messagebox.showerror('Unexpected error', 'file_path is None in file.py save()')
            return
        f = ''
        try:
            f = open(self.file_path, 'w')
        except Exception as e:
            messagebox.showerror('Error', f'Fail to save {self.name}')
            return
        f.write(self.text_area.get(1.0, tk.END))

    def update_content(self, close=False):
        if self.status == File_status.error: return
        if self.status == File_status.empty and close == False:
            self.refresh()
            return
        # if self.status
    
    def close(self):

        if self.status == File_status.empty \
            or self.status == File_status.saved \
            or self.status == File_status.error: return
        
        if self.status == File_status.changed:
            self.update_content()