#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:读取excel操作
"""

import os,sys
from datetime import date,datetime
import xlrd

newpath = os.chdir( r'D:\python_pycharmWorkspace\python36\python_study\excel_study') #改变当前目录到指定的目录
testfile = r"[]V6.2功能拆分 - 细分.xlsx"
file = os.path.join(os.getcwd(),testfile)
if not os.path.isfile(file):
    print('文件路径不存在')
    sys.exit()
xl = xlrd.open_workbook(file)#xl = xlrd.open_workbook(r"D:\python_pycharmWorkspace\python36\python_study\excel_study\[]V6.2功能拆分 - 细分.xlsx")
print(xl.sheet_names()) #获取所有sheet的名字：结果：['里程碑', '汇总', '选车', '我问老司机', '商城', '其他', '我是小二', '4S店']
table1 = xl.sheet_by_name('里程碑')#根据sheet名称获取sheet内容,
table2 = xl.sheet_by_index(1)#根据sheet索引获取sheet内容,获取第二个sheet
print(table2.name) #获取sheet的名称
print(table1.nrows) #获取sheet的行数
print(table1.ncols)  #获取sheet的列数

print(table1.row_values(0))#获取第1行的值
print(table1.row_values(3))#获取第4行的值
print(table1.col_values(0))#获取第1列的值
print(table1.col_values(3))#获取第4列的值
print(table1.cell(1,2).value)#获取第2行，第3列单元格的值
print(table1.cell_value(1,2))#获取第2行，第3列单元格的值
print(table1.cell_type(1,3))#获取单元格内容的数据类型，2为num
print(table1.cell(1,2).ctype)#获取单元格内容的数据类型，1为str
#ctype : 0 empty,1 string, 2 number, 3 date, 4 boolean, 5 error
print(table1.cell_value(1,4)) #日期类型，显示的时候按下面的方式处理
def date_handle(row,col):
    if (table1.cell_type(row,col) == 3):
        date_value = xlrd.xldate_as_tuple(table1.cell_value(col,col),xl.datemode)
        date_tmp = date(*date_value[:3]).strftime('%Y/%m/%d')
    print(date_value) #结果 (2017, 4, 12, 0, 0, 0)
    return date_tmp #结果  2017/04/12
result = date_handle(1,4)
print(result)
print(table1.cell_value(5,0))#结果为：我问老司机
print(table1.cell_type(6,0))#获取单元格内容的数据类型，0为empty
print(table1.cell_value(6,0))#结果为空,因为是合并单元格的原因，他只是合并的第一个单元格有值，其他的为空。这个是真没技巧，只能获取合并单元格的第一个cell的行列索引，才能读到值，读错了就是空值
#通过这种方式查看，循环列数据
for i in range(table1.nrows):
    print(table1.col_values(0)[i])
'''
#如何获取合并的单元格，需要将formatting_info参数设置为True，默认是False，所以上面获取合并的单元格数组为空
formatting_info=True只在xlrd的早期版本里支持，后期版本不在支持
workbook = xlrd.open_workbook(file,formatting_info=True)
sheet1 = workbook.sheet_by_name('里程碑')
merge = []
for (rlow,rhigh,clow,chigh) in sheet1.merged_cells:
  merge.append([rlow,clow])
print(merge)
'''

