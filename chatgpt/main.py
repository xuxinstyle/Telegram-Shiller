import asyncio
import time
import schedule
from telethon import TelegramClient, events

# 替换为您的 API ID 和 API Hash
api_id = YOUR_API_ID
api_hash = 'YOUR_API_HASH'

# 替换为您的 Bot Token
bot_token = 'YOUR_BOT_TOKEN'

# 替换为您的 Chat ID 和 Chat Link
chat_id = 'YOUR_CHAT_ID'
chat_link = 'YOUR_CHAT_LINK'

# 替换为您要拉进群组的用户 ID 列表
user_ids = [USER_ID_1, USER_ID_2, ...]


# 自动发送消息
async def send_message():
    async with TelegramClient('session_name', api_id, api_hash) as client:
        await client.start(bot_token=bot_token)
        chat = await client.get_entity(chat_id)
        await client.send_message(chat, "这是一条自动发送的消息")


# 自动加入并发送消息
async def join_chat():
    async with TelegramClient('session_name', api_id, api_hash) as client:
        await client.start(bot_token=bot_token)
        await client.join_chat(chat_link)
        chat = await client.get_entity(chat_id)
        await client.send_message(chat, "我加入了这个群组！")

        @client.on(events.NewMessage(chats=chat))
        async def handler(event):
            await client.send_message(chat, "我收到了新消息：{}".format(event.message.message))

        await client.run_until_disconnected()


# 批量拉人进群组
async def add_members():
    async with TelegramClient('session_name', api_id, api_hash) as client:
        await client.start(bot_token=bot_token)
        chat = await client.get_entity(chat_id)
        for user_id in user_ids:
            user = await client.get_entity(user_id)

    await client.add_chat_members(chat, [user])


# 定时发送消息
def schedule_messages():
    schedule.every(10).minutes.do(send_message)  # 每隔 10 分钟发送一条消息
    while True:
        schedule.run_pending()
        time.sleep(1)


# 主函数
if __name__ == '__main__':
    asyncio.run(join_chat())  # 加入群组并监听消息
    asyncio.run(add_members())  # 批量拉人进群组
    schedule_messages()  # 定时发送消息

# 需要注意的一些问题：
#
# - Telethon
# 包需要使用
# Python
# 的异步机制，因此使用
# `asyncio`
# 库和异步函数等。
# - `TelegramClient`
# 是与
# Telegram
# 进行交互的主要类。在使用
# `TelegramClient`
# 之前需要先调
