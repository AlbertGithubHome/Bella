# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 10:29:35 2017
@author: Administrator
"""
import pandas as pd
import datetime
#使用前提导入以下两个库
import xlrd
import xlutils.copy

#用于SQL中限定时间
yestoday = datetime.date.today() - datetime.timedelta(days = 1)
yestoday = yestoday.strftime("%Y-%m-%d")
time_limit = str(yestoday) + ' 23:59:59'

#指定原始excel路径
filepath = './origin_excel.xlsx'

#使用pandas库传入该excel的数值仅仅是为了后续判断插入数据时应插入行是哪行
#original_data = pd.read_excel(filepath,encoding='utf-8')

#rb打开该excel，formatting_info=True表示打开excel时并保存原有的格式
rb = xlrd.open_workbook(filepath,formatting_info=False)
#创建一个可写入的副本
wb = xlutils.copy.copy(rb)

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
wb.save('output.xls')
print('finish')