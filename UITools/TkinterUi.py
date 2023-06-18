import tkinter
import tkinter.messagebox

from tkinter import *
from ShillerUi import Shill
from threading import *
from config import tg_config
import time
import datetime

from PIL import ImageTk


class tkinterUi(object):
    def __init__(self):
        self.main = tkinter.Tk()
        self.m_tg_config = tg_config()
        self.idlist = {}
        self.radio_button={}
        for id in range(0, self.m_tg_config.max_index):
            self.idlist[id] = Shill(self.m_tg_config, id, self)


        # self.idlist = {}
        # self.idlist['+8617827198551'] = Shill("20201483", "7b0eeea50868a1744fadc74840f3a16c", "+8617827198551" , 2400)
        # self.idlist['+8618826578873'] = Shill("11770907", "7d820d4557af57f57ae3c5d40524ce80", "+8618826578873", 0)
        # self.idlist['+8613691724231'] = Shill("27791531", "46a50576ec06eb952b322e03f88f0f40", "+8613691724231", 1200)
        # self.idlist['+8618826578873'].initChannel()
        # self.idlist['+8618826578873'].printChannel()
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

    def inichannel(self):
        id = self.radio_var.get()
        myShill = self.idlist[int(id)]
        my_lambda = lambda: myShill.initChannel()
        t1 = Thread(target=my_lambda)
        t1.start()

    def addGroup(self):

        myShill = self.idlist[int(self.radio_var.get())]
        join_channel_lambda = lambda: myShill.join_channel()
        t1 = Thread(target=join_channel_lambda)
        t1.start()

    # def cbtn_selected(self):
    #     print('You select', self.ownerlist[0].get(), self.ownerlist[1].get(), self.ownerlist[2].get())

    # def save_data(self):
    #     with open("./config/Message.txt", 'w', encoding='UTF-8') as f:  # 返回一个文件对象
    #         f.write(self.e_path.get().replace("\n", "") + "\n")
    #         f.write(self.e_message.get().replace("\n", "") + "\n")
    #         f.write(self.e_period.get().replace("\n", ""))
    #     print("save data success")
    #     tkinter.messagebox.showinfo(title='tips', message='save data success!!!')

    def period_send(self):

        nowtime = datetime.datetime.now().strftime('%H%M%S')
        self.text_box.insert(tkinter.END, "nowtime:"+nowtime +"\n")
        period_time = int(self.e_period.get())
        detatime = period_time * 1000 * 60

        if int(nowtime) < 13000 or int(nowtime) > 100000:
            self.group_send_button()
            self.insert_new_line("group_send_button")

        self.insert_new_line("detatime:" + str(detatime))
        self.insert_new_line("nowtime:" + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
        self.main.after(int(detatime), self.period_send)

    # def add_login_account(self):
    #     api_id = self.e.get()
    #     api_hash = self.e1.get()
    #     owner = self.e2.get()
    #     self.idlist[owner] = Shill(api_id, api_hash, owner, self.group0, fetch_text(), 2400)
    #     self.idlist[owner].connection()

    def multiple_send(self):
        for owner in self.ownerlist:
            if owner.get() != '':
                myShill = self.idlist[owner.get()]

                t1 = Thread(target=myShill.account)
                t1.start()

    def group_send_button(self):
        for shell in self.idlist:
            self.idlist[shell].send_by_win(self.text_box)

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
        self.main.geometry("800x600")
        # frame1 = tkinter.Frame(self.main)
        # frame1.place(x=1, y=10, anchor='w', relx=0.2, rely=0.3)
        # frame1.pack(padx=1, pady=1, side='left')

        frame_left = tkinter.Frame(self.main)
        frame_left.place(x=1, y=10, anchor='w', relx=0.2, rely=0.3)
        frame_left.pack(padx=1, pady=20, side=tkinter.LEFT)

        frame_right = tkinter.Frame(self.main)
        frame_right.place(x=1, y=10, anchor='w', relx=0.2, rely=0.3)
        frame_right.pack(padx=1, pady=1, side=tkinter.RIGHT)

        # self.left_frame = tkinter.Frame(self.main)
        # self.left_frame.pack(side=tkinter.LEFT)
        frame_left_left = tkinter.Frame(frame_left)
        frame_left_left.place(x=1, y=1, anchor='w', relx=2, rely=3)
        frame_left_left.pack(padx=0, pady=20, side=tkinter.LEFT)

        frame_left_right = tkinter.Frame(frame_left)
        frame_left_right.place(x=1, y=1, anchor='w', relx=2, rely=3)
        frame_left_right.pack(padx=0, pady=20, side=tkinter.RIGHT)



        frame_left_top = tkinter.Frame(frame_left)
        frame_left_top.place(x=1, y=10, anchor='w', relx=0.2, rely=0.3)
        frame_left_top.pack(padx=1, pady=1, side='top')



        frame_left_top_1 = tkinter.Frame(frame_left_top)
        frame_left_top_1.place(x=1, y=1, anchor='w', relx=2, rely=3)
        frame_left_top_1.pack(padx=2, pady=2, side='left')



        self.b3 = tkinter.Button(frame_left_right, padx=40, pady=2)
        self.b3.config(text='定时群发')
        self.b3.config(command=self.period_send)
        self.b3.place(x=30, y=30)
        self.b3.pack(padx=3, pady=2)

        period = tkinter.IntVar(value=120)
        self.e_period = tkinter.Entry(frame_left_right, textvariable=period, width=10)
        self.e_period.place(x=100, y=20, anchor='w')
        self.e_period.pack(padx=3, pady=2)

        tkinter.Label(frame_left_right, text='定时周期（单位分钟）').pack()

        self.b2 = tkinter.Button(frame_left_right, padx=40, pady=2)
        self.b2.config(text='按键群发')
        self.b2.config(command=self.group_send_button)
        self.b2.place(x=1, y=1)
        self.b2.pack()





        self.b = tkinter.Button(frame_left_right, padx=40, pady=2)
        self.b.config(text='API群发')
        self.b.config(command=self.multiple_send)
        self.b.place(x=1, y=1)
        self.b.pack()

        # 创建单选按钮组
        self.radio_var = tkinter.StringVar(value="0")
        for shell_id in self.idlist:
            shiller= self.idlist[shell_id]
            sh_config=shiller.m_config
            sh_config.get_owner(shiller.m_id)
            self.radio_button[shell_id] = tkinter.Radiobutton(
                frame_left_left,
                text=sh_config.get_owner(shiller.m_id),
                variable=self.radio_var,
                value=shiller.m_id)
            # 显示单选按钮组
            self.radio_button[shell_id].pack()




        # self.ownerlist = []
        # self.ownerlist.append(tkinter.StringVar())
        # self.ownerlist.append(tkinter.StringVar())
        # self.ownerlist.append(tkinter.StringVar())
        #
        # c1 = tkinter.Checkbutton(frame_left_left, text='+8618826578873', variable=self.ownerlist[0], onvalue='+8618826578873',
        #                          offvalue='')
        # c1.config(command=self.cbtn_selected)
        # c1.pack()
        #
        # c2 = tkinter.Checkbutton(frame_left_left, text='+8617827198551', variable=self.ownerlist[1], onvalue='+8617827198551',
        #                          offvalue='')
        # c2.config(command=self.cbtn_selected)
        # c2.pack()
        #
        # c3 = tkinter.Checkbutton(frame_left_left, text='+8613691724231', variable=self.ownerlist[2], onvalue='+8613691724231',
        #                          offvalue='')
        # c3.config(command=self.cbtn_selected)
        # c3.pack()



        # 在文本框中插入一些文本
        # text_box.insert(tkinter.END, "这是我要显示的文本。")

        frame_left_bottom = tkinter.Frame(frame_left_right)
        frame_left_bottom.place(x=1, y=1, anchor='w', relx=2, rely=3)
        frame_left_bottom.pack(padx=0, pady=20, side=tkinter.BOTTOM)

        # self.b4 = tkinter.Button(frame_left_bottom, padx=2, pady=2)
        # self.b4.config(text='保存修改')
        # self.b4.config(command=self.save_data)
        # self.b4.place(x=1, y=1)
        # self.b4.pack(padx=10, pady=1, side='left')


        # 绑定窗口关闭事件
        self.main.protocol("WM_DELETE_WINDOW", self.main.destroy)

        self.text_box_join_load_button(frame_right)

        self.main.mainloop()

    # 文本框和加入频道按钮
    def text_box_join_load_button(self, frame):
        # 创建一个按钮，用于加载频道内容


        # 创建一个按钮，用于加入频道
        join_button = tkinter.Button(frame, text="加入频道")
        join_button.config(command=self.addGroup)
        join_button.pack()

        my_lambda = lambda: self.inichannel()
        load_button = tkinter.Button(frame, text="加载频道内容")
        load_button.config(command=my_lambda)
        load_button.pack()

        # 创建一个文本框
        self.text_box = tkinter.Text(frame, height=30, width=50)
        self.text_box.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True)

        scrollbar = tkinter.Scrollbar(frame)
        scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

        self.text_box.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.text_box.yview)

        self.insert_new_line("欢迎使用.. ")

    def insert_new_line(self, context):
        print(context)
        self.text_box.insert(tkinter.END, str(context)+"\n")
        self.text_box.see(tkinter.END)