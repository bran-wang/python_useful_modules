# -*- coding: utf-8 -*-

__author__ = 'branw'

import gevent

#先进入协程test1，打印12
#遇到”gevent.sleep(0)”时，test1被阻塞，自动切换到协程test2，打印56
#之后test2被阻塞，这时test1阻塞已结束，自动切换回test1，打印34
#当test1运行完毕返回后，此时test2阻塞已结束，再自动切换回test2，打印78
#所有协程执行完毕，程序退出

def test1():
    print 12
    gevent.sleep(2)
    print 34


def test2():
    print 56
    gevent.sleep(0)
    print 78


def main():
    jobs = []
    jobs.append(gevent.spawn(test1))
    jobs.append(gevent.spawn(test2))
    gevent.joinall(jobs)


if __name__ == "__main__":
    main()


#gevent提供了”monkey.patch_all()”方法将所有标准库都替换。
from gevent import monkey;monkey.patch_all()
import socket

urls = ["www.baidu.com", "www.gevent.org", "www.python.org"]

jobs = [gevent.spawn(socket.gethostbyname, url) for url in urls]

gevent.joinall(jobs, timeout=5)

print [job.value for job in jobs]




#获取协程状态
def win():
    return "you win"

def fail():
    raise Exception("you failed")

winner = gevent.spawn(win)

loser = gevent.spawn(fail)

print winner.started
print loser.started

try:
    gevent.joinall([winner, loser])
except Exception as e:
    print "this will never be reached"

print winner.ready()
print loser.ready()

print winner.value
print loser.value

print winner.successful()
print loser.successful()

print loser.exception


#我们将超时设为2秒，此后所有协程的运行，如果超过两秒就会抛出”Timeout”异常
from gevent import Timeout

timeout = Timeout(2)

timeout.start()

def wait():
    gevent.sleep(10)

try:
    gevent.spawn(wait).join()
except Timeout:
    print "Could not completed"


#我们也可以将超时设置在with语句内，这样该设置只在with语句块中有效
with Timeout(1):
    gevent.sleep(10)

#此外，我们可以指定超时所抛出的异常，来替换默认的”Timeout”异常。比如下例中超时就会抛出我们自定义的”TooLong”异常。
class Toolong(Exception):
    pass

with Timeout(1, Toolong):
    gevent.sleep(10)



# greenlet协程间的异步通讯可以使用事件（Event）对象。该对象的”wait()”方法可以阻塞当前协程，
# 而”set()”方法可以唤醒之前阻塞的协程。在下面的例子中，5个waiter协程都会等待事件evt，
# 当setter协程在3秒后设置evt事件，所有的waiter协程即被唤醒。
#
from gevent.event import Event

evt = Event()

def setter():
    print "wait for me"
    gevent.sleep(3)  # 3秒后唤醒所有在evt上等待的协程
    print "OK, i'm done"
    evt.set() # 唤醒

def waiter():
    print "i am waiting for you"
    evt.wait()
    print "Finish waiting"

gevent.joinall([
    gevent.spawn(setter),
    gevent.spawn(waiter),
    gevent.spawn(waiter),
    gevent.spawn(waiter),
    gevent.spawn(waiter),
    gevent.spawn(waiter),
])


#除了Event事件外，gevent还提供了AsyncResult事件，它可以在唤醒时传递消息。让我们将上例中的setter和waiter作如下改动:
from gevent.event import AsyncResult
aevt = AsyncResult()

def setter():
    print "wait for me"
    gevent.sleep(3)
    print "Ok, i am done"
    aevt.set("Hello!")  # 唤醒，并传递消息

def waiter():
    print "i am waiting for you"
    message = aevt.get()
    print "Got wake up message: %s" % message

gevent.joinall([
    gevent.spawn(setter),
    gevent.spawn(waiter),
    gevent.spawn(waiter),
    gevent.spawn(waiter),
    gevent.spawn(waiter),
    gevent.spawn(waiter),
])



#队列Queue的概念相信大家都知道，我们可以用它的put和get方法来存取队列中的元素。
# gevent的队列对象可以让greenlet协程之间安全的访问。运行下面的程序，
# 你会看到3个消费者会分别消费队列中的产品，且消费过的产品不会被另一个消费者再取到：

from gevent.queue import Queue
products = Queue()

def consumer(name):
    while not products.empty():
        print '%s got product %s' % (name, products.get())
        gevent.sleep(0)
    print '%s Quit' % name

def producer():
    for i in xrange(1, 10):
        products.put(i)

gevent.joinall([
    gevent.spawn(producer),
    gevent.spawn(consumer, 'steve'),
    gevent.spawn(consumer, 'john'),
    gevent.spawn(consumer, 'nancy'),
])

#put和get方法都是阻塞式的，它们都有非阻塞的版本：put_nowait和get_nowait。
# 如果调用get方法时队列为空，则抛出”gevent.queue.Empty”异常。


#信号量可以用来限制协程并发的个数。它有两个方法，acquire和release。
# 顾名思义，acquire就是获取信号量，而release就是释放。当所有信号量都已被获取，
# 那剩余的协程就只能等待任一协程释放信号量后才能得以运行：

from gevent.coros import BoundedSemaphore
sem = BoundedSemaphore(2)

def worker(n):
    sem.acquire()
    print('Worker %i acquired semaphore' % n)
    gevent.sleep(0)
    sem.release()
    print('Worker %i released semaphore' % n)

gevent.joinall([gevent.spawn(worker, i) for i in xrange(0, 6)])




#同线程类似，协程也有本地变量，也就是只在当前协程内可被访问的变量
from gevent.local import local
data = local()

def f1():
    data.x = 1
    print data.x

def f2():
    try:
        print data.x
    except AttributeError:
        print "x is not visible"

gevent.joinall([
    gevent.spawn(f1),
    gevent.spawn(f2)
])

#通过将变量存放在local对象中，即可将其的作用域限制在当前协程内，当其他协程要访问该变量时，就会抛出异常。
# 不同协程间可以有重名的本地变量，而且互相不影响。因为协程本地变量的实现，
# 就是将其存放在以的”greenlet.getcurrent()”的返回为键值的私有的命名空间内。
