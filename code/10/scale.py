
import tkinter as tk


if __name__ == '__main__':
    root = tk.Tk()
    root.title("My First GUI")
    root.geometry('100x150')

    scale = tk.Scale(root, from_=0, to=5, tickinterval=1)
    scale.pack()
    scale_h = tk.Scale(root, from_=0, to=10, resolution=2, orient=tk.HORIZONTAL)
    scale_h.pack()

    root.mainloop()