from telethon import TelegramClient, functions, sync, events
from Message import fetch_text, group0, group1, group2, group3,  fetch_text1, fetch_text2
import time
from telethon.errors import *
from threading import *
import asyncio
import socks
import re
import datetime
import tkinter
import tkinter.messagebox

import pyautogui

import pyperclip
import pandas
import time

import os


class Shill():
    def __init__(self,T_id,T_hash,owner,group, message = fetch_text(), time = 0, interval = 0 ):
        self.t_id = T_id
        self.t_hash = T_hash
        self.owner = owner
        self.channel_list = group
        self.message = message
        self.pre_time = time
        self.interval = interval

    def connection(self):
        # loop = asyncio.new_event_loop()
        # asyncio.set_event_loop(loop)

        asyncio.set_event_loop(asyncio.SelectorEventLoop())

        self.client = TelegramClient(self.owner, self.t_id, self.t_hash, proxy =(socks.SOCKS5, '127.0.0.1', 7890))
        self.client.start()

        print(f"已登录帐户 {self.owner} ")

    def disconnect(self):
        self.client.disconnect()

    def join_channel(self):
        for var in self.channel_list:
            try:
                result = self.client(functions.channels.JoinChannelRequest(channel=var))
                print(f"{self.owner}. 帐户  加入频道 {var}")
                time.sleep(10)

            except Exception as ex:
                print(ex)
                time.sleep(10)
                continue
        print("参加所有频道.")

    def send_message(self):
        # time.sleep(self.pre_time)

        count = 0
        for var in self.channel_list:
            try:
                count = count + 1
                entity = self.client.get_entity(var)
                self.client.send_message(entity, self.message)
                print(f"{self.owner}. 帐号发了一条消息。 内容：" + self.message + " to " + str(var))
                print("________________________________________")
                time.sleep(0)
                if (count % 3) == 0 and (self.interval == 1):
                    time.sleep(1)
                    count = 0
            except Exception as ex:
                print(ex)
                count = count + 1
                print(f"{self.owner}.在 频道:" + str(var) + "  信息发送失败 ")
                print("________________________________________")

                if (count % 3) == 0 and (self.interval == 1):
                    time.sleep(1)
                    count = 0
                continue
        currentTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(currentTime)



    def account(self):
        self.connection()
        #self.join_channel()
        self.send_message()
        tkinter.messagebox.showinfo(title='tips', message='send message success!!!')
        self.disconnect()
        print("disconnect success !")




