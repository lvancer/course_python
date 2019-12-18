

import tkinter as tk
import tkinter.messagebox


class MyFrame(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.value = tk.IntVar()
        options = [('中国', 0), ('美国', 1), ('日本', 2), ('韩国', 3)]  # 选项
        for t, v in options:
            tk.Radiobutton(self, text=t, value=v, variable=self.value,
                           command=self.radio_select).pack()

    def radio_select(self):
        print(self.value.get())


if __name__ == '__main__':
    root = tk.Tk()
    root.title("My First GUI")
    root.geometry('300x100')
    MyFrame(root).pack(side=tk.TOP)
    root.mainloop()