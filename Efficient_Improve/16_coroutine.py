# 协程:操作系统了解
import asyncio
import time


async def welcome():
    # time.sleep(1) 同步
    await asyncio.sleep(1) #awiat挂起,异步操作
    print("欢迎回家,达妮娅")
async def welcome1():
    await asyncio.sleep(2)
    print("欢迎回家,达妮娅")
async def welcome2():
    await asyncio.sleep(3)
    print("欢迎回家,达妮娅")
if __name__ == '__main__':
    async def main():
        f1 = welcome()
        # 或者f1 = asyncio.create_task(welcome1())
        f2 = welcome1()
        f3 = welcome2()
        await asyncio.gather(f1,f2,f3)
    asyncio.run(main())
