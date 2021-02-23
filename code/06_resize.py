#%%

import tkinter as tk
from PIL import Image, ImageTk
import platform
import time

# window.update()
# win_size = min( window.winfo_width(), window.winfo_height())
# print(win_size)

class APP:

    def __init__(self):

        self.window = tk.Tk()
        self.window.title('Window')

        self.align_mode = 'nsew'
        self.pad = 10

        self.div_size, self.img_size = 50, 400
        self.div1 = tk.Frame(self.window,  width=self.div_size , height=self.div_size)
        self.div2 = tk.Frame(self.window,  width=self.img_size , height=self.img_size) 

        self.div1.grid(column=0, row=0, padx=self.pad, pady=self.pad, sticky=self.align_mode)
        self.div2.grid(column=0, row=1, padx=self.pad, pady=self.pad, sticky=self.align_mode)

        self.bt1 = tk.Button(self.div1, text='Cat')
        self.bt1.grid(column=0, row=0, sticky=self.align_mode)
        self.bt2 = tk.Button(self.div1, text='Dog')
        self.bt2.grid(column=1, row=0, sticky=self.align_mode)
        self.bt3 = tk.Button(self.div1, text='Clear')
        self.bt3.grid(column=2, row=0, sticky=self.align_mode)
        self.bt4 = tk.Button(self.div1, text='Quit')
        self.bt4.grid(column=3, row=0, sticky=self.align_mode)

        self.define_layout(self.window, cols=1, rows=2)

        # 圖片的部分
        self.window.update()
        self.reszie_time, self.resize_rate = 0, 0.5
        self.w, self.h = self.div2.winfo_width(), self.div2.winfo_height()
        self.im = ''
        self.imTK = ''      # 預設給空白
        self.lbl_img = tk.Label(self.div2, image=self.imTK)
        self.lbl_img.image = self.imTK
        self.lbl_img.grid(column=0, row=0, sticky=self.align_mode)
        self.div2.grid_propagate(0)                 # 不會被子元件改變大小

        # 按鈕的部分
        self.bt1['command'] = self.bt1_event
        self.bt2['command'] = self.bt2_event
        self.bt3['command'] = self.bt3_event
        # self.bt4['command'] = lambda : self.window.destroy()
        self.bt4.bind('<Button-1>', self.del_window)
        self.define_layout(self.div1, rows=1, cols=4)

        # 切換全螢幕
        self.isFullScreen = False
        self.window.bind('<F12>', self.toggle_fullScreen)
        self.window.bind('<Escape>', self.del_window)

        self.window.bind('<ButtonRelease>', lambda event: self.get_size)

        self.update()
        self.window.mainloop()

    def get_size(self, event):
        self.w, self.h = self.div2.winfo_width(), self.div2.winfo_height()

    def update(self):
        if self.w == self.div2.winfo_width() and self.h ==self.div2.winfo_height():
            self.reszie_time = time.time()
        
        if self.w != self.div2.winfo_width() or self.h !=self.div2.winfo_height():
            if time.time()-self.reszie_time>= self.resize_rate and self.im is not '':
                self.w, self.h = self.div2.winfo_width(), self.div2.winfo_height()    
                self.imTK = ImageTk.PhotoImage( self.im.resize( (self.w, self.h) ) )
                self.lbl_img.configure(image=self.imTK)
                self.lbl_img.image = self.imTK             
                
        self.window.after(10, self.update)   # 5 是毫秒    

    def bt1_event(self):
        self.im = Image.open('../images/cat_1.jpg')
        self.imTK = ImageTk.PhotoImage( self.im.resize( (self.w, self.h) ) )
        self.lbl_img.configure(image=self.imTK)
        self.lbl_img.image = self.imTK              # 防止圖片被自動垃圾清掃給除掉

    def bt2_event(self):
        self.im = Image.open('../images/dog_1.jpg')
        w, h = self.div2.winfo_width(), self.div2.winfo_height()
        self.imTK = ImageTk.PhotoImage( self.im.resize( (w, h) ) )
        self.lbl_img.configure(image=self.imTK)
        self.lbl_img.image = self.imTK              # 防止圖片被自動垃圾清掃給除掉

    def bt3_event(self):
        self.lbl_img.configure(image='')

    def del_window(self, event):
        self.window.destroy()

    def toggle_fullScreen(self, event):

        is_windows = lambda : 1 if platform.system() == 'Windows' else 0

        self.isFullScreen = not self.isFullScreen
        self.window.attributes("-fullscreen" if is_windows() else "-zoomed", self.isFullScreen)

    def define_layout(self, obj, cols=1, rows=1):

        def method(trg, col, row):

            [ trg.columnconfigure(c, minsize=self.div_size, weight=1)  for c in range(cols) ]   
            [ trg.rowconfigure(r, minsize=self.div_size, weight=1)     for r in range(rows) ]

        if type(obj)==list:        
            [ method(trg, cols, rows) for trg in obj ]
        else:
            method(obj, cols, rows)

APP()

# %%
