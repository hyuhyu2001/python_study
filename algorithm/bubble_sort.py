#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:内部排序-交换排序-冒泡排序
冒泡排序是一种简单的排序，也是笔试中经常出的题目。
冒泡排序：重复走访需要遍历的元素，一次比较两个元素，将小的元素展现在前面，最终要求就是数组里的集合按小到大排列。
    这个算法的名字由来就是因为越小的元素会经由交换慢慢“浮”到数列的顶端
基本思想：在要排序的一组数中，对当前还未排好序的范围内的全部数，自上而下对相邻的两个数依次进行比较和调整，
        让较大的数往下沉，较小的往上冒。即：每当两相邻的数比较后发现它们的排序与排序要求相反时，就将它们互换。
"""

def bubble_sort1(a):
    '''从后往前依次遍历，把最小的数字沉到数组的最后'''
    # print(range(len(a)))  #range(0, 9)
    # for j in range(len(a))[::-1]:# 方法1：等同于range(8, -1, -1)
    for j in range(len(a)-1,0,-1):#方法2：等同于range(8, 0, -1)
        for i in range(j):
            if a[i] > a[i+1]:
                a[i],a[i+1]= a[i+1],a[i]
    return a

def bubble_sort2(a):
    '''从前往后依次遍历，把最小的数字沉到数组的最后'''
    count=len(a)
    for i in range(count):
        for j in range(i+1,count):
            if a[i]>a[j]:
                a[i],a[j]=a[j],a[i]
    return a

def bubble_sort3(a):
    '''同2,比2更好理解'''
    count=len(a)
    for i in range(1,count):
        for j in range(0,count-1):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a


def bubble_sort4(a):
    '''通过while和for循环实现'''
    flag = len(a) - 1
    while (flag > 0):
        k = flag
        flag = 0
        for j in range(k):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                flag = j
    return a


if __name__ == '__main__':
    a = [2,1,6,7,9,4,4,2,3]
    #a.sort(reverse=False)  #对于列表，可以直接通过sort进行排序
    result = bubble_sort3(a)
    print(result)
    # for j in range(len(a) - 1, 0, -1):
    #     print(j)
