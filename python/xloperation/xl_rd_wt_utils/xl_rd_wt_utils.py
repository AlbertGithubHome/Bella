#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2020-03-14 23:07:46
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : 使用 xlrd、xlwt、xlutils 库操作 Excel

# 注意：1. 这种方式最好用来操作 .xls 格式的文件
#       2. .xls 格式文件可以带有样式保存，但是操作 .xlsx 格式的文件不支持操作带有样式的表格
#       3. 保存为 .xlsx 格式的文件保存后常常出现格式错误无法打开的情况

import xlrd
import xlwt
import xlutils.copy

FILE_PATH_ROOT = '../data/'
FILE_PATH_A = 'sampleA.xlsx'
FILE_PATH_B = 'sampleB.xls'
FILE_PATH_M = 'sampleM.xlsm'

def copy_file(file_name, formatting):
    #rb打开该excel，formatting_info=True表示打开excel时并保存原有的格式
    rb = xlrd.open_workbook(FILE_PATH_ROOT + file_name, formatting_info=formatting)
    #创建一个可写入的副本
    wb = xlutils.copy.copy(rb)
    # 获得第一个sheet页签
    ws = wb.get_sheet(0)
    # 第一个单元格写入测试值
    ws.write(0, 0, 'test value')
    # 另存为一个新文件
    wb.save(file_name)

#本文重点，该函数中定义：对于没有任何修改的单元格，保持原有格式。
def setOutCell(outSheet, col, row, value):
    """ Change cell value without changing formatting. """
    def _getOutCell(outSheet, colIndex, rowIndex):
        """ HACK: Extract the internal xlwt cell representation. """
        row = outSheet._Worksheet__rows.get(rowIndex)
        if not row: return None

        cell = row._Row__cells.get(colIndex)
        return cell

    # HACK to retain cell style.
    previousCell = _getOutCell(outSheet, col, row)
    # END HACK, PART I

    outSheet.write(row, col, value)

    # HACK, PART II
    if previousCell:
        newCell = _getOutCell(outSheet, col, row)
        if newCell:
            newCell.xf_idx = previousCell.xf_idx

# #判断需要写入的行是哪一行
# for row in range(0,len(original_data)):
#     if original_data.iloc[row,0] == yestoday:
#         print('当前需要修改的行为：' + row)print('正在查询：注册人数……')
#         regist_white = execude_sql(sql1_1)
#         regist_nature = execude_sql(sql1_2)
#         regist_all = execude_sql(sql1_3)
# #写入excel数据
#         outSheet = wb.get_sheet(0)
#         setOutCell(outSheet,1,row,regist_white[0])
#         setOutCell(outSheet,2,row,regist_nature[0])
#         setOutCell(outSheet,3,row,regist_all[0])#保存excel

if __name__ == '__main__':
    copy_file(FILE_PATH_A, False)
    copy_file(FILE_PATH_B, True)
    copy_file(FILE_PATH_M, False)