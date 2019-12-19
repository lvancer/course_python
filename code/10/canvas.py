
import tkinter as tk



if __name__ == '__main__':
    root = tk.Tk()
    root.title("画布")
    root.geometry('400x300')

    canvas = tk.Canvas(root)
    canvas.pack()

    canvas.create_line((200, 0), (150, 150), width=5, fill="red")
    canvas.create_arc((100, 100), (200, 200), width=5)
    canvas.create_text((200, 200), text="这是一个画布", font=("宋体", 18))
    canvas.create_rectangle((50, 25), (150, 75), fill='blue', outline='red', width=5)
    canvas.create_oval((200, 25), (250, 100), fill='pink', outline='green', width=5)
    point = [(50, 50), (50, 100), (100, 200), (200, 100), (200, 200)]
    canvas.create_polygon(point, outline='green', fill='yellow')

    line = canvas.create_line((0, 0), (100, 100), width=5, fill="red")
    canvas.delete(line)

    root.mainloop()