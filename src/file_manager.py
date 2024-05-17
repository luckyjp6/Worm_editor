import tkinter as tk
from tkinter import ttk, filedialog
from file import File, File_status

class File_manager():
    def __init__(self, parent):
        self.note_book = ttk.Notebook(parent)
        self.note_book.pack(expand=True, fill='both')

        self.default_file_name = 'new file'
        self.files = []

    def new_file(self, name=None):
        new_file_conter = 0
        for f in self.files:
            if f.name == self.default_file_name: new_file_conter += 1
        
        new_f = ''
        display_name = name
        if name is not None: # open file
            new_f = File(self.note_book, name, open=True)
            if new_f.status == File_status.error:
                return
            
            display_name = new_f.name
            same_name_idx = []
            for i in range(len(self.files)):
                f = self.files[i]
                if f.name == new_f.name: same_name_idx.append(i)
            if same_name_idx:
                display_name = f'{new_f.name} ({new_f.file_path})'
                for i in same_name_idx:
                    f = self.files[i]
                    self.note_book.tab(i, text=f'{f.name} ({f.file_path})')

        elif new_file_conter == 0: # new file
            display_name = self.default_file_name
            new_f = File(self.note_book, self.default_file_name)
        else: # new file
            display_name = f'{self.default_file_name}({new_file_conter})'
            new_f = File(self.note_book, f'{self.default_file_name}({new_file_conter})')
        
        # add display
        self.note_book.add(new_f.text_area, text=display_name)
        # store object
        self.files.append(new_f)
        return new_f
    
    def open_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[('All files', '*.*'),
                    ('Text files', '*.txt'), 
                    ('C/C++ file', '*.c;*.cpp'),
                    ('Python files', '*.py'),
                    ('Java files', '*.')]
        )
        if not file_path:
            return

        
        self.new_file(file_path)
    
    def check_and_update(self):
        wait_for_delete = []
        for f in self.files:
            f.update_content()

            if f.status == File_status.error:
                wait_for_delete.append(f)
                continue
        for f in wait_for_delete:
            self.files.remove(f)

    def set_font(self, font):
        for f in self.files:
            try:
                f.text_area.configure(font=font)
            except tk.TclError:
                pass