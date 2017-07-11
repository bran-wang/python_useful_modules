#!/usr/bin/env python
# encoding: utf-8

import itchat
import time

CHATROOM_NAME = 'friend1'
CHATROOM = None

def get_chatroom():
    global CHATROOM
    if CHATROOM is None:
        itchat.get_chatrooms(update=True)
        chatrooms = itchat.search_chatrooms(CHATROOM_NAME)
        print "search chatrooms return: ", chatrooms 
        if chatrooms:
            return chatrooms[0]
        else:
            r = itchat.create_chatroom(itchat.get_friends()[:1], topic=CHATROOM_NAME)
            print u"新建群聊", r
            if r['BaseResponse']['Ret'] == 0:
                CHATROOM = {'UserName': r['ChatRoomName']}
                return CHATROOM
    else:
        return CHATROOM

def check_friends(friends, chatroom, num):
    deleted_list = []
    bad_list = []
    left, deleted, bad = num
    for friend in friends[1:]:
        print '\n', u"昵称:",friend['NickName'], u'  备注:', friend['RemarkName'], u'  签名:', friend['Signature']
        time.sleep(60)
        r = itchat.add_member_into_chatroom(chatroom['UserName'], [friend])
        print r
        if r['BaseResponse']['Ret'] == 0:
            status = r['MemberList'][0]['MemberStatus']
            itchat.delete_member_from_chatroom(chatroom['UserName'], [friend])
            if status == 3:
                bad = bad + 1
                bad_list.append(friend['NickName'])
            elif status == 4:
                deleted = deleted + 1
                deleted_list.append(friend['NickName'])
            else:
                left = left + 1
            print { 3: u'该好友已经将你加入黑名单。', 4: u'该好友已经将你删除。',}.get(status, u'该好友仍旧与你是好友关系。')
    print ""
    print ""
    print u"您还剩{}个好友".format(left)
    print u"惨惨惨，有{}个好友将您删除".format(deleted), u", 分别是", deleted_list
    print u"牛逼啊，有{}个好友将您拉黑".format(bad),  u", 分别是", bad_list


itchat.auto_login(enableCmdQR=2)

friends = itchat.get_friends()
chatroom = get_chatroom()
left, deleted, bad = 0, 0, 0
num = [left, deleted, bad]
check_friends(friends, chatroom, num)

#print u"您共有{}个好友".format(len(friends))


