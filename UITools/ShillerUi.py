import telethon
from telethon import TelegramClient, functions, sync, events
from config import tg_config
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
    def __init__(self, config, id, tkinterUi):
        self.m_config = config
        self.m_id = id
        self.ignorechannels={}
        self.tkinterUi = tkinterUi
        with open("./config/ignore_channel.txt", "r") as file:
            for line in file.readlines():
                self.ignorechannels[line.strip()] = 1

    def initChannel(self):
        self.connection(self.m_config.get_owner(self.m_id), self.m_config.get_t_id(self.m_id), self.m_config.get_t_hash(self.m_id))
        file = open("./config/"+self.m_config.get_owner(self.m_id)+"_channel.txt", "w")
        file1 = open("./config/channel.txt", "w")
        self.m_config.channel_list = []
        for dialog in self.client.iter_dialogs():
            try:
                chUsername = dialog.entity.username
                if dialog.is_group and (not dialog.is_user) and (chUsername is not None):

                    coutMsg = "群组:" + chUsername
                    self.tkinterUi.insert_new_line(coutMsg)

                    if chUsername is not None:

                        channelhttp = chUsername + "\n"
                        self.tkinterUi.insert_new_line(str(len(self.m_config.channel_list)))

                        self.m_config.channel_list.append(channelhttp)

                        file.write(channelhttp)
                        file1.write(channelhttp)

                        file.flush()
                        file1.flush()
            except Exception as e:
                self.tkinterUi.insert_new_line(e)

        file.close()
        file1.close()
        self.tkinterUi.insert_new_line("initChannel success !")
        self.disconnect()

    def connection(self, owner, t_id, t_hash, ip='127.0.0.1', port=7890):

        asyncio.set_event_loop(asyncio.SelectorEventLoop())

        self.client = TelegramClient(owner, t_id, t_hash, proxy=(socks.SOCKS5, ip, port))
        self.client.start()

        self.tkinterUi.insert_new_line(f"已登录帐户 {self.m_config.get_owner(self.m_id)} ")

    def disconnect(self):
        self.client.disconnect()

    def join_channel(self):
        self.connection(self.m_config.get_owner(self.m_id), self.m_config.get_t_id(self.m_id), self.m_config.get_t_hash(self.m_id))
        for var in self.m_config.channel_list:
            try:
                result = self.client(functions.channels.JoinChannelRequest(channel=var))
                self.tkinterUi.insert_new_line(f"{self.m_config.get_owner(self.m_id)}. 帐户  加入群组 {var}")
                time.sleep(2)

            except Exception as ex:
                self.tkinterUi.insert_new_line(ex)
                strs = str(ex).split(" ")
                if len(strs) >= 3 and strs[3].isnumeric():
                    sleeptime = int(strs[3])
                    self.tkinterUi.insert_new_line(f"sleep time :{sleeptime} s")
                    time.sleep(sleeptime)
                continue
        self.tkinterUi.insert_new_line("参加所有频道.")
        self.disconnect()

    def send_message(self):
        # time.sleep(self.pre_time)

        count = 0
        for var in self.m_config.channel_list:
            try:
                count = count + 1
                entity = self.client.get_entity(var)
                self.client.send_message(entity, self.m_config.advertising_message)
                self.tkinterUi.insert_new_line(f"{self.m_config.get_owner(self.m_id)}. 帐号发了一条消息。 内容：" + self.m_config.advertising_message(self.m_id) + " to " + str(var))
                print("________________________________________")
                time.sleep(1)

            except Exception as ex:
                print(ex)
                count = count + 1
                self.tkinterUi.insert_new_line(f"{self.m_config.get_owner(self.m_id)}.在 频道:" + str(var) + "  信息发送失败 ")
                print("________________________________________")

                time.sleep(1)

                continue
        currentTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(currentTime)



    def account(self):
        self.connection(self.m_config.get_owner(self.m_id), self.m_config.get_t_id(self.m_id), self.m_config.get_t_hash(self.m_id))
        #self.join_channel()
        self.send_message()
        tkinter.messagebox.showinfo(title='tips', message='send message success!!!')
        self.disconnect()
        print("disconnect success !")

    def send_by_win(self, text_box):
        path = self.m_config.telegram_path(self.m_id)
        os.startfile(path)
        self.tkinterUi.insert_new_line("open telegram " + path)
        time.sleep(2)
        count = 0
        for column in self.m_config.channel_list:
            value = self.ignorechannels.get(column.strip())
            if value:
                continue
            pyautogui.press('esc')
            pyautogui.press('esc')
            pyautogui.hotkey('ctrl', 'f')
            time.sleep(1)
            pyautogui.write(column)
            time.sleep(2)
            pyautogui.press('enter')
            time.sleep(2)
            advertising_message = self.m_config.advertising_message(self.m_id)

            pyperclip.copy(advertising_message)
            pyautogui.hotkey('ctrl', 'v')
            time.sleep(1)
            # pyautogui.write("nanshanxili   ");
            pyautogui.press('enter')
            pyautogui.press('esc')
            msg = "send message :" + advertising_message + " to " + column + " success!"
            self.tkinterUi.insert_new_line(msg)
            count = count + 1

        # tkinter.messagebox.showinfo(title='tips', message='send message success!!!')
        msg = 'The script executed successfully. send message ' + str(count) + '\n'
        self.tkinterUi.insert_new_line(msg)




