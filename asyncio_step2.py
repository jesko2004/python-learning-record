import os
import asyncio
from openai import OpenAI

api_key = os.getenv("DEEPSEEK_API_KEY")

if not api_key:
    raise ValueError("没有找到 DEEPSEEK_API_KEY，请先在终端设置环境变量。")

client = OpenAI(
    api_key=api_key,
    base_url="https://api.deepseek.com",
)

def ask_deepseek_sync(question):
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "你是一个耐心的编程学习助手，请用简单中文回答。"},
            {"role": "user", "content": question},
        ],
        temperature=1.3,
    )
    return response.choices[0].message.content

async def ask_deepseek(question):
    if "pytest" in question:
      raise ValueError("这是我故意制造的测试错误")

    print(f"开始提问：{question}")

    try:
        answer = await asyncio.to_thread(ask_deepseek_sync, question)
        return question, answer, None
    except Exception as e:
        return question, None, e

async def main():
    questions = [
        "什么是 asyncio？",
        "pytest 有什么作用？",
        "tenacity 是做什么的？",
    ]

    tasks = [asyncio.create_task(ask_deepseek(question)) for question in questions]

    print("\n按完成顺序输出：")
    for completed_task in asyncio.as_completed(tasks):
        question, answer, error = await completed_task

        print(f"\n问题：{question}")
        if error:
            print("状态：失败")
            print(f"错误信息：{error}")
        else:
            print("状态：成功")
            print("回答：")
            print(answer)

asyncio.run(main())
