#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:内部排序-交换排序-快速排序
快速排序：选择一个基准元素,通常选择第一个元素或者最后一个元素,通过一趟扫描，将待排序列分成两部分,一部分比基准元素小,一部分大于等于基准元素,
    此时基准元素在其排好序后的正确位置,然后分别对这两部分记录用同样的方法继续进行排序，直到整个序列有序
分析：快速排序通常被认为在同数量级（O(nlog2n)）的排序方法中平均性能最好的。但若初始序列按关键码有序或基本有序时，快排序反而蜕化为冒泡排序。
    为改进之，通常以“三者取中法”来选取基准记录，即将排序区间的两个端点与中点三个记录关键码居中的调整为支点记录。快速排序是一个不稳定的排序方法。
实现过程：
步骤1：将大于flag的放在右边，将小于flag的放在左边，以flag，分成两个子list，left和right
步骤2：在left和right中分别再选择flag，将left和right，继续拆分成两个子list，依次类推（递归）
步骤3：直到n=1，即每个list都只有一个元素，整个过程 : n/2x = 1  x = log2n
"""

def quick_sort1(lists):
    '''步骤1：将大于flag的放在右边，将小于flag的放在左边，以flag，分成两个子list'''
    flag = lists[-1] #选定最后一个元素作为flag
    i = -1 #定义游标i和游标j，i指向大于flag的元素，j指向小于flag的元素，将i初始化到-1的位置
    for j in range(len(lists)-1):#将j初始化到0的位置
        if lists[j] < flag:
            i+=1
            tmp = lists[i]
            print(tmp)
            lists[i] = lists[j]
            lists[j] = tmp
            print(lists)
    print("\n" + "*"*20 + "\n")

    tmp = lists[-1]
    print(tmp)
    lists[-1] = lists[i+1]
    lists[i+1] = tmp

    return lists

def partition(lists, left, right):
    """步骤1：找到基准位置, 并返回"""
    pivot_index = left
    pivot = lists[left]

    for i in range(left + 1, right + 1):
        if lists[i] < pivot:
            # 如果此处索引的值小于基准值, 基准值的位置后移一位
            # 并将后移一位的值和这个值交换, 让基准位置及之前的始终小于基准值
            pivot_index += 1
            if pivot_index != i:
                lists[pivot_index], lists[i] = lists[i], lists[pivot_index]

    # 将基准值移动到正确的位置
    lists[left], lists[pivot_index] = lists[pivot_index], lists[left]

    return pivot_index

def quicksort(lists, left, right):
    '''只有left < right 排序,，调用partition函数，递归进行排序'''
    if left < right:
        pivot_index = partition(lists, left, right)
        quicksort(lists, left, pivot_index - 1)
        quicksort(lists, pivot_index + 1, right)
    return lists

def quick_sort2(lists, left, right):
    '''快速排序,一步实现'''
    if left >= right:
        return lists
    key = lists[left]
    low = left
    high = right
    while left < right:
        while left < right and lists[right] >= key:
            right -= 1
        lists[left] = lists[right]
        while left < right and lists[left] <= key:
            left += 1
        lists[right] = lists[left]
    lists[right] = key
    quick_sort2(lists, low, left - 1)
    quick_sort2(lists, left + 1, high)
    return lists


if __name__ == '__main__':
    lists = [7,8,16,17,9,10,14,4,2,10]
    result = quick_sort2(lists,0,len(lists)-1)
    print(result)
