#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:
"""

class Person(object):
    def __init__(self,name,male):
        self.name=name
        self.male=male

    def get_name(self):
        print self.name

    def __str__(self):  #定义__str__方法
        return '(Person: %s, %s)' %(self.name, self.male)
        '''因为Python定义了__str__()和__repr__()两种方法，__str__()用于显示给用户，而__repr__()用于显示给开发人员。有一个偷懒的定义__repr__的方法'''
        __repr__ == __str__


lst = [1,2,3]
print lst  #非实例正常打印：[1,2,3]
p = Person('李阳','男')
print p  #打印实例结果 <__main__.person object at 0x02614C90>  #增加__str__方法后，可以直接打印出p的结果

#问题来了，person如何把任意变量变成str？
#因为任何一个数据类型都有一个特殊方法：__str__
print lst.__str__() #[1, 2, 3]
print p.__str__() #<__main__.person object at 0x02614C90>

'''
1、如何给Person类加上__str__这个特殊方法'
用于print的__str__
用于len的__len__
用于cmp的__cmp__
……
特殊方法定义在class中
不需要直接调用
Python的某些函数或操作符会调用对应的特殊方法
2、正确实现特殊方法
（1）只需要编写用到的特殊方法
（2）有关联性的特殊方法都必须实现
__getattr__ ; __setattr__ ; __delattr__
'''