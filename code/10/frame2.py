
import tkinter as tk
import tkinter.messagebox


class MyFrame(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.label = tk.Label(self, text="输入")
        self.label.pack(side=tk.LEFT)
        self.var = tk.StringVar()
        self.entry = tk.Entry(self, textvariable=self.var)
        self.entry.pack(side=tk.LEFT)
        self.button = tk.Button(self, text='点击', command=self.btn_click)
        self.button.pack(side=tk.RIGHT)

    def btn_click(self):
        tkinter.messagebox.showinfo('输入内容', self.var.get())


if __name__ == '__main__':
    root = tk.Tk()
    root.title("My First GUI")
    root.geometry('300x100')
    MyFrame(root).pack(side=tk.TOP)
    root.mainloop()