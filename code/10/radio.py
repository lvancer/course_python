

import tkinter as tk


class MyFrame(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)

        frame = tk.LabelFrame(self, text="选择一个国家", padx=5, pady=5)
        self.value = tk.IntVar()
        options = [('中国', 0), ('美国', 1), ('日本', 2), ('韩国', 3)]  # 选项
        for t, v in options:
            tk.Radiobutton(frame, text=t, value=v, variable=self.value,
                           command=self.radio_select).pack()
        frame.pack(padx=5, pady=5)

    def radio_select(self):
        print(self.value.get())


if __name__ == '__main__':
    root = tk.Tk()
    root.title("My First GUI")
    root.geometry('100x150')
    MyFrame(root).pack()
    root.mainloop()