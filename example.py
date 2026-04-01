import os
from openai import OpenAI

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("没有找到 OPENAI_API_KEY，请先在终端设置环境变量。")

client = OpenAI(api_key=api_key)

try:
    response = client.responses.create(
        model="gpt-5.4",
        input="请用简单的话解释什么是大语言模型。"
    )
    print("模型返回结果：")
    print(response.output_text)
except Exception as e:
    print("调用失败：", e)
