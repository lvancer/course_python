
import tkinter as tk
import tkinter.filedialog
import tkinter.ttk as ttk

class Window(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self)
        self.title("菜单")
        self.geometry('300x100')
        # 添加菜单
        self.addMenu()

        options = ['gbk', 'utf-8']  # 选项
        self.code = tk.StringVar()  # 绑定变量
        menuCode = ttk.OptionMenu(self, self.code,
                                  options[0], *options,
                                  command=self.codeChange)
        menuCode.pack()

    def codeChange(self, value):
        print(value)

    def addMenu(self):
        menubar = tk.Menu(self)     # 菜单栏
        self.config(menu=menubar)   # 设置菜单

        menuFile = tk.Menu(menubar, tearoff=0)  # 一级菜单
        menubar.add_cascade(label="文件", menu=menuFile)  # 添加到菜单栏
        menuFile.add_command(label="打开", command=self.onMenuFileOpen)   # 添加子菜单



    def onMenuFileOpen(self):
        file = tkinter.filedialog.askopenfilename()
        print(file)




if __name__ == '__main__':
    Window().mainloop()
