import requests
import json

# 设置代理
proxies = {
    'http': 'http://127.0.0.1:7890',
    'https': 'http://127.0.0.1:7890'
}
headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer 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'
}

data = {
     "model": "gpt-3.5-turbo",
     "messages": [{"role": "user", "content": "中国有多少人口"}],
     "temperature": 0.7
}

# 发送POST请求
response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, data=json.dumps(data), proxies=proxies)

# 打印响应内容
print(response.text)