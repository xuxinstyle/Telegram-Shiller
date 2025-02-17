# coding=utf-8
import telethon
from telethon import TelegramClient, functions, sync, events
from Message import fetch_text, fetch_list
import time
from telethon.errors import *
from threading import *
import asyncio
from telethon.tl.functions.channels import InviteToChannelRequest
import socks

from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
from time import sleep
import socks
import asyncio

offset = 0
limit = 100
all_participants = []

# https://www.jianshu.com/p/0f61dd28d969?utm_campaign=maleskine    这是中国的教程

class Shill():
    def __init__(self,T_id,T_hash,owner, time = 0):
            self.t_id = T_id
            self.t_hash = T_hash
            self.owner = owner
            self.channel_list = fetch_list()
            self.message = fetch_text()
            self.pre_time = time

    def connection(self):


        asyncio.set_event_loop(asyncio.SelectorEventLoop())
        self.client = TelegramClient(self.owner, self.t_id, self.t_hash, proxy=(socks.SOCKS5, '127.0.0.1', 7890))
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

    def GetParticipantsInfo(self, channel_id):

        participants = self.client(GetParticipantsRequest(
            channel_id, ChannelParticipantsSearch(''), offset, limit, 0 ))
        if not participants.users:
            print("not participants.users")
        all_participants.extend(participants.users)
        channelusers = []
        for par in all_participants:
            if par.username is not None:
                channelusers.append(par.username)
        print(channelusers)
        self.AddChatUse(self.GetMainChannelid(), all_participants)

        for var in self.channel_list:
            friend_info = self.client.get_entity(var)  # dialog.title为first_name
            if type(friend_info) is not telethon.tl.types.User:
                channel_id = friend_info.id
                channel_title = friend_info.title
                channel_username = friend_info.username
                dict_channel_info = {"channel_id": channel_id, "channel_title": channel_title,
                                     "channel_username": channel_username}
                print(channel_title, "这是一个频道", dict_channel_info)


    def GetMainChannelid(self):
        friend_info = self.client.get_entity("xiuchejiaoliu666")
        if type(friend_info) is not telethon.tl.types.User:
            channel_id = friend_info.id
            channel_title = friend_info.title
            channel_username = friend_info.username
            dict_channel_info = {"channel_id": channel_id, "channel_title": channel_title,
                                 "channel_username": channel_username}
            return channel_id

    async def GetChannelInfo(self):
        dialogs = await self.client.get_dialogs()
        for dialog in dialogs:
            friend_info = await self.client.get_entity(dialog.title)  # dialog.title为first_name
            print(type(friend_info))
            if type(friend_info) == telethon.tl.types.Channel:
                channel_id = friend_info.id
                channel_title = friend_info.title
                channel_username = friend_info.username
                dict_channel_info = {"channel_id": channel_id, "channel_title": channel_title,
                                     "channel_username": channel_username}

                await self.client.send_message(friend_info, "南山 西丽 地铁站B口 400米 60分钟 环保莞式服务，丝足，抓龙筋")
                print(dialog.title, "这是一个频道", dict_channel_info)
                # self.GetParticipantsInfo(channel_id)
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

        my_channel = self.client.get_entity(dialogs.title)
        print(my_channel)

    def AddChatUse(self, channelid, userlist):
        self.client(InviteToChannelRequest(
            channel=channelid,  # 频道id
            users=userlist,  # 列表格式的username
        ))


    def send_message(self):
        while True:
            time.sleep(self.pre_time)
            for var in self.channel_list:
                try:
                    entity = self.client.get_entity(var)
                    self.client.send_message(entity, self.message)
                    print(f"{self.owner}. 帐号发了一条消息。 内容："+self.message + "to " + var)
                    print("________________________________________")
                    time.sleep(10)
                except Exception as ex:
                    print(ex)
                    print(ex.args)
                    time.sleep(10)
                    continue
            time.sleep(4500)

    def account(self):
        self.connection()
        self.GetChannelInfo()
        #self.GetParticipantsInfo("")
        # self.join_channel()
        #self.send_message()


#id0 = Shill("20201483","7b0eeea50868a1744fadc74840f3a16c","+8617827198551") # Telegram account info
id0 = Shill("11770907","7d820d4557af57f57ae3c5d40524ce80","+8618826578873") #Account 1
target=id0.account()
# t1 = Thread(target=id0.account)
#
# t1.start()
#
# t1.join()
