# 对话框


import tkinter as tk
import tkinter.messagebox
import tkinter.filedialog
import tkinter.colorchooser
import tkinter.simpledialog


class MyFrame(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Button(self, text='显示对话框', command=self.show_dialog).pack()
        tk.Button(self, text='提问对话框', command=self.show_ask).pack()
        tk.Button(self, text='文件对话框', command=self.show_file).pack()
        tk.Button(self, text='文件夹对话框', command=self.show_dir).pack()
        tk.Button(self, text='颜色选择', command=self.choose_color).pack()
        tk.Button(self, text='输入对话框', command=self.input).pack()
        tk.Button(self, text='自定义对话框', command=self.custom).pack()
        tk.Button(self, text='登录对话框', command=self.login).pack()


    def show_dialog(self):
        tkinter.messagebox.showinfo(title='info', message='info')
        tkinter.messagebox.showwarning(title='warn', message='warn')
        tkinter.messagebox.showerror(title='error', message='error')

    def show_ask(self):
        ask = tkinter.messagebox.askyesno(title='ask', message='yesorno')
        ask = tkinter.messagebox.askokcancel(title='ask', message='okorcancel')
        ask = tkinter.messagebox.askretrycancel(title='ask', message='retrycancel')
        ask = tkinter.messagebox.askyesnocancel(title='ask', message='yesnocancel')

    def show_file(self):
        filename = tkinter.filedialog.askopenfilename(initialdir='C:\\')
        filenames = tkinter.filedialog.askopenfilenames()
        file = tkinter.filedialog.askopenfile(mode='r', filetypes=[('Python', '.py')])
        files = tkinter.filedialog.askopenfiles(title='选择多个文件')

    def show_dir(self):
        dir = tkinter.filedialog.askdirectory(initialdir='C:\\')

    def save_file(self):
        filename = tkinter.filedialog.asksaveasfilename(filetypes=[('Python', '.py')])
        file = tkinter.filedialog.asksaveasfile(defaultextension='py', initialdir='C:\\')

    def choose_color(self):
        color = tkinter.colorchooser.askcolor(color='red', title='选择喜欢的颜色')
        print(color)

    def input(self):
        i = tkinter.simpledialog.askinteger(title='simple', prompt='整数：',
                                            minvalue=1, maxvalue=10)
        f = tkinter.simpledialog.askfloat(title='simple', prompt='小数：',
                                          initialvalue='1.1')
        s = tkinter.simpledialog.askstring(title='simple', prompt='字符串：')

    def custom(self):
        dialog = MyDialog(self)
        self.wait_window(dialog)
        print(dialog.value.get())

    def login(self):
        dialog = LoginDialog(self)
        self.wait_window(dialog)
        print(dialog.login_info)

class MyDialog(tk.Toplevel):

    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)

        frame = tk.LabelFrame(self, text="选择一个国家", padx=5, pady=5)
        self.value = tk.IntVar()
        options = [('中国', 0), ('美国', 1), ('日本', 2), ('韩国', 3)]  # 选项
        for t, v in options:
            tk.Radiobutton(frame, text=t, value=v, variable=self.value,
                           command=self.radio_select).pack()
        frame.pack(padx=5, pady=5)

    def radio_select(self):
        self.destroy()


class LoginDialog(tk.Toplevel):

    def __init__(self, parent):
        tk.Toplevel.__init__(self, parent)

        tk.Label(self, text='用户名：',).grid(column=0, row=0)
        tk.Label(self, text='密码：').grid(column=0, row=1)

        self._username = tk.StringVar()
        self._password = tk.StringVar()
        tk.Entry(self, textvariable=self._username).grid(column=1, row=0)
        tk.Entry(self, textvariable=self._password).grid(column=1, row=1)

        btns = tk.Frame(self)
        tk.Button(btns, text="取消", command=self.cancel).pack(side=tk.RIGHT)
        tk.Button(btns, text="确定", command=self.ok).pack(side=tk.RIGHT)
        btns.grid(column=1, row=2, sticky=tk.E)

        self.login_info = {'username': None, 'password': None}

    def cancel(self):
        self.destroy()

    def ok(self):
        self.login_info['username'] = self._username.get()
        self.login_info['password'] = self._password.get()
        self.destroy()


if __name__ == '__main__':
    root = tk.Tk()
    root.title("对话框")
    root.geometry('100x250')
    MyFrame(root).pack(side=tk.TOP)
    root.mainloop()