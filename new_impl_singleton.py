#!/usr/bin/env python
# encoding: utf-8

class SingleTon(object):
    _instance = dict()

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instance:
            cls._instance[cls] = super(SingleTon, cls).__new__(cls, *args, **kwargs)

        print cls._instance
        return cls._instance[cls]


a = SingleTon()
b = SingleTon()

print id(a)
print id(b)
