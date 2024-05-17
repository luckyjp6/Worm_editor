import tkinter as tk
from tkinter import ttk, filedialog
from file import File, File_status

class File_manager():
    def __init__(self, parent):
        self.note_book = ttk.Notebook(parent)
        self.note_book.pack(expand=True, fill='both')

        self.default_file_name = 'new file'
        self.files = []
        self.new_file_counter_max = 0

        # TODO: first file
        self.new_file()

    def close_file(self, event=None):
        # get current file
        index = self.note_book.index(self.note_book.select())
        file = self.files[index]

        # remove entry
        file.close()
        self.note_book.forget(index)
        self.files.remove(file)

        # Remove file path for "same file name" situation if needed
        same_name = -1
        for i in range(len(self.files)):
            if self.files[i].name == file.name: 
                if same_name >= 0: return # still more than one same-name file, no need to remove
                same_name = i
        if same_name < 0: return
        self.note_book.tab(same_name, text=self.files[same_name].name)


    def refresh_file(self, event=None):
        # get current file
        index = self.note_book.index(self.note_book.select())
        # do refresh
        self.files[index].refresh()

    def new_file_event(self, event=None):
        self.new_file()
    def new_file(self, name=None):        
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

        else: # new file
            display_name = self.default_file_name
            if self.new_file_counter_max > 0: 
                display_name += f' ({self.new_file_counter_max})'
            new_f = File(self.note_book, display_name)
            self.new_file_counter_max += 1
        
        # add display
        self.note_book.add(new_f.text_area, text=display_name)
        # display
        self.note_book.select(len(self.files))
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
    
    def save_file(self, event=None):
        # get current file
        index = self.note_book.index(self.note_book.select())
        file = self.files[index]

        if file.file_path is None:
            file.file_path = filedialog.asksaveasfilename(
                defaultextension='.txt',
                initialfile=file.name,
                filetypes=[('Text files', '*.txt'), 
                        ('C/C++ file', '*.c;*.cpp'),
                        ('Python files', '*.py'),
                        ('Java files', '*.'),
                        ('All files', '*.*')]
            )
        if file.file_path is not None:
            self.files[index].save()

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