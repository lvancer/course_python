

import tkinter as tk
import tkinter.messagebox
import random


class MyFrame(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.listbox = tk.Listbox(self, selectmode=tk.MULTIPLE)
        for item in range(10):
            self.listbox.insert(tk.END, item)
        self.listbox.pack(side=tk.LEFT)

        tk.Button(self, text='删除', command=self.delete).pack(side=tk.TOP)

    def delete(self):
        self.listbox.delete('active')   # 删除选中项


if __name__ == '__main__':
    root = tk.Tk()
    root.title("My First GUI")
    root.geometry('300x100')
    MyFrame(root).pack(side=tk.TOP)
    root.mainloop()