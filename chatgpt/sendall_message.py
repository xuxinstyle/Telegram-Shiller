from telethon import TelegramClient, events, connection
from telethon.errors.rpcerrorlist import PeerFloodError
import socks
import asyncio
# 填写你自己的 API ID 和 API hash
api_id = 11770907
api_hash = '7d820d4557af57f57ae3c5d40524ce80'

# 填写你自己的 Telegram 账号的手机号和密码
phone_number = '+8618826578873'
proxy = (socks.SOCKS5, '127.0.0.1', 7890)


# 填写你要发送的消息内容
message = '南山 西丽 地铁站B口 400米 60分钟 环保莞式服务，丝足，抓龙筋'

# 创建一个 Telegram 客户端
client = TelegramClient('session_name', api_id, api_hash)

# 登录到 Telegram 账号
client.start(phone_number, password = None)

# 获取当前账号已加入的所有群组
dialogs = client.get_dialogs()

# 遍历所有群组，向每个群组发送消息
for dialog in dialogs:
    if dialog.is_group:
        try:
            client.send_message(dialog.id, message)
            print(f'已向群组 {dialog.title} 发送消息')
        except PeerFloodError:
            print(f'无法向群组 {dialog.title} 发送消息：发送消息过于频繁')
        except Exception as e:
            print(f'无法向群组 {dialog.title} 发送消息：{e}')

# 退出客户端
client.disconnect()