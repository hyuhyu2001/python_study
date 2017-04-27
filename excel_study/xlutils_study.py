#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:xluntils进行修改excel操作
"""

import os,sys
import xlrd
import xlutils.copy


newpath = os.chdir( r'D:\python_pycharmWorkspace\python36\python_study\excel_study')
testfile = r"[]V6.2功能拆分 - 细分.xlsx"
file = os.path.join(os.getcwd(),testfile)
if not os.path.isfile(file):
    print('文件路径不存在')
    sys.exit()
xl = xlrd.open_workbook(file)#xl = xlrd.open_workbook(r"D:\python_pycharmWorkspace\python36\python_study\excel_study\[]V6.2功能拆分 - 细分.xlsx")

wb = xlutils.copy.copy(xl)  #复制xl文件

ws = wb.get_sheet(0) #通过get_sheet()获取的sheet有write()方法
ws.write(0,0,'changed')
wb.save(r'D:\python_pycharmWorkspace\python36\python_study\excel_study\xlutils_save.xls')#只能复制内容，不能复制格式，且不能保存为xlsx文件

def write_append(file_name):
    '''
    附带样式的copy
　　xlrd打开文件，必须加参数formatting_info=True,不过高版本xlrd已经不支持formatting_info
    '''
    values = ["Ann", "woman", 22, "UK"]

    r_xls = xlrd.open_workbook(file_name)
    r_sheet = r_xls.sheet_by_index(0)
    rows = r_sheet.nrows
    w_xls = xlutils.copy.copy(r_xls)
    sheet_write = w_xls.get_sheet(0)

    for i in range(0, len(values)):
        sheet_write.write(rows, i, values[i])

    w_xls.save(file_name + '.out' + os.path.splitext(file_name)[-1]);

if __name__ == '__main__':
    write_append("./[]V6.2功能拆分 - 细分.xlsx")

