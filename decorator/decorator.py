__author__ = 'branw'

from time import ctime
from functools import wraps

def deco(tag):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kw):
            print "[%s] %s() is called, Tag is %s" % (ctime(), func.__name__, tag)
            return func(*args, **kw)
        return wrapper
    return decorator


@deco('Python')
def foo():
    print "Hello, Python"


@deco('Java')
def bar():
    print "Hello, Java"


foo()
bar()


'''
OUTPUT:
[Sun Jul 23 12:35:10 2017] foo() is called, Tag is Python
Hello, Python
[Sun Jul 23 12:35:10 2017] bar() is called, Tag is Java
Hello, Java
'''