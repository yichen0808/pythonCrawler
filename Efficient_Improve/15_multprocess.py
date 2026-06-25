from multiprocessing import Process
# 同14
from concurrent.futures import ThreadPoolExecutor,ProcessPoolExecutor
# 线程和进程池
with ThreadPoolExecutor(50) as t:
    for i in range(1,10000):
        t.submit("函数",f"参数{i}")