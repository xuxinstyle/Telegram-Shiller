from telethon import TelegramClient, functions, sync, events
from Message import fetch_text, group0, group1
import time
from telethon.errors import *
from threading import *
import asyncio

group0 = group0()
group1 = group1()
# group2 = group2()
# group3 = group3()
# group4 = group4()


class Shill():
    def __init__(self,T_id,T_hash,owner,group):
            self.t_id = T_id
            self.t_hash = T_hash
            self.owner = owner
            self.channel_list = group
            self.message = fetch_text()

    def connection(self):
        print("" + str(self.t_id))
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        self.client = TelegramClient(self.owner, self.t_id, self.t_hash)
        self.client.start()
        print("已登录帐户")

    def join_channel(self):
        for var in self.channel_list:
            try:
                result = self.client(functions.channels.JoinChannelRequest(channel=var))
                print(f"{self.owner}. 帐户  加入频道 {var}")
                time.sleep(3)

            except Exception as ex:
                print(ex)
                time.sleep(6)
                continue
        print("参加所有频道.")

    def send_message(self):
        while True:
            for var in self.channel_list:
                try:
                    entity = self.client.get_entity(var)
                    self.client.send_message(entity, self.message)
                    print(f"{self.owner}. 帐号发了一条消息。 内容：" + self.message + "to " + var)
                    print("________________________________________")
                    time.sleep(5)
                except Exception as ex:
                    print(ex)
                    time.sleep(10)
                    continue
            time.sleep(3600)

    def account(self):
        self.connection()
        self.join_channel()
        self.send_message()

id0 = Shill("20201483","7b0eeea50868a1744fadc74840f3a16c","+8617827198551",group0) #Account 0
id1 = Shill("11770907","7d820d4557af57f57ae3c5d40524ce80","+8618826578873",group1) #Account 1
# id2 = Shill("","","2",group2) #Account 2
# id3 = Shill("","","3",group3) #Account 3
# id4 = Shill("","","4",group4) #Account 4


t1 = Thread(target=id0.account)
t2 = Thread(target=id1.account)
# t3 = Thread(target=id2.account)
# t4 = Thread(target=id3.account)
# t5 = Thread(target=id4.account)


t1.start()
t2.start()
# t3.start()
# t4.start()
# t5.start()


t1.join()
t2.join()
# t3.join()
# t4.join()
# t5.join()

