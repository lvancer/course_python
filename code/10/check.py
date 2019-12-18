

import tkinter as tk
import tkinter.messagebox


class MultiCheckBox(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)

        self.check1 = tk.IntVar()
        self.checkbutton1 = tk.Checkbutton(self, text="安卓", variable=self.check1)
        self.checkbutton1.grid(column=0, row=0, sticky=tk.W)
        self.check2 = tk.IntVar()
        self.checkbutton2 = tk.Checkbutton(self, text="苹果", variable=self.check2)
        self.checkbutton2.grid(column=1, row=0, sticky=tk.W)
        self.check3 = tk.IntVar()
        self.checkbutton3 = tk.Checkbutton(self, text="PC", variable=self.check3,
                                           state='disabled')
        self.checkbutton3.select()  # 选择
        self.checkbutton3.grid(column=2, row=0, sticky=tk.W)






if __name__ == '__main__':
    root = tk.Tk()
    root.title("My First GUI")
    root.geometry('300x100')


    # def checkbutton_select(x):   #
    #     print(x.get())
    # check = tk.IntVar()
    # checkbutton = tk.Checkbutton(root, text="选择框", variable=check,
    #     command=lambda : checkbutton_select(check))
    # checkbutton.pack()

    MultiCheckBox(root).pack(side=tk.TOP)
    root.mainloop()