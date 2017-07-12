#coding: utf-8
from threading import Thread

'''
继承Thread类并在派生类中重写__init__()和run()方法。创建了线程对象以后，可以调用其start()方法来启动，该方法自动调用该类对象的run()方法，此时该线程处于alive状态，直至线程的run()方法运行结束。
'''

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
