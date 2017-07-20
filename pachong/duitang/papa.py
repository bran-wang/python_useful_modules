#!/usr/bin/env python
# -*- coding:utf-8 -*-

import requests
import urllib.parse
import threading

#设置最大线程锁, 最多10个线程
thread_lock = threading.BoundedSemaphore(value=10)

#通过url获取数据
def get_page(url):
    # request.get 自带json.loads
    page = requests.get(url)
    page = page.content
    #bytes to str
    page = page.decode('utf-8')
    return page

def findall_in_page(page, startpart, endpart):
    all_strings = []
    end = 0
    while page.find(startpart, end) != -1:
        start = page.find(startpart, end) + len(startpart)
        end = page.find(endpart, start)
        string = page[start:end]
        all_strings.append(string)
    return all_strings

def pages_from_duitang(label):
    pages = []
    url = "http://www.duitang.com/napi/blog/list/by_search/?kw={}&start={}&limit=1000"
    label = urllib.parse.quote(label)
    #print(label)
    for index in range(0, 3600, 100):
        u = url.format(label, index)
        print(u)
        page = get_page(u)
        pages.append(page)
    return pages

def pic_urls_from_pages(pages):
    pic_urls = []
    for page in pages:
        urls = findall_in_page(page, 'path":"', '"')
        pic_urls.extend(urls)
    return pic_urls

def download_img(url, n):
    r = requests.get(url)
    path = 'pics/' + str(n) + '.jpg'
    with open(path, 'wb') as f:
        f.write(r.content)
    # unlock
    thread_lock.release()


def main(label):
    pages = pages_from_duitang(label)
    pic_urls = pic_urls_from_pages(pages)
    n = 0
    for url in pic_urls:
        n += 1
        print("正在下载第{}张图片".format(n))
        # lock
        thread_lock.acquire()
        t = threading.Thread(target=download_img, args=(url, n))
        t.start()


main("校花")


#url = "http://www.duitang.com/napi/blog/list/by_search/?kw=%E6%A0%A1%E8%8A%B1&start=0&limit=2"

#print(get_page(url))
