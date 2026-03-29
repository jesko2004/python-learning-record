

"""
@retry
def never_gonna_give_you_up():
    print("Retry forever ignoring Exceptions, don't wait between retries")
    raise Exception

"""
"""

from tenacity import stop_after_attempt


@retry(stop=stop_after_attempt(3))
def stop_after_3_attempts():
    print("Stopping after 3 attempts")
    raise Exception


stop_after_3_attempts()
"""
"""
from tenacity import stop_after_attempt, stop_after_delay, wait_fixed


@retry(wait=wait_fixed(2))
def wait_2_s():
    print("Wait 2 second between retries")
    raise Exception

wait_2_s()
"""

"""
from tenacity import retry, stop_after_attempt, stop_after_delay, wait_fixed, wait_random, wait_exponential


@retry(wait=wait_fixed(3) + wait_random(0, 2))
def wait_fixed_jitter():
    print("Wait at least 3 seconds, and add up to 2 seconds of random delay")
    raise Exception

wait_fixed_jitter()

"""
"""
from tenacity import retry, stop_after_attempt, stop_after_delay, wait_fixed, wait_random, wait_exponential,wait_chain


@retry(wait=wait_chain(*[wait_fixed(3) for i in range(3)] +
                       [wait_fixed(7) for i in range(2)] +
                       [wait_fixed(9)]))
def wait_fixed_chained():
    print("Wait 3s for 3 attempts, 7s for the next 2 attempts and 9s for all attempts thereafter")
    raise Exception

wait_fixed_chained()
"""
"""
from tenacity import retry, retry_if_result, retry_if_exception_type, stop_after_attempt


class MyException(Exception):
	pass

@retry(reraise=True, stop=stop_after_attempt(3))
def raise_my_exception():
	raise MyException("Fail")

try:
	raise_my_exception()
except Exception as e:
	print(e)
	
"""
"""
from tenacity import retry, stop_after_attempt, retry_if_result


@retry(stop=stop_after_attempt(3))
def raise_my_exception():
	print('retrying.')
	raise Exception("Fail")

try:
	raise_my_exception.retry_with(stop=stop_after_attempt(4))()  # 运行时可以改变参数
except Exception:
	passfrom tenacity import retry, stop_after_attempt, retry_if_result, Retrying


def never_good_enough(arg1):
	print(arg1)
	raise Exception('Error')


def try_never_good_enough(max_attempts=3):
	retryer = Retrying(stop=stop_after_attempt(max_attempts), reraise=True)  # retryer 对象
	retryer(never_good_enough, 'I really do try')  # 将要重试的函数和参数传递进去

try_never_good_enough()
"""

import asyncio

from tenacity import retry, stop_after_attempt


@retry(stop=stop_after_attempt(3), reraise=True)
async def my_async_function(seconds):
	await asyncio.sleep(seconds)
	print(f'sleep {seconds}')
	raise Exception('Async Error')


loop = asyncio.new_event_loop()
loop.run_until_complete(my_async_function(1))