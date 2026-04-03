from tenacity import (
    retry,
    stop_after_attempt,
    wait_fixed,
    retry_if_exception_type,
)

counter = {"count": 0}


def log_before_sleep(retry_state):
    print(f"第 {retry_state.attempt_number} 次失败")
    print(f"错误原因: {retry_state.outcome.exception()}")
    print("准备 1 秒后重试...\n")


@retry(
    stop=stop_after_attempt(3),
    wait=wait_fixed(1),
    retry=retry_if_exception_type(ConnectionError),
    before_sleep=log_before_sleep,
    reraise=True,
)
def ask_model():
    counter["count"] += 1
    print(f"开始第 {counter['count']} 次请求")

    raise ConnectionError("模拟网络一直失败")


try:
    ask_model()
except Exception as e:
    print("最终失败：", e)
