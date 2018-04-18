#!/usr/bin/env python
# coding=utf-8

import sys
import time
sys.path.append("../")
from baidupush import BaiduPush

# 以下只是测试数据，请使用者自行修改为可用数据
apikey = ""
secretkey = ""
user_id = ""
channel_id = 

message = "{'title':'baidu push','description':'message from python sdk'}"
message_key = "key1"
tagname = "test_tag"

def test_pushMessage_to_user():
    c = BaiduPush(apikey, secretkey)
    push_type = BaiduPush.PUSH_TO_USER
    optional = dict()
    optional[BaiduPush.USER_ID] = user_id
    optional[BaiduPush.CHANNEL_ID] = channel_id
    # 推送通知类型
    #optional[BaiduPush.MESSAGE_TYPE] = BaiduPush.PUSH_NOTIFICATION
    optional[BaiduPush.MESSAGE_TYPE] = BaiduPush.PUSH_MESSAGE

    ret = c.push_msg(push_type, message, message_key, optional)
    print ret

def test_pushMessage_to_tag():
    c = BaiduPush(apikey, secretkey)
    push_type = BaiduPush.PUSH_TO_TAG
    tag_name = 'push'
    optional = dict()
    optional[BaiduPush.TAG_NAME] = tag_name
    ret = c.push_msg(push_type, message, message_key, optional)
    print ret

def test_pushMessage_to_all():
    c = BaiduPush(apikey, secretkey)
    push_type = BaiduPush.PUSH_TO_ALL
    optional = dict()
    ret = c.push_msg(push_type, message, message_key, optional)
    print ret


def test_queryBindList():
    c = BaiduPush(apikey, secretkey)
    optional = dict()
    optional[BaiduPush.CHANNEL_ID] = channel_id
    ret = c.query_bindlist(user_id, optional)
    print ret

def test_verifyBind():
    c = BaiduPush(apikey, secretkey)
    optional = dict()
    optional[BaiduPush.DEVICE_TYPE] = BaiduPush.DEVICE_ANDRIOD
    ret = c.verify_bind(user_id, optional)
    print ret

def test_fetchMessage():
    c = BaiduPush(apikey, secretkey)
    ret = c.fetch_msg(user_id)
    print ret

def test_deleteMessage():
    c = BaiduPush(apikey, secretkey)
    msg_id = "111"
    ret = c.delete_msg(user_id, msg_id)
    print ret

def test_setTag():
    c = BaiduPush(apikey, secretkey)
    optional = dict()
    optional[BaiduPush.USER_ID] = user_id
    ret = c.set_tag(tagname, optional)
    print ret

def test_fetchTag():
    c = BaiduPush(apikey, secretkey)
    ret = c.fetch_tag()
    print ret

def test_deleteTag():
    c = BaiduPush(apikey, secretkey)
    optional = dict()
    optional[BaiduPush.USER_ID] = user_id
    ret = c.delete_tag(tagname, optional)
    print ret

def test_queryUserTag():
    c = BaiduPush(apikey, secretkey)
    ret = c.query_user_tag(user_id)
    print ret

def test_queryDeviceType():
    c = BaiduPush(apikey, secretkey)
    ret = c.query_device_type(channel_id)
    print ret

if __name__ == '__main__':
    test_pushMessage_to_user()
    time.sleep(1)
    #test_pushMessage_to_tag()
    #time.sleep(1)
    #test_pushMessage_to_all()
    #time.sleep(1)
    #test_queryBindList()
    #time.sleep(1)
    #test_verifyBind()
    #time.sleep(1)
    #test_fetchMessage()
    #time.sleep(1)
    #test_deleteMessage()
    #time.sleep(1)
    #test_setTag()
    #time.sleep(1)
    #test_fetchTag()
    #time.sleep(1)
    #test_deleteTag()
    #time.sleep(1)
    #test_queryUserTag()
    #time.sleep(1)
    #test_queryDeviceType()
    #time.sleep(1)
