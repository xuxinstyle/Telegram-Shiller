import tkinter as tk
from telethon import TelegramClient
from telethon.tl.functions.channels import JoinChannelRequest
from datetime import datetime, timedelta

class TelegramUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Telegram UI")

        # API ID 输入框和标签
        api_id_label = tk.Label(self.master, text="API ID:")
        api_id_label.pack(side="top")
        self.api_id = tk.Entry(self.master)
        self.api_id.pack(side="top")

        # API Hash 输入框和标签
        api_hash_label = tk.Label(self.master, text="API Hash:")
        api_hash_label.pack(side="top")
        self.api_hash = tk.Entry(self.master)
        self.api_hash.pack(side="top")

        # 手机号码输入框和标签
        phone_number_label = tk.Label(self.master, text="Phone Number:")
        phone_number_label.pack(side="top")
        self.phone_number = tk.Entry(self.master)
        self.phone_number.pack(side="top")

        # 群组链接输入框和标签
        group_link_label = tk.Label(self.master, text="Group Link:")
        group_link_label.pack(side="top")
        self.group_link = tk.Entry(self.master)
        self.group_link.pack(side="top")

        # 消息输入框和标签
        message_label = tk.Label(self.master, text="Message:")
        message_label.pack(side="top")
        self.message = tk.Entry(self.master)
        self.message.pack(side="top")

        # 发送间隔输入框和标签
        interval_label = tk.Label(self.master, text="Interval (seconds):")
        interval_label.pack(side="top")
        self.interval = tk.Entry(self.master)
        self.interval.pack(side="top")

        # 登录按钮
        login_button = tk.Button(self.master, text="Login", command=self.login)
        login_button.pack(side="left")

        # 加入群组按钮
        join_group_button = tk.Button(self.master, text="Join Group", command=self.join_group)
        join_group_button.pack(side="left")

        # 发送消息按钮
        send_message_button = tk.Button(self.master, text="Send Message", command=self.send_message)
        send_message_button.pack(side="left")

        # 定时发送消息按钮
        schedule_messages_button = tk.Button(self.master, text="Schedule Messages", command=self.schedule_messages)
        schedule_messages_button.pack(side="left")

        # 状态标签和标签变量
        self.status = tk.StringVar()
        self.status.set("Status: Not logged in.")

        # 创建标签并将其添加到窗口中
        status_label = tk.Label(self.master, textvariable=self.status)
        status_label.pack(side="top")


    def login(self):
        # 获取用户输入
        api_id = self.api_id.get()
        api_hash = self.api_hash.get()
        phone_number = self.phone_number.get()

        # 登录Telegram
        self.client = TelegramClient("session", api_id, api_hash)
        self.client.start(phone_number)

        self.status.set("Logged in successfully.")

    def join_group(self):
        # 获取用户输入
        group_link = self.group_link.get()

        # 加入群组
        self.client(JoinChannelRequest(group_link))

        self.status.set("Joined group successfully.")


    def send_message(self):
        # 获取用户输入
        group_link = self.group_link.get()
        message = self.message.get()

        # 发送消息
        self.client.send_message(group_link, message)

        self.status.set("Message sent successfully.")

    def schedule_messages(self):
        # 获取用户输入
        group_link = self.group_link.get()
        message = self.message.get()
        interval = int(self.interval.get())

        # 定时发送消息
        now = datetime.now()
        schedule_time = datetime(now.year, now.month, now.day, now.hour, now.minute, 0) + timedelta(seconds=interval)
        while True:
            if datetime.now() >= schedule_time:
                self.client.send_message(group_link, message)
                schedule_time += timedelta(seconds=interval)
                self.status.set("Message sent successfully.")
            self.master.update()


root = tk.Tk()
app = TelegramUI(root)
root.mainloop()