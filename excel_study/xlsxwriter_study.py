#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     jinzj
@desc:写入excel操作
"""

import datetime
import xlsxwriter

workbook = xlsxwriter.Workbook('test.xlsx')#创建一个excel文件,每次打开会清空。。
worksheet = workbook.add_worksheet('test') #在文件中创建一个名为test的sheet，不加名字默认为sheet1

worksheet.set_column('A:A',20)#设置第一列宽度为20,'A:A'是一个列的范围，这里就是A列，如果是A到E列就是'A:E'。

bold = workbook.add_format({'bold':True})#设置一个加粗的格式对象
#border：边框，align:对齐方式，bg_color：背景颜色，font_size：字体大小，bold：字体加粗
top = workbook.add_format({'border':1,'align':'center','bg_color':'cccccc','font_size':13,'bold':True})


worksheet.write('A1','HELLO') #在A1单元格上写上hello
worksheet.write('A2','WORLD',top) #在A2单元格上写上world，并且采用top的格式
worksheet.write('B2','中文测试',bold)#在B2单元格上写上中文测试，并且设置为加粗

worksheet.write(2,0,32)#使用行列的方式写上数字32
worksheet.write(3,0,35.5)#使用行列的时候第一行起始为0,所以2,0代表着第三行的第一列,等价于A4
worksheet.write(4,0,'=SUM(A3:A4)')

worksheet.write(5,0,'重新新增')
worksheet.write_blank(6,0,None)#写入空类型数据worksheet.write(6,0,'')
worksheet.write(7,0,'ftp://www.python.org')

worksheet.write_datetime(8,0,datetime.datetime.strptime('2017-04-14','%Y-%m-%d'),workbook.add_format({'num_format':'yyyy-mm-dd'}))#写入日期类型数据

worksheet.insert_image('E2','E:\My Documents\My Pictures\搞笑图片\上衣标准.png', {'x_scale':0.2, 'y_scale':0.2})#插入一张图片,并通过 {'x_scale':0.2, 'y_scale':0.2}进行缩放，如果大于1便是放大
worksheet.insert_image('B9','E:\My Documents\My Pictures\搞笑图片\超隐晦的广告.jpg',{'url':'http://www.baidu.com','x_scale':0.5, 'y_scale':0.5})#例如插入一个图片的超链接为www.python.org

worksheet.write_column('P2',['1','2','3','4'])#写入到一列,后面接一个数组。从P2开始，依次写入excel第P列的4行中
worksheet.write_row('Q1',['5','6','7','8'])#写入到一行,后面接一个数组。从P2开始，依次写入excel，写入到4列中

def write_loop(bold,money):
    '''循环写入到excel'''
    expense=(['Rent',1000,'2017-04-09'],['Gas',100,'2017-04-10'],['Food',300,'2017-04-11'],['Gym',50,'2017-04-12'])

    worksheet1 = workbook.add_worksheet('test_loop')
    # Write some data headers. 带自定义粗体blod格式写表头
    worksheet1.write('A1', 'Item', bold)
    worksheet1.write('B1', 'Cost', bold)
    worksheet1.set_column('A:C', 20)  # 设置第1列至第3列宽度为20

    row = 1
    col = 0
    for item,cost,date_str in (expense):
        worksheet1.write(row,col,item) # 带默认格式写入
        worksheet1.write(row,col+1,cost,money)  # 带自定义money格式写入
        worksheet1.write_datetime(row,col+2,datetime.datetime.strptime(date_str,"%Y-%m-%d"),workbook.add_format({'num_format':'yyyy-mm-dd'}))
        row += 1
    worksheet1.write(row,0,'Total')
    BN = ''.join(['B','%d'%(int(row))])
    worksheet1.write(row, 1, '=SUM(B1:%s)'%BN,money)


def write_loop_format():
    '''excel自定义格式'''
    # Add a bold format to use to highlight cells. 设置粗体，默认是False
    bold = workbook.add_format({'bold': True})
    # Add a number format for cells with money.  定义数字格式
    money = workbook.add_format({'num_format': '$#,##0'})
    write_loop(bold,money)

def write_loop_chart():
    '''生成柱形图
    更多图表类型说明:
    area:创建一个面积样式的图表;
    bar:创建一个条形样式的图表;
    column:创建一个柱形样式的图表;
    line:创建一个线条样式的图表
    pie:创建一个饼图样式的图表
    scatter:创建一个散点样式的图表
    stock:创建一个股票样式的图表;
    radar:创建一个雷达央视的图表'''

    worksheet2 = workbook.add_worksheet('test_chart')

    chart = workbook.add_chart({'type': 'column'}) # 默认格式,创建一个column图表
    data = [[1, 2, 3, 4, 5],[2, 4, 6, 8, 10],[3, 6, 9, 12, 15]]

    worksheet2.write_column('A1', data[0])  # 按列插入
    worksheet2.write_column('B1', data[1])
    worksheet2.write_column('C1', data[2])

    chart.add_series({'values': '=test_chart!$A$1:$A$5'})
    chart.add_series({'values': '=test_chart!$B$1:$B$5'})
    chart.add_series({'values': '=test_chart!$C$1:$C$5'})

    worksheet2.insert_chart('A7', chart)#通过insert_chart()方法将图表插入到指定的位置

write_loop_format()
write_loop_chart()

workbook.close()#关闭文件