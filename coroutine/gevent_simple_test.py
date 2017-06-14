#! -*- coding:utf-8 -*-
import gevent
from gevent import monkey
import urllib2

monkey.patch_all()

def get_body(i):
  print "start", i
  urllib2.urlopen("http://cn.bing.com")
  print "end", i

tasks = [gevent.spawn(get_body, i) for i in range(3)]
gevent.joinall(tasks)



