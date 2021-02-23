

# %%
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
    
    def quit(self, event):

        quit_check = tk.messagebox.askokcancel('提示', '是否要退出?')
        if quit_check:
            print('離開程式')
            cv2.destroyAllWindows()
            self.cap.release()
            self.window.destroy()

def simple_stream():
    
    import tkinter as tk
    import cv2
    from PIL import ImageTk, Image

    window = tk.Tk()
    window.title('Video Stream')

    main = tk.Frame(window, bg="white")
    main.grid()

    video = tk.Label(main)
    video.grid()

    window.bind('<Escape>', lambda event: window.destroy())

    # 宣告攝影機
    status, frame = 0, []
    cap = cv2.VideoCapture(0)   

    def stream():

        # 讀取當前的影像
        global status, frame
        status, frame = cap.read()
        # 如果有影像的話
        if status:
            # 將 OpenCV 色改格式 ( BGR ) 轉換成 RGB
            im_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
            # 將 OpenCV 圖檔轉換成 PIL
            im_pil = Image.fromarray(im_rgb)
            # 轉換成 ImageTK
            imgTK = ImageTk.PhotoImage(image=im_pil)
            # 放入圖片
            video.configure(image=imgTK)
            # 防止圖片丟失，做二次確認
            video.image = imgTK
        # 10 豪秒 後執行 stream 函式，這裡是模擬 While 迴圈的部分
        window.after(10, stream) 

    # 先執行一次
    stream()

    window.mainloop()

    # 釋出攝影機記憶體、關閉所有視窗
    cap.release()
    cv2.destroyAllWindows()

# simple_stream()
APP()
# %%
