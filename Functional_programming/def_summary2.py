#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:
"""

#1、变量可以指向函数
f = abs  #f替代了abs函数
print f(-20) #结果20

#2、函数名其实就是指向函数的变量
#abs =len #abs代替了len的函数，abs就不能作为绝对值函数
#print abs([1,2,3])#结果3

'''
3、高阶函数：能接受函数做参数的函数
（1）变量可以指向函数
（2）函数的参数可以接收变量
（3）一个函数可以接收另一个函数作为参数
（4）能接收函数作参数的函数就是高阶函数
'''

'''
demo:接收abs函数
定义一个函数，接收x，y，f三个函数
其中x，y是数值；f是函数
'''
def add(x,y,f):
    return f(x)+f(y)
print add(5,9,abs) #结果:14

'''
4、什么是装饰器，以及装饰器原理
（1）定义了一个函数
（2）想在运行时动态增加功能
（3）又不想改动函数本身的代码
'''
#demo：希望对下列函数调用增加log功能，打印出函数调用
def f1(x):
    return x*2
def f2(x):
    return x*x
def f3(x):
    return x*x*x

#方法2：通过高阶函数返回新函数
def f1(x):
    return  x*2
def new_fn(f):
    '''装饰器函数'''
    def fn(x):
        print 'call'+f.__name__+'()'
        return f(x)
    return fn

g1 = new_fn(f1)#把函数当变量传入，g1就是fn
print g1(5) #打印g1（即fn），就是调用fn函数，5为参数
f1 = new_fn(f1) #f1的原始定义函数被彻底隐藏了
print f1(5)

#python内置的@语法就是为了简化装饰器调用
@new_fn  #等同于f1 = new_fn(f1)
def f1(x):
    return x*2
print f1(6)  #callf1()  ,12

'''
装饰器的作用
可以极大的简化代码，避免每个函数编写重复性代码
（1）打印日志：@log
（2）检测性能：@performance
（3）数据库事务：@transaction
（4）URL路由：@post('/register')
'''

