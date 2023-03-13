# 以下是一个基于 Telegram 的 Python 代码，可以实现自动群发消息，自动加入群组，定时群发信息和批量拉人进自己的群组的功能以及获取某个群里的所有用户 ID，获取所有和关键字有关的群组链接和群组名的功能。在使用前请注意替换变量的值，如你的 `api_id`，`api_hash`，`bot_token` 等。
#
# ```python

import asyncio
import time
import schedule
from telethon import TelegramClient, events
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
from telethon.tl.functions.channels import InviteToChannelRequest, GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch

# 替换为您的API ID 和 API Hash
api_id = YOUR_API_ID
api_hash = 'YOUR_API_HASH'

# 替换为您的 Bot Token
bot_token = 'YOUR_BOT_TOKEN'

# 替换为您的 Chat ID 和 Chat Link
chat_id = 'YOUR_CHAT_ID'
chat_link = 'YOUR_CHAT_LINK'

# 替换为您要拉进群组的用户 ID 列表
user_ids = [USER_ID_1, USER_ID_2, ...]

# 替换为您的关键字（用于搜索和筛选群组）
search_keyword = 'YOUR_SEARCH_KEYWORD'


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
        join_link = await client.import_chat_invite_link(chat_link)
        await client(InviteToChannelRequest(join_link.chat_id, [client.get_me().id]))
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
            await client(InviteToChannelRequest(chat, [user]))
            await asyncio.sleep(1)


# 定时发送消息
def schedule_messages():
    schedule.every(10).minutes.do(send_message)  # 每隔 10 分钟发送一条消息
    while True:
        schedule.run_pending()
        time.sleep(1)


# 获取指定群组的所有成员 ID
async def get_chat_members(chat_id):
    async with TelegramClient('session_name', api_id, api_hash) as client:
        await client.start(bot_token=bot_token)
        chat = await client.get_entity(chat_id)
        members = []
        async for participant in client.iter_participants(chat):
            if participant.bot == False:  # 排除机器人用户
                members.append(participant.id)
        return members


# 获取所有和关键字有关的群组的链接和群组名
async def get_chat_links():
    async with TelegramClient('session_name', api_id, api_hash) as client:
        await client.start(bot_token=bot_token)
        dialogs = await client(GetDialogsRequest(
            offset_date=None,
            offset_id=0,
            offset_peer=InputPeerEmpty(),
            limit=100,
            hash=0
        ))
        chats = [dialog.entity for dialog in dialogs.entities if dialog.is_group]
        chat_links = []
        for chat in chats:
            if search_keyword in chat.title:
                chat_links.append({'title': chat.title, 'link': 'https://t.me/joinchat/' +
                                                                (await client.export_chat_invite_link(chat.id)).split(
                                                                    '/')[-1]})
        return chat_links


# 主函数
if __name__ == '__main__':
    asyncio.run(join_chat())  # 加入群组并监听消息
    asyncio.run(add_members())  # 批量拉人进群组
    schedule_messages()  # 定时发送消息
    print(asyncio.run(get_chat_members(chat_id)))  # 获取指定群组的所有成员 ID
    print(asyncio.run(get_chat_links()))  # 获取所有和关键字有关的群组链接和群组名

    # 需要注意的一些问题：
    #
    # - 这里使用了
    # `GetDialogsRequest`
    # 方法获取
    # Telegram
    # 上的对话列表，然后逐个检查每个对话，如果该对话属于群组并包含指定的关键字，则将其存储为字典并添加到列表中。
    # - 在使用
    # `InviteToChannelR

    # equest
    # ` 方法将用户添加到群组中时，需要使用
    # `get_entity()`
    # 方法获取每个用户的实体以便可以将其作为参数传递给此方法。
    # - 在使用
    # `get_chat_invite_link()`
    # 方法获取邀请链接时，如果没有管理员权限，则需要先将机器人添加为群组管理员。
    # - 使用
    # `schedule`
    # 包可以实现定时发送消息。每个线程只能有一个事件循环，因此在主线程中使用
    # `schedule`
    # 包时不需要使用异步函数。
