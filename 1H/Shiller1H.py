# coding=utf-8
import telethon
from telethon import TelegramClient, functions, sync, events
from Message import fetch_text, fetch_list
import time
from telethon.errors import *
from threading import *
import asyncio

from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
from time import sleep
offset = 0
limit = 100
all_participants = []

# https://www.jianshu.com/p/0f61dd28d969?utm_campaign=maleskine    这是中国的教程

class Shill():
    def __init__(self,T_id,T_hash,owner):
            self.t_id = T_id
            self.t_hash = T_hash
            self.owner = owner
            self.channel_list = fetch_list()
            self.message = fetch_text()

    def connection(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        self.client = TelegramClient(self.owner, self.t_id, self.t_hash)
        self.client.start()
        print("已登录帐户")

    def join_channel(self):
        for var in self.channel_list:
            try:
                result = self.client(functions.channels.JoinChannelRequest(channel=var))
                print(f"{self.owner}. 帐户 {var} 登录您的频道.")
                time.sleep(300)

            except Exception as ex:
                print(ex)
                time.sleep(600)
                continue
        print("参加所有频道.")

    def GetChannelInfo(self):
        dialogs = self.client.get_dialogs()
        for dialog in self.client.iter_dialogs():
            friend_info = self.client.get_entity(dialog.title)  # dialog.title为first_name
            if type(friend_info) is not telethon.tl.types.User:
                channel_id = friend_info.id
                channel_title = friend_info.title
                channel_username = friend_info.username
                dict_channel_info = {"channel_id": channel_id, "channel_title": channel_title,
                                     "channel_username": channel_username}
                print(dialog.title, "这是一个频道", dict_channel_info)
            else:
                if friend_info.bot is False:
                    user_id = friend_info.id
                    user_name = friend_info.username
                    is_bot = friend_info.bot
                    user_phone = friend_info.phone
                    dict_user_info = {'user_id': user_id, 'user_name': user_name, 'user_phone': user_phone,
                                      'is_bot': is_bot}
                    print(dialog.title, "这是一个用户", dict_user_info)
                else:
                    bot_id = friend_info.id
                    bot_name = friend_info.username
                    is_bot = friend_info.bot
                    dict_bot_info = {'bot_id': bot_id, 'bot_name': bot_name, 'is_bot': is_bot}
                    print(dialog.title, '这是一个机器人', dict_bot_info)
        # 打印群信息
        print(self.client.get_entity("@hello")) # 可更换群组名
        my_channel = self.client.get_entity(dialogs.title)
        print(my_channel)
    def GetParticipantsInfo(self):
        participants = self.client(GetParticipantsRequest(
            1387666944, ChannelParticipantsSearch(''), offset, limit, hash=0
        ))
        if not participants.users:
            print("no find users");
            return
        all_participants.extend(participants.users)
        for par in all_participants:
            print(par)

    def send_message(self):
        while True:
            for var in self.channel_list:
                try:
                    entity = self.client.get_entity(var)
                    self.client.send_message(entity, self.message)
                    print(f"{self.owner}. 帐号发了一条消息。 内容："+self.message + "to " + var)
                    print("________________________________________")
                    time.sleep(5)
                except Exception as ex:
                    print(ex)
                    print(ex.args)
                    time.sleep(10)
                    continue
            time.sleep(3600)

    def account(self):
        self.connection()
        # self.GetChannelInfo()
        # self.join_channel()
        self.send_message()


#id0 = Shill("20201483","7b0eeea50868a1744fadc74840f3a16c","+8617827198551") # Telegram account info
id0 = Shill("11770907","7d820d4557af57f57ae3c5d40524ce80","+8618826578873") #Account 1
t1 = Thread(target=id0.account)

t1.start()

t1.join()
