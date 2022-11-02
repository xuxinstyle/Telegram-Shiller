import tkinter
import tkinter.messagebox
from ShillerUi import Shill
from Message import fetch_text, group0, group1, group2, group3,  fetch_text1, fetch_text2
from threading import *

class tkinterUi(object):
    def __init__(self):
        self.group0 = group0()
        self.group1 = group1()
        self.group2 = group2()
        self.group3 = group3()
        self.main = tkinter.Tk()
        self.idlist = {}
        self.idlist['+8617827198551'] = Shill("20201483", "7b0eeea50868a1744fadc74840f3a16c", "+8617827198551", self.group0, fetch_text(), 2400)
        self.idlist['+8618826578873'] = Shill("11770907", "7d820d4557af57f57ae3c5d40524ce80", "+8618826578873", self.group1, fetch_text(), 0)
        self.idlist['+8613691724231'] = Shill("27791531", "46a50576ec06eb952b322e03f88f0f40", "+8613691724231", self.group2, fetch_text1(), 1200)
        # self.id0 = Shill("20201483", "7b0eeea50868a1744fadc74840f3a16c", "+8617827198551", self.group0, fetch_text(), 2400)  # Account 0
        # self.id1 = Shill("11770907", "7d820d4557af57f57ae3c5d40524ce80", "+8618826578873", self.group1, fetch_text(), 0)  # Account 1
        # self.id2 = Shill("27791531", "46a50576ec06eb952b322e03f88f0f40", "+8613691724231", self.group2, fetch_text1(), 1200)
        # self.id3 = Shill("22641341", "9bb6137509065c3676a09599407aed2c", "+8613923782526", group3, fetch_text2(), 600)  # Account 3
        # for accid in self.idlist.values():
        #     accid.connection()


    # def btn_click(self):
    #     print('Button Click')
    #     # tkinter.messagebox.showinfo(title='tips', message=self.e.get())
    #     sl = self.lbox.curselection()
    #     for i in sl:
    #         print(i)
    #         tkinter.messagebox.showinfo(message=self.lbox.get(i))



    def cbtn_selected(self):
        print('You select', self.ownerlist[0].get(), self.ownerlist[1].get(), self.ownerlist[2].get())

    def add_login_account(self):
        api_id = self.e.get()
        api_hash = self.e1.get()
        owner = self.e2.get()
        self.idlist[owner] = Shill(api_id, api_hash, owner, self.group0, fetch_text(), 2400)
        self.idlist[owner].connection()

    def multiple_send(self):
        for owner in self.ownerlist:
            if owner.get() != '':
                myShill = self.idlist[owner.get()]

                t1 = Thread(target=myShill.account)
                t1.start()



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


        self.l = tkinter.Label(frame1, text='登录账号 api_id')
        self.l.place(x=10, y=10, anchor='w', relx=0.2, rely=0.3)
        self.l.pack(ipadx=100, ipady=1)

        self.e = tkinter.Entry(frame1)
        self.e.place(x=50, y=10, anchor='w')
        self.e.pack(padx=10, pady=1)

        self.l1 = tkinter.Label(frame1, text='登录账号 api_hash')
        self.l1.place(x=10, y=10, anchor='w', relx=0.2, rely=0.3)
        self.l1.pack(ipadx=100, ipady=1)
        self.e1 = tkinter.Entry(frame1)
        self.e1.place(x=50, y=10, anchor='w')
        self.e1.pack(padx=10, pady=1)

        self.l2 = tkinter.Label(frame1, text='登录账号电话')
        self.l2.place(x=10, y=10, anchor='w', relx=0.2, rely=0.3)
        self.l2.pack(ipadx=100, ipady=1)
        self.e2 = tkinter.Entry(frame1)
        self.e2.place(x=50, y=10, anchor='w')
        self.e2.pack(padx=10, pady=1)


        self.b1 = tkinter.Button(frame1, padx=40, pady=2)
        self.b1.config(text='添加登录账号')
        self.b1.config(command=self.add_login_account)
        self.b1.place(x=1, y=1)
        self.b1.pack()


        self.b = tkinter.Button(self.main, padx=40, pady=2)
        self.b.config(text='群发')
        self.b.config(command=self.multiple_send)
        self.b.place(x=1, y=1)
        self.b.pack()

        self.lbox = tkinter.Listbox(self.main)
        fruits = ['+8618826578873', '+8617827198551', '+8613691724231']
        for f in fruits:
            self.lbox.insert('end', f)
        self.lbox.pack()

        # self.v = tkinter.IntVar()
        #
        # r1 = tkinter.Radiobutton(self.main, text='One', variable=self.v, value=1)
        # r1.config(command=self.rbtn_selected)
        # r1.pack()
        #
        # r2 = tkinter.Radiobutton(self.main, text='Two', variable=self.v, value=2)
        # r2.config(command=self.rbtn_selected)
        # r2.pack()
        #
        # r3 = tkinter.Radiobutton(self.main, text='Three', variable=self.v, value=3)
        # r3.config(command=self.rbtn_selected)
        # r3.pack()
        self.ownerlist = []
        self.ownerlist.append(tkinter.StringVar())
        self.ownerlist.append(tkinter.StringVar())
        self.ownerlist.append(tkinter.StringVar())

        c1 = tkinter.Checkbutton(self.main, text='+8618826578873', variable=self.ownerlist[0], onvalue='+8618826578873', offvalue='')
        c1.config(command=self.cbtn_selected)
        c1.pack()

        c2 = tkinter.Checkbutton(self.main, text='+8617827198551', variable=self.ownerlist[1], onvalue='+8617827198551', offvalue='')
        c2.config(command=self.cbtn_selected)
        c2.pack()

        c3 = tkinter.Checkbutton(self.main, text='+8613691724231', variable=self.ownerlist[2], onvalue='+8613691724231', offvalue='')
        c3.config(command=self.cbtn_selected)
        c3.pack()

        self.main.mainloop()