#coding: utf-8
from threading import Thread

class MyThread(Thread):
    def __init__(self, begin, end):
        Thread.__init__(self)
        self.begin = begin
        self.end = end

    def run(self):
        # 调用线程start()方法执行这里的代码
        for i in range(self.begin, self.end):
            print(i)


#创建线程
t = MyThread(3, 6)

#启动线程
t.start()
