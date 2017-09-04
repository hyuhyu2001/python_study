#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc: 常见面试题及答案
"""
import random

# 1、Python里面如何生成随机数生成[0, 1）之间的浮点数
random.random()
0.9322428827845128

# 生成指定范围的浮点数
random.uniform(1, 2)
1.8681591185822142

# 生成指定范围的整数
random.randint(1, 10)
7

# 指定范围，指定间隔生成随机数
random.randrange(10)
5
random.randrange(1, 10, 2)
7

# 从序列中获取一个随机元素，参数seq表示序列。
list1 = [1, 2, 3, 'a', 'this']
random.choice(list1)
1

# 从指定序列中随机获取指定长度的片断
list1 = [1, 2, 3, 'a', 'this']
random.sample(list1, 3)
[3, 'this', 'a']
random.sample(list1, 3)
['this', 3, 'a']

# 2、字符串逆序输出
# 方法一：
s = "abcdefg"
s[::-1]
'gfedcba'

# 方法二：
s = "abcdefg"
cList = list(s)
cList.reverse()
print("".join(cList))

# 方法三：
def reverseStr(ss):
    c = []
    for i in range(len(ss)):
        c.append(ss[i])
    c.reverse()  # 反转列表
    return ''.join(c)


if __name__ == '__main__':
    s = input("please input str: ")
    print(reverseStr(s))

# 3、判断一个字符串是否为回文字符串
def converted(s):
    ss = s[:]
    if len(ss) >= 2 and s == ss[::-1]:
        return True
    else:
        return False
if __name__ == "__main__":
    s = "abcdcba"
    print(converted(s))
    print(converted("adgede"))

# 4、随机生成100个数，然后写入文件
# 思路：
# 1、打开一个新文件，准备去写
# 2、随机生成一个数（整数或小数），并将该数写入文件中
# 3、循环第2步，直到完成100个随机数的生成
# 打开一个文件
fp = open("c:\\a.txt", "w")
for i in range(1, 101):
    # 生成一个随机整数
    n = random.randint(1, 1000)
    fp.write(str(i) + " " + str(n) + "\n")
fp.close()

# 5、给定dict = {'a': 3, 'bc': 5, 'c': 3, 'asd': 4, '33': 56, 'd': 0}，根据其键值进行排序
dict1 = {'a': 3, 'bc': 5, 'c': 3, 'asd': 4, '33': 56, 'd': 0}
# 按字典key，降序排列
sorted(dict1.items(), key=lambda i: i[0], reverse=True)
[('d', 0), ('c', 3), ('bc', 5), ('asd', 4), ('a', 3), ('33', 56)]

lambda i: i[0]
# 等价于：
def t(item):
    return item[0]

# 按字典key升序排列
sorted(dict1.items(), key=lambda i: i[0], reverse=False)
[('33', 56), ('a', 3), ('asd', 4), ('bc', 5), ('c', 3), ('d', 0)]

# 6、嵌套list排序
# 思路：利用列表数据结构提供的sort函数，对列表进行排序
list2 = [[1, 2], [4, 6], [3, 1]]
list2.sort(key=lambda x: x[0], reverse=False)
list2
[[1, 2], [3, 1], [4, 6]]
list2.sort(key=lambda x: x[1], reverse=False)
list2
[[3, 1], [1, 2], [4, 6]]

# 7、对a = [1, 3, 2, 2, 1, 5, 5, 3]
# 里面的元素去重，有几种方法，并写出来
# 方法一：set集合
a = [1, 3, 2, 2, 1, 5, 5, 3]
list(set(a))
[1, 2, 3, 5]

# 方法二：字典key的唯一性
a = [1, 3, 2, 2, 1, 5, 5, 3]
list(dict.fromkeys(a, 0))
# 或
dict.fromkeys(a, 0).keys()
[1, 2, 3, 5]

# 方法三：count计数
a = [1, 1, 3, 2, 2, 1, 5, 5, 3, 4]
n = 0
while n < len(a):
    if a.count(a[n]) > 1:
        a.remove(a[n])
        continue
    n += 1
print(a)

# 方法四：
list1 = [1, 4, 3, 3, 4, 2, 3, 4, 5, 6, 1]
reduce(lambda x, y: x if y in x else x + [y], [[]] + list1)
[1, 4, 3, 2, 5, 6]

# 8、有一个urf8编码的文件a.txt，文件路径是E盘根目录，请写一段程序逐行读入这个文本文件，并在屏幕（GBK编码）上打印出来

# import chardet  # 查看字符串的编码方式模块
fp = open("c:\\me.txt")
lines = fp.readlines()
fp.close()

for line in lines:
    print
    line.decode("utf-8").encode("gbk", "ignore")



