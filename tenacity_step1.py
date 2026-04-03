from tenacity import retry, stop_after_attempt, wait_fixed

counter = {"count": 0}

@retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
def ask_model():
    counter["count"] += 1
    print(f"开始第 {counter['count']} 次请求")

    if counter["count"] < 3:
        raise ConnectionError("模拟网络波动")

    return "模型成功返回结果"

result = ask_model()
print(result)
