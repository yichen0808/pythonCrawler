# 进程和线程:类似与Java
# 多线程
from threading import Thread
# 法一
# def fuc():
#     for i in range(100):
#         print(f"fuc:{i}")
# if __name__ == '__main__':
#     t = Thread(target=fuc)
#     t.start()
#     for i in range(100):
#         print(f"main:{i}")
class Mythread(Thread):
    def run(self):
        for i in range(100):
            print(f"fuc:{i}")
if __name__ == '__main__':
    t = Mythread()
    t.start()
    for i in range(100):
        print(f"main:{i}")
