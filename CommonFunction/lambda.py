#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:
"""

#三元运算以及lambda表达式
temp = None
if 1>3:
    tmp = 'gt'
else:
    temp = 'lt'
print temp
#三元运算,如此简洁的运算，一次性搞定，便是三元运算
result = 'gt' if 1>3 else 'lt'
print result
'''
# lambda表达式，相当于执行了一个函数 ，一个temp变量，接受了两个参数x和y，也可以定义一个参数或者多个 temp = lambda x:x*y
temp = lambda x, y: x + y  # lambda为匿名函数（就是没有名的函数）
print temp(4, 10)
'''
def foo(x,y):
    return x+y

print foo(4,10)
'''

print map(lambda x: x * 2, range(10))
print map(lambda x: x ** x, range(10))

'''