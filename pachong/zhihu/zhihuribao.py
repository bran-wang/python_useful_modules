# -*- coding: utf-8 -*-

import urllib2, re
import requests
import HTMLParser

#import sys
#reload(sys)
#sys.setdefaultencoding('utf-8') #输出的内容是utf-8


user_agent = [
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X x.y; rv:42.0) Gecko/20100101 Firefox/42.0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_1 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.0 Mobile/14E304 Safari/602.1",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0)",
]

def getHtml(url):
    header = {
        "User-Agent": user_agent[1]
    }
    #request = urllib2.Request(url, headers=header) #用地址创建一个对象
    #response = urllib2.urlopen(request)
    #text = response.read()

    # changed by bran, you can see requests is powerful, and urlopen sometimes occur error
    html = requests.get(url, headers=header)
    text = html.content
    return text


#获取超链接
def getUrl(html):
    pattern = re.compile('<a href="/story/(.*?)"', re.S)
    items = re.findall(pattern, html)

    urls = []
    for item in items:
        urls.append("http://daily.zhihu.com/story/" + item)
        print urls[-1]
    return urls


def getContent(url):
    html = getHtml(url)

    #标题
    pattern = re.compile('<h1 class="headline-title">(.*?)</h1>')
    items = re.findall(pattern, html)
    print items[0]

    #正文
    pattern = re.compile('<div class="content">\\n<p>(.*?)</div>', re.S)
    items_withtag = re.findall(pattern, html)
    for item in items_withtag:
        print item


def main():
    url = "http://daily.zhihu.com/"
    html = getHtml(url)
    urls = getUrl(html)
    for u in urls:
        try:
            getContent(u)
        except Exception,e:
            print e


if __name__ == "__main__":
    main()