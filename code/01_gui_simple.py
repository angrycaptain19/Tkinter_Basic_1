# %%
import tkinter as tk
from PIL import Image, ImageTk

window = tk.Tk()
window.title('window')

def create_label(txt):
    lbl_1 = tk.Label(window, text=txt, bg='yellow', fg='#263238', font=('Arial', 12), width=100, height=2)
    lbl_1.grid(column=0, row=0)

def create_button(txt):
    bt_1 = tk.Button(window, text=txt, bg='red', fg='white', font=('Arial', 12))
    bt_1['width'] = 50
    bt_1['height'] = 4
    bt_1['activebackground'] = 'red'        # 按鈕被按下的背景顏色
    bt_1['activeforeground'] = 'yellow'     # 按鈕被按下的文字顏色 ( 前景 )

    bt_1.grid(column=0, row=0)

def create_label_image():

    # 放照片在UI上
    img = Image.open('../images/cat_1.jpg')                    # 讀取圖片
    img = img.resize( (img.width // 10, img.height // 10) )   # 縮小圖片
    imgTk =  ImageTk.PhotoImage(img)                        # 轉換成Tkinter可以用的圖片
    lbl_2 = tk.Label(window, image=imgTk)                   # 宣告標籤並且設定圖片
    lbl_2.image = imgTk
    lbl_2.grid(column=0, row=0)                             # 排版位置

create_label_image()

window.mainloop()
# %%
