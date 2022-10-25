from telethon import TelegramClient, functions, sync, events
from Message import fetch_text, group0, group1, group2, group3,  fetch_text1, fetch_text2
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
        print("" + str(self.t_id))
        # loop = asyncio.new_event_loop()
        # asyncio.set_event_loop(loop)

        asyncio.set_event_loop(asyncio.SelectorEventLoop())
        self.client = TelegramClient(self.owner, self.t_id, self.t_hash, proxy =(socks.SOCKS5, '127.0.0.1', 7890))
        self.client.start()
        print("已登录帐户")

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
                    time.sleep(3)
                    if (count % 3) == 0 and (self.interval == 1):
                        time.sleep(300)
                        count = 0
                except Exception as ex:
                    print(ex)
                    count = count + 1
                    print(f"{self.owner}.在 频道:" + str(var) + "  信息发送失败 ")
                    print("________________________________________")
                    time.sleep(10)
                    if (count % 3) == 0 and (self.interval == 1):
                        time.sleep(300)
                        count = 0
                    continue
            currentTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            print(currentTime)
            time.sleep(4800)

    def account(self):
        self.connection()
        #self.join_channel()
        self.send_message()

id0 = Shill("20201483","7b0eeea50868a1744fadc74840f3a16c","+8617827198551",group0,fetch_text(), 1200) #Account 0
id1 = Shill("11770907","7d820d4557af57f57ae3c5d40524ce80","+8618826578873",group1,fetch_text(), 0) #Account 1
id2 = Shill("27791531", "46a50576ec06eb952b322e03f88f0f40", "+8613691724231", group2, fetch_text1(), 2400)
id3 = Shill("22641341","9bb6137509065c3676a09599407aed2c","+8613923782526",group3,fetch_text2(), 600 ) #Account 3
# id4 = Shill("","","4",group4) #Account 4


t1 = Thread(target=id0.account)
t2 = Thread(target=id1.account)
t3 = Thread(target=id2.account)
#t4 = Thread(target=id3.account)
# t5 = Thread(target=id4.account)


t1.start()
t2.start()
t3.start()
#t4.start()
# t5.start()


t1.join()
t2.join()
t3.join()
#t4.join()
# t5.join()

