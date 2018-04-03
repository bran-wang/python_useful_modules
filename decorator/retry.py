#!/usr/bin/env python
# encoding: utf-8

import requests
import time

def retry(attempt, sleep_time):
    def decorator(func):
        def wrapper(url, *args, **kwargs):
            count = 0
            while count < attempt:
                try:
                    print "Call {}".format(func.__name__)
                    print "Retry {} {} time".format(url, count)
                    return func(url, *args, **kwargs)
                except Exception as e:
                    count = count + 1
                time.sleep(sleep_time)
        return wrapper
    return decorator


@retry(attempt=3, sleep_time=60)
def get_response(url):
    r = requests.get(url)
    return r.content


if __name__ == "__main__":
    print get_response('http://www.oschina.net')
    #print get_response('http:///www.oschina')
