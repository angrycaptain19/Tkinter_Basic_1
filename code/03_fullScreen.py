#%%

import tkinter as tk
from PIL import Image, ImageTk
import platform

# window.update()
# win_size = min( window.winfo_width(), window.winfo_height())
# print(win_size)

class APP:

    def __init__(self):

        self.window = tk.Tk()
        self.window.title('Window')

        self.align_mode = 'nsew'
        self.pad = 5

        self.div_size = 200
        self.img_size = self.div_size * 2
        self.div1 = tk.Frame(self.window,  width=self.img_size , height=self.img_size , bg='blue')
        self.div2 = tk.Frame(self.window,  width=self.div_size , height=self.div_size , bg='orange')
        self.div3 = tk.Frame(self.window,  width=self.div_size , height=self.div_size , bg='green')

        self.div1.grid(column=0, row=0, padx=self.pad, pady=self.pad, rowspan=2, sticky=self.align_mode)
        self.div2.grid(column=1, row=0, padx=self.pad, pady=self.pad, sticky=self.align_mode)
        self.div3.grid(column=1, row=1, padx=self.pad, pady=self.pad, sticky=self.align_mode)

        im = Image.open('../images/cat.jpg')
        imTK = ImageTk.PhotoImage( im.resize( (self.img_size, self.img_size) ) )

        self.lbl_img = tk.Label(self.div1, image=imTK)
        self.lbl_img.image = imTK
        self.lbl_img.grid(column=0, row=0, sticky=self.align_mode)

        self.lbl_title1 = tk.Label(self.div2, text='Hello World', bg='orange')
        self.lbl_title2 = tk.Label(self.div2, text="I'm Shei-mi", bg='orange')

        self.lbl_title1.grid(column=0, row=0, sticky=self.align_mode)
        self.lbl_title2.grid(column=0, row=1, sticky=self.align_mode)

        self.bt1 = tk.Button(self.div3, text='Button 1', bg='green')
        self.bt2 = tk.Button(self.div3, text='Button 2', bg='green')
        self.bt3 = tk.Button(self.div3, text='Button 3', bg='green')
        self.bt4 = tk.Button(self.div3, text='Button 4', bg='green')

        self.bt1.grid(column=0, row=0, sticky=self.align_mode)
        self.bt2.grid(column=0, row=1, sticky=self.align_mode)
        self.bt3.grid(column=0, row=2, sticky=self.align_mode)
        self.bt4.grid(column=0, row=3, sticky=self.align_mode)

        self.define_layout(self.window, cols=2, rows=2)
        self.define_layout(self.div1)
        self.define_layout(self.div2, rows=2)
        self.define_layout(self.div3, rows=4)
        
        # 切換全螢幕
        self.isFullScreen = False
        self.window.bind('<F12>', self.toggle_fullScreen)
        self.window.bind('<Escape>', self.del_window)

        self.window.mainloop()

    def del_window(self, event):
        self.window.destroy()

    def toggle_fullScreen(self, event):

        is_windows = lambda : 1 if platform.system() == 'Windows' else 0

        self.isFullScreen = not self.isFullScreen
        self.window.attributes("-fullscreen" if is_windows() else "-zoomed", self.isFullScreen)

    def define_layout(self, obj, cols=1, rows=1):
    
        def method(trg, col, row):

            for c in range(cols):    
                trg.columnconfigure(c, weight=1)
            for r in range(rows):
                trg.rowconfigure(r, weight=1)

        if type(obj)==list:        
            [ method(trg, cols, rows) for trg in obj ]
        else:
            trg = obj
            method(trg, cols, rows)

APP()

# %%
