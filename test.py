import asyncio
import time


# 同步执行
def sync_task():
    time.sleep(2)  # 模拟耗时任务


print("同步模式开始")
sync_task()
sync_task()
sync_task()
print("同步模式结束")


# 异步执行
async def async_task():
    await asyncio.sleep(2)  # 异步等待


async def main():
    print("异步模式开始")
    await asyncio.gather(async_task(), async_task(), async_task())
    print("异步模式结束")


asyncio.run(main())
