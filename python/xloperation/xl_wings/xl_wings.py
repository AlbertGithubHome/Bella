#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2020-3-15 08:55:51
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : 使用 xlwigns 库操作 Excel

# 注意：1. 这种方式最好用来操作 .xlsx 格式的文件
#       2. .xls 格式文件无法打开，但是可以保存，新建保存后会提示格式错误，但可以看到基础数据
#       3. 处理不了带有宏的表格，强行存储为 .xlsx 格式化后宏会全部丢失

import xlwings as xw

FILE_PATH_ROOT = '../data/'
FILE_PATH_A = 'sampleA.xlsx'
FILE_PATH_B = 'sampleB.xls'
FILE_PATH_C = 'sampleC.xlsx'
FILE_PATH_D = 'sampleD.xls'
FILE_PATH_M = 'sampleM.xlsm'
FILE_PATH_Z = 'sampleZ.xlsx'

def test():
    pass
    # ============== 第六部分，其它 ========================
    # lst=load_ws.range('A1:A'+str(load_ws['A1048576'].end('up').row)).value #把excel单列值读取到列表中
    # lst1=load_ws.range('A1:C'+str(load_ws['A1048576'].end('up').row)).value # 把excel连续两个列的值读取到列表中
    # lst=load_ws.range('A1:A'+str(load_ws['A1048576'].end('up').row)).value #A列的值
    # lst2=load_ws.range('C1:C'+str(load_ws['A1048576'].end('up').row)).value#C列的值
    # lst3=list(zip(lst,lst2))#合并起来然后转为列表
    # dicta=dict(lst3)#列表转为字典

def write_new_excel(app, file_name):
    # 创建新的 Excel 表
    wb = app.books.add()
    # 获取当前活动的sheet
    ws = wb.sheets.active
    # 初始化二维区域的值
    arr_data = [[1, 2, 3], [4, 5, 6], [7, 8, 'end']]
    # 设置到新建的Excel中
    ws.range('A1:B3').value=arr_data
    # 设置单独一个单元格的值
    ws.range('A4').value='this is A4'
    # 设置单独一个单元格的值
    ws[3,1].value='this is B4'
    # 保存Excel文件
    wb.save(file_name)
    wb.close()


def read_update_excel(app, file_name):
    # 加载已有的表格
    load_wb = app.books.open(FILE_PATH_ROOT + file_name)
    # 获取Excel表中第一个sheet
    load_ws = load_wb.sheets[0]
    # 打印sheet的名字
    print(load_ws.name)
    # 根据sheet名字获取sheet对象
    load_ws = load_wb.sheets[load_ws.name]
    # 获取当前活动的sheet
    load_ws = load_wb.sheets.active

    # 获取存在数据的行数和列数
    rows = load_ws.api.UsedRange.Rows.count
    cols = load_ws.api.UsedRange.Columns.count
    print('rows count:', rows, 'cols count:', cols)

    # 修改指定单元格数据（A1单元格）
    load_ws[0,0].value='this is A1'

    # 有空行或空列时获取准确的行列数量
    print(load_ws.used_range.shape)

    # 从A1单元格开始扩展到非空行空列，最后的行数和列数
    print((load_ws.range('A1').expand().last_cell.row,
        load_ws.range('A1').expand().last_cell.column))

    # 从A1单元格开始扩展到非空行空列，最后的行数和列数
    print((load_ws.range('A1').expand().last_cell.row,
        load_ws.range('A1').expand().last_cell.column))

    # 从A1单元格开始扩展到非空行空列，最后形状
    print(load_ws.range(1,1).expand().shape)

    # 从A1单元格开始扩展到非空行空列，最后的行数和列数
    print((load_ws.range('A1').expand('table').rows.count,
        load_ws.range('A1').expand('table').columns.count))

    # 保存修改后的Excel
    load_wb.save(file_name)
    load_wb.close()


def insert_delete_rowscols(app, file_name):
    # 加载已有的表格
    load_wb = app.books.open(FILE_PATH_ROOT + file_name)
    # 获取当前活动的sheet
    load_ws = load_wb.sheets.active

    # 从第2行开始插入4行，也就是说2-5行变成新插入的空行
    load_ws.api.rows('2:5').insert
    # 删除第6行和第7行
    load_ws.api.rows('6:7').delete
    # 插入一个单元格，实际测试效果是B列从B2开始向下移动，B2为新添加的单元格
    load_ws.range('B2').api.insert
    # 插入新的一列
    load_ws.api.columns('B').insert
    # 删除一列
    load_ws.api.columns('C').delete

    # 保存修改后的Excel
    load_wb.save(file_name)
    load_wb.close()

def cell_operation(app, file_name):
    # 加载已有的表格
    load_wb = app.books.open(FILE_PATH_ROOT + file_name)
    # 获取当前活动的sheet
    load_ws = load_wb.sheets.active

    # 合并单元格
    load_ws.range('A2:A3').api.merge

    #获取单元格
    cell = xw.Range('B2')
    # 打印单元格所在的行和列
    print("row is:", cell.row, "col is:", cell.column)

    # 打印当前格子的高度和宽度
    print("cell.width:", cell.width, "cell.height:", cell.height)

    # 设置当前格子的高度和宽度
    cell.row_height = 32
    cell.column_width = 64

    # 指定单元格的高度和宽度自适应
    cell.columns.autofit()
    cell.rows.autofit()

    # 再次打印当前格子的高度和宽度
    print("cell.width:", cell.width, "cell.height:", cell.height)

    # 保存修改后的Excel
    load_wb.save(file_name)
    load_wb.close()


if __name__ == '__main__':
    # 设置Excel程序不可见
    app = xw.App(visible=False, add_book=False)

    # write_new_excel(app, FILE_PATH_C)
    # write_new_excel(app, FILE_PATH_D)

    # read_update_excel(app, FILE_PATH_A)
    # read_update_excel(app, FILE_PATH_B)
    # read_update_excel(app, FILE_PATH_M)
    read_update_excel(app, FILE_PATH_Z)

    # insert_delete_rowscols(app, FILE_PATH_A)

    # cell_operation(app, FILE_PATH_A)

    app.quit()