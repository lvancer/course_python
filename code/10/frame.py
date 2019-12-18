# Tkinker

import tkinter as tk        # Tk库
import tkinter.messagebox

root = tk.Tk()              # 创建Tk对象
root.title("My First GUI")  # 界面标题
root.geometry('400x300')    # 界面大小

frame = tk.Frame(root)

label = tk.Label(frame, text="输入")
label.pack(side=tk.LEFT)

var = tk.StringVar()
entry = tk.Entry(frame, textvariable=var)
entry.pack(side=tk.LEFT)

def btn_click():                # 按钮点击触发方法
    tkinter.messagebox.showinfo('点击', 'OK')

button = tk.Button(frame, text='点击', command=btn_click)
button.pack(side=tk.RIGHT)

frame.pack(side=tk.TOP)

root.mainloop()             # 启动界面






