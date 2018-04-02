#!/usr/bin/env python
# encoding: utf-8

def singleton(cls):
    instances = dict()
    def _singleton(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return _singleton


@singleton
class Test(object):
    def __str__(self):
        return "id is {}\n".format(id(self))


if __name__ == '__main__':
    t1 = Test()
    t2 = Test()

    print t1
    print t2
