

import tkinter as tk

if __name__ == '__main__':
    root = tk.Tk()
    root.title("My First GUI")
    root.geometry('100x150')

    frame = tk.LabelFrame(root, text="选择一个国家", padx=5, pady=5)
    tk.Label(frame, text="中国").pack()
    tk.Label(frame, text="美国").pack()
    tk.Label(frame, text="日本").pack()
    tk.Label(frame, text="韩国").pack()
    frame.pack(padx=5, pady=5)

    root.mainloop()