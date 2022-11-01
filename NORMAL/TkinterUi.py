import tkinter
import tkinter.messagebox

class tkinterUi(object):
    def __init__(self):
        self.main = tkinter.Tk()


    def btn_click(self):
        print('Button Click')
        # tkinter.messagebox.showinfo(title='tips', message=self.e.get())
        sl = self.lbox.curselection()
        for i in sl:
            print(i)
            tkinter.messagebox.showinfo(message=self.lbox.get(i))

    def rbtn_selected(self):
        print('You select', self.v.get())

    def cbtn_selected(self):
        print('You select', self.v1.get(), self.v2.get())

    # tkinter.messagebox.showinfo(title='tips', message='hello')  # 提示信息对话窗
    # tkinter.messagebox.showwarning(title='tips', message='warning')  # 提出警告对话窗
    # tkinter.messagebox.showerror(title='tips', message='error！')  # 提出错误对话窗
    # print(tkinter.messagebox.askquestion(title='tips', message='need some help?'))  # 询问选择对话窗return 'yes', 'no'
    # print(tkinter.messagebox.askyesno(title='tips', message='hello'))  # return 'True', 'False'
    # print(tkinter.messagebox.askokcancel(title='tips', message='hello'))  # return 'True', 'False'
    def show(self):
        # 设置标题
        self.main.title("telegram群发工具")
        # 设置大小（宽x高）
        self.main.geometry("600x400")
        frame1 = tkinter.Frame(self.main)
        frame1.place(x=1, y=10, anchor='w', relx=0.2, rely=0.3)
        frame1.pack(padx=1, pady=1, side='left')

        self.l = tkinter.Label(frame1, text='登录账号')
        self.l.place(x=10, y=10, anchor='w', relx=0.2, rely=0.3)
        self.l.pack(ipadx=100, ipady=1)

        self.e = tkinter.Entry(frame1)
        self.e.place(x=50, y=10, anchor='w')

        self.e.pack(padx=10, pady=1)

        self.b = tkinter.Button(self.main, padx=40, pady=2)
        self.b.config(text='群发')
        self.b.config(command=self.btn_click)
        self.b.place(x=1, y=1)
        self.b.pack()

        self.b1 = tkinter.Button(frame1, padx=40, pady=2)
        self.b1.config(text='登录')
        self.b1.config(command=self.btn_click)
        self.b1.place(x=1, y=1)
        self.b1.pack()
        self.lbox = tkinter.Listbox(self.main)

        fruits = ['apple', 'banana', 'orange']
        for f in fruits:
            self.lbox.insert('end', f)
        self.lbox.pack()

        self.v = tkinter.IntVar()

        r1 = tkinter.Radiobutton(self.main, text='One', variable=self.v, value=1)
        r1.config(command=self.rbtn_selected)
        r1.pack()

        r2 = tkinter.Radiobutton(self.main, text='Two', variable=self.v, value=2)
        r2.config(command=self.rbtn_selected)
        r2.pack()

        r3 = tkinter.Radiobutton(self.main, text='Three', variable=self.v, value=3)
        r3.config(command=self.rbtn_selected)
        r3.pack()

        self.v1 = tkinter.IntVar()
        self.v2 = tkinter.IntVar()

        c1 = tkinter.Checkbutton(self.main, text='apple', variable=self.v1, onvalue=1, offvalue=0)
        c1.config(command=self.cbtn_selected)
        c1.pack()

        c2 = tkinter.Checkbutton(self.main, text='banana', variable=self.v2, onvalue=1, offvalue=0)
        c2.config(command=self.cbtn_selected)
        c2.pack()

        self.main.mainloop()