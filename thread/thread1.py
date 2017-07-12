#coding: utf-8
import threading

def demo(start, end):
    for i in range(start, end):
        print(i)

#创建线程
t = threading.Thread(target=demo, args=(3, 6))

#启动线程
t.start()
