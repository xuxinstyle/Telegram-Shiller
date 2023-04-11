import tkinter
import tkinter.messagebox

from tkinter import *
from ShillerUi import Shill
from Message import fetch_text, group0, group1, group2, group3,  fetch_text1, fetch_text2, period_time, telegram_path
from threading import *
import script
import time
import datetime

from PIL import ImageTk


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
        self.idlist['+8618826578873'].initChannel()
        self.idlist['+8618826578873'].printChannel()
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

    def save_data(self):
        with open("./config/Message.txt", 'w', encoding='UTF-8') as f:  # 返回一个文件对象
            f.write(self.e_path.get().replace("\n", "")+"\n")
            f.write(self.e_message.get().replace("\n", "")+"\n")
            f.write(self.e_period.get().replace("\n", ""))
        print("save data success")
        tkinter.messagebox.showinfo(title='tips', message='save data success!!!')

    def period_send(self):
        print("" + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        detatime = int(self.e_period.get()) * 1000 * 60
        print(detatime)
        self.group_send_button()
        print("" + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        self.main.after(detatime, self.period_send)

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

    def group_send_button(self):
        script.group_send(self.e_path.get().strip(), self.e_message.get())






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
        self.main.geometry("600x500")
        # frame1 = tkinter.Frame(self.main)
        # frame1.place(x=1, y=10, anchor='w', relx=0.2, rely=0.3)
        # frame1.pack(padx=1, pady=1, side='left')


        frame2 = tkinter.Frame(self.main)
        frame2.place(x=1, y=10, anchor='w', relx=0.2, rely=0.3)
        frame2.pack(padx=1, pady=20, side='top')


        frame3 = tkinter.Frame(self.main)
        frame3.place(x=1, y=10, anchor='w', relx=0.2, rely=0.3)
        frame3.pack(padx=1, pady=1, side='top')

        frame4 = tkinter.Frame(self.main)
        frame4.place(x=1, y=10, anchor='w', relx=0.2, rely=0.3)
        frame4.pack(padx=1, pady=1, side='top')

        frame5 = tkinter.Frame(self.main)
        frame5.place(x=1, y=1, anchor='w', relx=2, rely=3)
        frame5.pack(padx=0, pady=20, side='top')

        path = tkinter.StringVar( value = telegram_path() )
        self.e_path = tkinter.Entry(frame3, textvariable=path, width=50)
        self.e_path.place(x=100, y=10, anchor='w')
        self.e_path.pack(padx=10, pady=1)

        message = tkinter.StringVar( value = fetch_text1() )
        self.e_message = tkinter.Entry(frame3, textvariable=message, width=50)
        self.e_message.place(x=100, y=20, anchor='w')
        self.e_message.pack(padx=30, pady=2)

        self.b2 = tkinter.Button(frame3, padx=40, pady=2)
        self.b2.config(text='按键群发')
        self.b2.config(command=self.group_send_button)
        self.b2.place(x=1, y=1)
        self.b2.pack()

        frame3_1 = tkinter.Frame(frame3)
        frame3_1.place(x=1, y=10, anchor='w', relx=2, rely=3)
        frame3_1.pack(padx=20, pady=20, side='left')

        frame3_2 = tkinter.Frame(frame3)
        frame3_2.place(x=1, y=1, anchor='w', relx=2, rely=3)
        frame3_2.pack(padx=2, pady=2, side='left')



        self.b3 = tkinter.Button(frame3_1, padx=40, pady=2)
        self.b3.config(text='定时群发')
        self.b3.config(command=self.period_send)
        self.b3.place(x=30, y=30)
        self.b3.pack(padx=3, pady=2)

        period = tkinter.IntVar( value=period_time() )
        self.e_period = tkinter.Entry(frame3_2, textvariable=period, width=10)
        self.e_period.place(x=100, y=20, anchor='w')
        self.e_period.pack(padx=3, pady=2)

        tkinter.Label(frame3_2, text='定时周期（单位分钟）').pack()


        self.b = tkinter.Button(frame2, padx=40, pady=2)
        self.b.config(text='API群发')
        self.b.config(command=self.multiple_send)
        self.b.place(x=1, y=1)
        self.b.pack()


        self.ownerlist = []
        self.ownerlist.append(tkinter.StringVar())
        self.ownerlist.append(tkinter.StringVar())
        self.ownerlist.append(tkinter.StringVar())

        c1 = tkinter.Checkbutton(frame2, text='+8618826578873', variable=self.ownerlist[0], onvalue='+8618826578873', offvalue='')
        c1.config(command=self.cbtn_selected)
        c1.pack()

        c2 = tkinter.Checkbutton(frame2, text='+8617827198551', variable=self.ownerlist[1], onvalue='+8617827198551', offvalue='')
        c2.config(command=self.cbtn_selected)
        c2.pack()

        c3 = tkinter.Checkbutton(frame2, text='+8613691724231', variable=self.ownerlist[2], onvalue='+8613691724231', offvalue='')
        c3.config(command=self.cbtn_selected)
        c3.pack()


        self.b4 = tkinter.Button(frame5, padx=2, pady=2)
        self.b4.config(text='保存修改')
        self.b4.config(command=self.save_data)
        self.b4.place(x=1, y=1)
        self.b4.pack(padx=10, pady=1, side='left')

        self.main.mainloop()