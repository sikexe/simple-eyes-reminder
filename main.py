import tkinter as tk
import time

while True:
    def center_window(width=100, height=20):

        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        x = (screen_width) - (width*2)
        y = (screen_height) - (height*8)

        root.geometry('%dx%d+%d+%d' % (width, height, x, y))

    root = tk.Tk()
    w = tk.Label(root, text="Remember to eyes!", fg="red")
    w.pack()
    center_window(100, 20)
    root.mainloop()
    time.sleep(3600)