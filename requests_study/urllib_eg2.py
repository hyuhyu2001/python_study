#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:
"""
import urllib
import urllib2

def get_simple():
    url = 'http://reg.haibian.com/login/ajax_login'
    #定义请求数据，并且对数据进行复制
    data = {}
    data['loginname'] = 'student08@qq.com'
    data['password'] = '11111'
    #对请求数据进行编码
    data =  urllib.urlencode(data)
    #将数据和url进行连接
    request = url + '?' + 'data'
    #打开请求、获取对象
    requestResponse = urllib2.urlopen(request)
    #读取服务端返回的数据
    ResponseStr = requestResponse.read()
    #打印数据
    ResponseStr = ResponseStr.decode('unicode_escape')  #将unicode转换为utf-8 "\u8d26\u6237\u540d\u4e0d\u80fd\u4e3a\u7a7a" 转换为"账户名不能为空"
    print(ResponseStr)

def post_simple():
    url = 'http://xapi.kybyun.com/user/login'
    #定义请求数据，并且对数据进行复制
    headers = {}
    headers = {'host':'xapi.kybyun.com',
               'Connection':'keep-alive'}
    data = {}
    data['loginname'] = 'student08@qq.com'
    data['password'] = '11111'
    #数据编码以及赋值
    data =  urllib.urlencode(data)
    req = urllib2.Request(url,data,headers)
    #打开地址并赋值给变量
    ResponseStr =urllib2.urlopen(req)
    #读取获得的值
    ResponseStr = ResponseStr.read()
    #将获得的结果进行转码
    ResponseStr = ResponseStr.decode('unicode_escape')  #将unicode转换为utf-8 "\u8d26\u6237\u540d\u4e0d\u80fd\u4e3a\u7a7a" 转换为"账户名不能为空"
    print(ResponseStr)

if __name__ == '__main__':
    post_simple()

