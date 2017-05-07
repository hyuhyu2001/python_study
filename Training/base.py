#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:python基础培训,基于python3.6
Py3.X源码文件默认使用utf-8编码
"""
import operator
import sys
import os


def number_base():
    '''数字示例'''
    anint = 1
    along = -555555555555555  #python3以后不支持long整形，改为int整型，2的写法along = -555555555555L
    afloat = 9.384E-23
    acomplex = 1.334+4.5433j
    # print(type(anint + along + afloat + acomplex))  #支持不同的数字类型相加
    # print(type(along))
    print(type(str(along)))  #str转换为str
    print(int(str(along),8)) #转换为8进制
    print(operator.lt(anint,along))  #python3不支持cmp比较函数，改为用operator模块的lt、le等函数
    #
    print( abs( 1.334- 4.5433j)) #返回绝对值，如果参数是一个复数，那么就返回 math.sqrt(num.real2 + num.imag2)
    print(divmod( 10, 3))#返回包含商和余数的元组
    print (round( 3.34345, 2))#常用于浮点数，进行四舍五入运算，返回和第一参数最接近的整数，第2个参数告诉round函数精确到小数点后几位
    print(ord('%')) # 接受一个ASCII或 Unicode字符（长度为1的字符串），返回相应的ASCII值或 Unicode值

def string_base():
    '''字符串示例'''
    # print(dir('str'))
    # print(help('str'))
    # print("hello,my name's alex li")
    # print('Bob said \"I\'m OK\".') #通过转译符实现
    # print(r'''"To be, or not to be": that is the question.\
    # Whether it's nobler in the mind to suffer.''')#加前缀r表示自然字符串，不需要转译;跨行用三引号
    # print(1 + 2 \
    # + 4 + 5) # '\'表示拆为两行

    #print(isinstance('jim', str)) #判断对象的类型
    # print(operator.lt( '12345'[0: 3], '123bc'[ 0: 3]))
    #
    # print("hello,%s,%s enough"%('world' ,'not'))   #字符串是 %s;整数 %d;浮点数%f
    # print("{who} turned {age} this year".format(age=88,who="she"))
    # stock = ['paper', "envelopes", "notepads ", "pens"]
    # print("we have {0[1]} and {0[2]} in stock".format(stock))
    #
    # d = 'abcdefghijklmnop'
    # print(d[1:10:2]) #从1开始，每隔2元素取一次，分别取1 3 5 7 9 结果： bdfhj
    # print(d[::2]) #从0开始到末尾，分别取0 2 4 6... 结果 acegikmo
    # print(d[::- 1]) #负数代表从末尾开始取，步长=1，结果为 ponmlkjihgfedcba
    # print(d[::- 2])#步长=2，结果为pnljhfdb
    #
    # enmu = 'fo'
    # # for i, t in enumerate(enmu):
    # #     print(i,t)
    #
    # print(zip(enmu))
    # print(type(zip(enmu)))
    # a = zip(enmu)
    # for i in a: #需要通过循环打印出来
    #     print(i)
    # print(sorted([5, 2, 3, 1, 4], reverse= True)) #reverse= True时倒序排列
    #
    # print('*** SPAM * for * everyone!!! ***'.strip('*!' ) )#同时去除首尾包含*和！的字符 结果：SPAM * for * everyone
    # print(' hello world!'.title())#结果： Hello World!
    # seq = ['1', '2', '3', '4', '5']
    # sep = '+'
    # print('+'.join(seq))  #join函数非常重要，连接字符串，也可以将列表元组等转换为字符串，与之对应的函数是split()
    sepseq = '1+2+3+4+5'
    print(sepseq.split('+'))
    # print('''1+2+3
    # # +4+5'''.splitlines(1)) #splitlines()按照行风格
    # dd ='$$$ Get rich now!!! $$$'
    # print(dd.find('$$$',0,50))
    # print(dd.count('$$$'))
    # #
    # u = '中文'  # 指定字符串类型对象u
    # str = u.encode('gb2312') #以gb2312编码对u进行编码，获得bytes类型对象str
    # print(str)
    # u1 = str.decode('gb2312')#以gb2312编码对字符串str进行解码，获得字符串类型对象u1
    # print(u1)


def list_base():
    '''列表处理'''
    # Ed = ["Gumby", 42]  # 直接声明
    # AD = 'hello', 'world'  # 通过list()创建  list(AD)=['hello', 'world']
    # AED= [Ed,AD,list(AD),("Smith",50)]
    # AED[2] = 'upt' #将下标2的元素更新为upt
    # AED.append('last')
    # print(AED.count('last'))
    # AED.extend(['1', '2', '3', '4'])
    # AED.insert(2, 'ins')
    # print(AED)
    # dd = ['1','2','3']
    # print(sorted(dd,reverse = True))
    ee = [('a',1),('b',2)] #    ee = （('a',1),('b',2)）
    for data in ee:
        print('%s,%s'% data)

def dict_base():
    '''字典处理'''
    name_info = {
        'name':'jacky',
        'age':'29',
        'job':'Engineer'
    }
    aa=dict.fromkeys(['a','b','c'],0)
    # print(aa)
    bb= dict(zip([1,2,3], [4,5,6]))
    # print(bb)
    # print('name' in name_info)
    # print(name_info.has_key( 'user'))
    # print(name_info.keys())
    # print(name_info.values())
    # print(name_info.items())
    # print(name_info[ 'name'])
    # print(name_info.get( 'name'))
    # name_info['salary'] = 3000  # 相当于新增
    # name_info.setdefault('name', 'king')#有值则不更新，无值则更新
    # name_info.setdefault('sex', '男')
    # print(name_info)
    # for i in name_info:
    #      print(i,name_info[i])
    aa.update(bb)#bb合并到aa，aa有变化，bb没变化
    print(aa)
    print(bb)

def file_base():
    '''文件处理'''

    f = open('myFile.txt','r+')
    # f.seek(0,os.SEEK_CUR)
    # f.write('DASDAD')
    # f.writelines(['大大\n','发放\n','发发发\n'])
    # # print(f.tell())
    # # print(f.tell())
    # # print(f.readline())
    # # print(f.read())
    # # f.flush()
    #
    # print(f.mode)
    # print(f.encoding)
    # print(f.closed)
    # print(f.readlines())
    # f.write('100')
    # for line in iter(f):
    #     print(line)
    print(os.getcwd())
    file = os.path.join(os.getcwd(),'myFile.txt')
    print(file)

if __name__ == '__main__':
    list_base()

