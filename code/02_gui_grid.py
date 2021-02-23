#%%

import tkinter as tk
from PIL import Image, ImageTk

def get_size(window, image_main, im):
    global win_size
    win_size = min( window.winfo_width(), window.winfo_height())
    # image_main['height'] = win_size
    # image_main['width'] = win_size
    image_main.image = ImageTk.PhotoImage(im.resize( (win_size, win_size) ) )
    print(win_size)

def define_layout(obj, cols=1, rows=1):
    
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

window = tk.Tk()
window.title('Window')
align_mode = 'nswe'
pad = 5

div_size = 200
img_size = div_size * 2
div1 = tk.Frame(window,  width=img_size , height=img_size , bg='blue')
div2 = tk.Frame(window,  width=div_size , height=div_size , bg='orange')
div3 = tk.Frame(window,  width=div_size , height=div_size , bg='green')

window.update()
win_size = min( window.winfo_width(), window.winfo_height())
print(win_size)

div1.grid(column=0, row=0, padx=pad, pady=pad, rowspan=2, sticky=align_mode)
div2.grid(column=1, row=0, padx=pad, pady=pad, sticky=align_mode)
div3.grid(column=1, row=1, padx=pad, pady=pad, sticky=align_mode)

define_layout(window, cols=2, rows=2)
define_layout([div1, div2, div3])

im = Image.open('../images/cat_1.jpg')
imTK = ImageTk.PhotoImage( im.resize( (img_size, img_size) ) )

image_main = tk.Label(div1, image=imTK)
image_main['height'] = img_size
image_main['width'] = img_size

image_main.grid(column=0, row=0, sticky=align_mode)

lbl_title1 = tk.Label(div2, text='Hello', bg='orange', fg='white')
lbl_title2 = tk.Label(div2, text="World", bg='orange', fg='white')

lbl_title1.grid(column=0, row=0, sticky=align_mode)
lbl_title2.grid(column=0, row=1, sticky=align_mode)

bt1 = tk.Button(div3, text='Button 1', bg='green', fg='white')
bt2 = tk.Button(div3, text='Button 2', bg='green', fg='white')
bt3 = tk.Button(div3, text='Button 3', bg='green', fg='white')
bt4 = tk.Button(div3, text='Button 4', bg='green', fg='white')

bt1.grid(column=0, row=0, sticky=align_mode)
bt2.grid(column=0, row=1, sticky=align_mode)
bt3.grid(column=0, row=2, sticky=align_mode)
bt4.grid(column=0, row=3, sticky=align_mode)

bt1['command'] = lambda : get_size(window, image_main, im)

define_layout(window, cols=2, rows=2)
define_layout(div1)
define_layout(div2, rows=2)
define_layout(div3, rows=4)

window.mainloop()




# %%
