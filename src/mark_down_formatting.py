import tkinter as tk

class Mark_down_formatting():
    def __init__(self, text):
        self.text = text

        self.cache = ''
        self.status = ''
        
        # configure
        self.text.tag_config('default', font=('Helvetica', 16, 'bold'))
        self.text.tag_config('header', font=('Helvetica', 36, 'bold'))
    
    def clear(self):
        self.cache = ''
        # self.status = ''
    def set_default(self):
        cursor_pos = self.text.index(tk.INSERT)
        self.text.tag_add('default', cursor_pos, 'end')
    def apply(self, event):
        if event.keysym == 'BackSpace': 
            self.cache = self.cache[:-1]
            return
        if event.keysym == 'Return': 
            self.clear()
            self.set_default()
            return

        self.cache += event.char
        print(event)
        print(f'\'{self.cache}\'')
        # process ongoing status
        # if self.status == 'header':
            

        # check new pattern
        if self.cache.startswith('# '):
            cursor_pos = self.text.index(tk.INSERT)
            row = (int)(cursor_pos.split('.')[0])
            
            if self.cache == '# ': self.text.delete(f'{row}.{0}', f'{row}.{0}')
            else: # for bug purpose
                self.text.tag_add('header', f'{row}.{0}', f'end') # change the whole line
                self.cache = ''

#     cursor_pos = self.text.index(tk.INSERT)
#     row, col = map(int, cursor_pos.split('.'))

# TODO: 再重新思考下架構，因為這個檔案室要被存起來的，
# TODO: 光標改變要清空cache
# TODO: 再次backspace要刪除pattern，可以用self.cache跟backspace的互動去做，應該要搭配status
