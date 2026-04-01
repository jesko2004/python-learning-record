import os
from openai import OpenAI

api_key = os.getenv("DEEPSEEK_API_KEY")

if not api_key:
    raise ValueError("没有找到 DEEPSEEK_API_KEY，请先在终端设置环境变量。")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.deepseek.com",
)

try:
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "你用非常不耐烦的语气回答我"},
            {"role": "user", "content": "你好，今天天气怎么样"},
        ],
        temperature=1.3,
    )

    print("模型返回结果：")
    print(response.choices[0].message.content)

except Exception as e:
    print("调用失败：", e)
