#%%

import tkinter as tk
import tkinter.messagebox
from PIL import ImageTk, Image
import cv2


class APP:
    
    def __init__(self):

        self.window = tk.Tk()
        self.window.title('Video Stream')
        self.main = tk.Frame(self.window, bg="white")
        self.main.grid()

        self.status, self.frame = 0, []
        self.video = tk.Label(self.main)
        self.video.grid()

        self.window.bind('<Escape>', self.quit)

        self.cap = cv2.VideoCapture(0)

        self.delay = 10     # 毫秒
        self.stream()

        self.window.mainloop()

    def cv2_pil(self, im):
        im_rgb = cv2.cvtColor(im, cv2.COLOR_BGR2RGBA)
        return Image.fromarray(im_rgb)

    def stream(self):

        self.status, self.frame = self.cap.read()
        imgTK = ImageTk.PhotoImage(image=self.cv2_pil(self.frame))
        self.video.configure(image=imgTK)
        self.video.image = imgTK

        self.window.after(self.delay, self.stream) 
    
    def exit(self):
        cv2.destroyAllWindows()
        self.cap.release()
        self.window.destroy()

    def quit(self, event):

        quit_check = tk.messagebox.askokcancel('提示', '是否要退出?')
        if quit_check:

            quit_check = tk.messagebox.askokcancel('提示', '可是我會想你欸，確定要退出?')
        if quit_check:

            quit_check = tk.messagebox.askokcancel('提示', '不要離開我拉')
        if quit_check:        

            quit_check = tk.messagebox.askokcancel('提示', '拜託不要拉')
        if quit_check:

            quit_check = tk.messagebox.askokcancel('提示', '再給你最後一次機會哦！')
        if quit_check:                    

            quit_check = tk.messagebox.askokcancel('提示', '沒良心的使用者...')
        if quit_check:                        
            self.exit()

APP()
# %%
