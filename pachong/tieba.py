# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup

import pymongo


client = pymongo.MongoClient('localhost', 27017)
tieba = client['tieba']   #具体连接到哪个数据库   不需要你创建数据库和表，默认会创建
time_list = tieba['time_list']   #具体连接到哪张表


start_url = 'https://tieba.baidu.com/p/5182673366?pn={}'

headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}

for i in range(1, 3):
    try:
        url = start_url.format(i)
        print url
        response = requests.get(url, timeout=20, headers=headers)
        print response.text
    except:
        print "error"

    soup = BeautifulSoup(response.text, 'lxml')

    data = soup.select('div.post-tail-wrap > span:nth-of-type(4)')
    for item in data:
        time_list.insert_one({'date':item.text[:10]})    #text取文本
        print item
