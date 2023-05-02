from telethon import TelegramClient, functions, sync, events
from NORMAL.Message import fetch_text, group0, group1, group2, group3,  fetch_text1, fetch_text2
import time
from telethon.errors import *
from threading import *
import asyncio
import socks
import re
import datetime




group0 = group0()
group1 = group1()
group2 = group2()
group3 = group3()
# group4 = group4()


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

        loop = asyncio.new_event_loop()
        # asyncio.set_event_loop(loop)

        asyncio.set_event_loop(asyncio.SelectorEventLoop())
        self.client = TelegramClient(self.owner, self.t_id, self.t_hash, proxy =(socks.SOCKS5, '127.0.0.1', 7890))
        self.client.start()
        print(f"已登录帐户 {self.owner} ")

    def join_channel(self):
        #first = False
        for var in self.channel_list:
            try:
                # if var == "https://t.me/gssy100":
                #     first = True
                #     continue

                # if first is False:
                #     continue

                result = self.client(functions.channels.JoinChannelRequest(channel=var))
                print(f"{self.owner}. 帐户  加入频道 {var} ")
                time.sleep(3)

            except Exception as ex:
                print(ex)
                strs = str(ex).split(" ")
                if strs[3].isnumeric():
                    sleeptime = int(strs[3])
                    print("sleep time :%s s", sleeptime)
                    time.sleep(++sleeptime)

        print("参加所有频道.")

    def send_message(self):
        time.sleep(self.pre_time)
        while True:
            count = 0
            for var in self.channel_list:
                try:
                    count = count + 1
                    entity = self.client.get_entity(var)
                    self.client.send_message(entity, self.message)
                    print(f"{self.owner}. 帐号发了一条消息。 内容：" + self.message + " to " + str(var))
                    print("________________________________________")

                    if (count % 3) == 0 and (self.interval == 1):
                        time.sleep(300)
                        count = 0
                except Exception as ex:
                    print(ex)
                    count = count + 1
                    print(f"{self.owner}.在 频道:" + str(var) + "  信息发送失败 ")
                    print("________________________________________")


                    continue
            currentTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(currentTime)
            time.sleep(7200)

    def account(self):
        self.connection()
        self.join_channel()
        #self.send_message()

channellist=[]
with open("channel.txt","r") as file:
    channellist = file.readlines()


id0 = Shill("20201483","7b0eeea50868a1744fadc74840f3a16c","+8617827198551",channellist,fetch_text(), 2400) #Account 0
id1 = Shill("11770907","7d820d4557af57f57ae3c5d40524ce80","+8618826578873",channellist,fetch_text(), 0) #Account 1
id2 = Shill("27791531","46a50576ec06eb952b322e03f88f0f40", "+8613691724231", channellist, fetch_text(), 600)
id3 = Shill("22641341","9bb6137509065c3676a09599407aed2c","+8613923782526",channellist,fetch_text(), 0) #Account 3
id4 = Shill("27543213","18c5a43c1da4b0e71b5ffc8c79ccc00e","+12142187553",channellist,"深圳🌸南山+丝足会所😘 龙井  天花板 会所", 0 ) #Account 3
id5 = Shill("27543213","18c5a43c1da4b0e71b5ffc8c79ccc00e","+8615070094026",channellist,"", 0 )
id6 = Shill("27543213","18c5a43c1da4b0e71b5ffc8c79ccc00e","66960245980",channellist,"", 0 )
#t1 = Thread(target=id0.account)
#t2 = Thread(target=id1.account)
#t3 = Thread(target=id2.account)
#t4 = Thread(target=id3.account)
#t5 = Thread(target=id4.account)
t6 = Thread(target=id5.account)
#t7 = Thread(target=id6.account)
#t1.start()
#t2.start()
#t3.start()
#t4.start()
#t5.start()
t6.start()
#t7.start()

#t1.join()
#t2.join()
#t3.join()
#t4.join()
#t5.join()
t6.join()
#t7.join()
