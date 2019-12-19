
import tkinter as tk

if __name__ == '__main__':
    root = tk.Tk()
    root.title("My First GUI")
    root.geometry('400x300')

    # text = tk.Text(root)
    # text.pack()
    # text.insert(tk.INSERT, "123\n")     # 在光标出插入
    # text.insert(tk.END, "444")          # 在最后插入
    # content = text.get('0.0', tk.END)   # 获取内容

    import tkinter.scrolledtext
    text = tkinter.scrolledtext.ScrolledText(root)
    text.pack()

    root.mainloop()