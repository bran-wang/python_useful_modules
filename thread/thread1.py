#coding: utf-8

'''
直接使用Thread类实例化一个线程对象并传递一个可调用对象作为参数
'''

import threading

def demo(start, end):
    for i in range(start, end):
        print(i)

#创建线程
t = threading.Thread(target=demo, args=(3, 6))

#启动线程
t.start()
