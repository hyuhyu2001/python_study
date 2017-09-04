#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:内部排序-插入排序-直接插入排序
    算法适用于少量数据的排序.
    将一个记录插入到已排序好的有序表中，从而得到一个新，记录新增1的有序表。
    即：先将序列的第一个记录看成是一个有序的子序列，然后从第2个记录逐个进行插入，直至整个序列有序为止。
 如果碰见一个和插入元素相等的，那么插入元素把想插入的元素放在相等元素的后面。
 所以，相等元素的前后顺序没有改变，从原无序序列出去的顺序就是排好序后的顺序，所以插入排序是稳定的。
"""

def direct_insertion_sort(lists):
    '''直接插入排序,方法1'''
    for i in range(1,len(lists)):
        tmp = lists[i]
        j = i-1
        while j>= 0:
            if tmp < lists[j]:
                lists[j+1] = lists[j]
                lists[j] = tmp
                print(lists)
            j -= 1
    return lists

def direct_insertion_sort2(lists):
    '''直接插入排序,方法2'''
    for i in range(1, len(lists)):
        if lists[i] < lists[i - 1]:
            tmp = lists[i]
            j = i - 1
            lists[j + 1] = lists[j]

            j = j - 1
            while j >= 0 and lists[j] > tmp:
                lists[j + 1] = lists[j]
                j = j - 1
                lists[j + 1] = tmp
    return lists

if __name__ == '__main__':
    lists = [5,8,6,7,9,4,2,1]
    result = direct_insertion_sort2(lists)
    print(result)
