# -*- coding: utf-8 -*-

import urllib
from bs4 import BeautifulSoup
import re

def getLiveids(url):
    html = urllib.urlopen(url)
    liveIds = set()
    bsObj = BeautifulSoup(html, 'html.parser')
    for link in bsObj.find_all('a', href=re.compile('^(/l/)')):
        if 'href' in link.attrs:
            newpage = link.attrs['href']
            liveId = re.findall("[0-9]+", newpage)
            liveIds.add(liveId[0])
    return liveIds


def getpage():
    liveIds = set()
    liveIds = getLiveids('http://www.huajiao.com/category/1000?pageno=1') | getLiveids('http://www.huajiao.com/category/1000?pageno=2')
    return liveIds

def getUserId(liveId):
    html = urllib.urlopen('http://www.huajiao.com/' + 'l/' + str(liveId))
    bsobj = BeautifulSoup(html, 'html.parser')
    text = bsobj.title.get_text()
    try:
        res = re.findall('[0-9]+', text)
        return res[0]
    except Exception:
        return 0

def getUserData(userid):
    print "getUserData:userId=", userid
    html = urllib.urlopen('http://www.huajiao.com/user/' + str(userid))
    bsobj = BeautifulSoup(html, 'html.parser')
    data = dict()
    try:
        userInfoObj = bsobj.find('div', {'id':'userInfo'})
        data['FAvatar'] = userInfoObj.find('div', {'class':'avatar'}).img.attrs['src']
        data['FUserId'] = userid
        tmp = userInfoObj.h3.get_text('|', strip=True).split('|')
        data['FUserName'] = tmp[0]
        data['FLevel'] = tmp[1]
        tmp = userInfoObj.find('ul', {'class':'clearfix'}).get_text('|', strip=True).split('|')
        data['FFollow'] = tmp[0]
        data['FFollowed'] = tmp[2]
        data['Fsupported'] = tmp[4]
        data['FExperience'] = tmp[6]
        return data
    except AttributeError:
        print str(userid) + u'出现错误' 
        return None


def main():
    for live in getpage():
        userId = getUserId(live)
        userdata = getUserData(userId)
        try:
            if userdata:
                print userdata
        except Exception as e:
            print e
    return 1


if __name__ == '__main__':
    main()


#url = 'http://www.huajiao.com/category/1000?pageno=1'
#print getLiveids(url)

#liveIds = getpage()
#for i in liveIds:
#    print getUserId(i)

