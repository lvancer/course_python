# Tkinker

import tkinter as tk        # Tk库
import tkinter.messagebox

root = tk.Tk()              # 创建Tk对象
root.title("My First GUI")  # 界面标题
root.geometry('400x300')    # 界面大小

# 标签文字
label = tk.Label(root, text="输入",
                 bg="white", font=("Arial", 12),
                 width=5, height=1)
label.pack()    # 添加到界面

# 单行文本输入框
var = tk.StringVar()    # 用于存储内容的变量
entry = tk.Entry(root, textvariable=var)
var.set("hello")        # 设置输入框内容
# print(var.get())        # 获取输入框内容
entry.pack()

# 按钮
def btn_click():                # 按钮点击触发方法
    tkinter.messagebox.showinfo('点击', 'OK')

button = tk.Button(root, text='点击', command=btn_click)
button.pack()

root.mainloop()             # 启动界面






