import tkinter as tk
from tkinter import scrolledtext, messagebox
from enum import Enum
from tkhtmlview import HTMLLabel
import markdown

class File_status(Enum):
    empty = "empty"         # not yet started editting
    saved = "saved"         # saved to file_path
    changed = "changed"     # already changed content
    error = "error"         # error, please discard or handle it

class File():
    def __init__(self, parent, name, open=False):
        self.name = name
        self.file_path = None
        self.frame = tk.Frame(parent)
        self.text_area = scrolledtext.ScrolledText(self.frame, undo=True, wrap=tk.WORD, height=10)

        if self.name.endswith('.md'):  # TODO: button to close display
            self.is_md = True
            self.display_area = HTMLLabel(self.frame, html='', width=50, height=10)
            self.display_area.pack(side='right', expand=True, fill='both')
            self.text_area.pack(side='left', expand=True, fill='both')
            self.text_area.bind('<KeyRelease>', self.update_preview) # TODO: less frequecy update
        else:
            self.is_md = False
            self.text_area.pack(expand=True, fill='both')


        self.status = File_status.empty

        if open:
            self.file_path = self.name
            self.name = self.file_path.split('/')[-1]
            self.update_content()

    def update_preview(self, event=None):
        new_preview = markdown.markdown(self.text_area.get('1.0', tk.END))
        self.display_area.set_html(new_preview)

    def refresh(self):
        f = ''
        try:
            f = open(self.file_path)
        except:
            messagebox.showerror("Error", f"Fail to open {self.name}")
            self.status = File_status.error
            return
        
        # maintain cursor position (part 1)
        now_cursor = self.text_area.index('insert')

        self.text_area.delete('1.0', tk.END)
        self.text_area.insert(tk.INSERT, f.read())

        # update preview for .md file
        if self.is_md: self.update_preview()

        # maintain cursor position (part 2)
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
        f.write(self.text_area.get('1.0', tk.END))

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