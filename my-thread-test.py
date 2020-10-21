from threading import Thread
from time import sleep

def threadFun(args1,args2):
    print("子线程  开始")
    print(f"函数的参数为：{args1},{args2}")
    sleep(3)
    print("子函数  结束")

thread=Thread(target=threadFun,args=('霍元甲','陈真'))

thread.start()

thread.join()

print("主线程结束")