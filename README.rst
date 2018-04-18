Well, I didnt do much just fixed to properly support Baidu v3, all credits go to the original authors

some docs
https://translate.googleusercontent.com/translate_c?act=url&depth=1&hl=ru&ie=UTF8&prev=_t&rurl=translate.google.com&sl=zh-CN&sp=nmt4&tl=en&u=http://push.baidu.com/doc/restapi/restapi&xid=17259,15700023,15700124,15700149,15700168,15700173,15700186,15700201&usg=ALkJrhjzVvfE74uxeux5tjyUJU4s73wR6Q

https://translate.googleusercontent.com/translate_c?act=url&depth=1&hl=ru&ie=UTF8&prev=_t&rurl=translate.google.com&sl=zh-CN&sp=nmt4&tl=en&u=http://push.baidu.com/doc/restapi/msg_struct&xid=17259,15700023,15700124,15700149,15700168,15700173,15700186,15700201&usg=ALkJrhiff3Ej16G2QZUPLHPNzvvIyabZ2Q

https://github.com/HelloWorldDev/api-service/blob/master/src/Being/Push/Message/BaiduMessage.php

Original memo is below

百度云推送服务端SDK Python版本
==============================

将百度云推送（Push）服务端的所有 API 封装成一个类 `BaiduPush`，通过对该类的简单初始化，即可调用其内部的各种方法，使用百度云推送服务。

`BaiduPush` 提供的方法和服务端 API 对应，是对服务端 REST API 的封装，详细的 REST API 请参考 `官网API列表 <http://developer.baidu.com/wiki/index.php?title=docs/cplat/push/api/list>`_ 。


代码构成
--------

*   `baidupush/baidupush.py` -- SDK 脚本，包含对外提供的所有接口
*   `sample/sample.py` -- 使用 SDK 的 Demo 文件


依赖库
------

* `requests <http://python-requests.org>`_

* `ujson <https://github.com/esnme/ultrajson>`_


一般规则
---------

* 所有函数的参数和返回值中如果有中文，必须是UTF-8编码
* 不需要对函数参数进行urlencode
* 错误信息见 `错误码定义 <http://developer.baidu.com/wiki/index.php?title=docs/cplat/push/api#JSON.E5.93.8D.E5.BA.94.E7.BC.96.E7.A0.81>`_


安装
----

::

    pip install baidupush

或者

::

    easy_install baidupush


调用方法
---------

::

    from baidupush import BaiduPush, BaiduPushError
    apikey = "76Yi0ZBGGV2HrAziIiYEFtRh"
    secretkey = "xxxxxxxxxxxxx"
    user_id = "1105115563847474869"
    channel_id = 3944730196422489622

    message = "{'title':'baidu push','description':'message from python sdk'}"
    message_key = "key1"

    pusher = BaiduPush(apikey, secretkey)
    push_type = BaiduPush.PUSH_TO_USER
    optional = dict()
    optional[BaiduPush.USER_ID] = user_id
    optional[BaiduPush.CHANNEL_ID] = channel_id
    optional[BaiduPush.MESSAGE_TYPE] = BaiduPush.PUSH_NOTIFICATION
    try:
        ret = pusher.push_msg(push_type, message, message_key, optional)
    except BaiduPushError:
        print 'Exception :', err
    print ret


版本更迭
----------

该 Python SDK 主要由 `luvchh <https://github.com/Argger/pusher_python_sdk>`_ 完成了大部分的工作

**第一版：**

由 `luvchh <https://github.com/Argger/pusher_python_sdk>`_ 提供

**第二版：**

由 `blacklaw0 <https://github.com/blacklaw0/pusher_python_sdk>`_ 修改

**第三版：**

由 `gfreezy <https://github.com/gfreezy>`_ 修改

**第四版：**

由 `cheng-shiwen <https://github.com/cheng-shiwen/Baidu-Push-Server-SDK-Python>`_ 更新

**第五版：**

由 `sinchb <https://github.com/quatanium/python-baidu-push-server>`_ 修改

