

import tkinter as tk


root = tk.Tk()
root.title("My First GUI")
root.geometry('400x300')

def key(event):
    print(event)

def callback(event):
    print(event)
    type = event.type           # 事件类型
    widget = event.widget       # 触发事件的控件
    x, y = event.x, event.y     # 触发位置
    char = event.char           # 键盘事件内容
    num = event.num             # 鼠标事件内容
    width, height = event.width, event.height   # 控件新大小




text = tk.Text(root)
text.bind('<Control-Shift-H>', key)
text.bind('<Button-1>', callback)
text.pack(padx=5, pady=5)

root.mainloop()