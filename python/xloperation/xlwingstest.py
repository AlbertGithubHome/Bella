# -*- coding: utf-8 -*-
import xlwings as xw
# 设置程序不可见运行
app = xw.App(visible=False, add_book=False)

# ===============  第一部分,创建并写入数据 =====================
# 创建一个test2.xlsx表，并写入数据
# wb = app.books.add()
# ws = wb.sheets.active
# arr = []
# for col in range(1,4):
#     arr_temp = []
#     for row in range(1,4):
#         arr_temp.append(col*10+row)
#     arr.append(arr_temp)
# ws.range('A1:B3').value=arr
# wb.save('data/test2.xlsx')
# wb.close()
# app.quit()
# exit()

# ============== 第二部分，插入、删除行和列 ========================

# 导入已存的demo表格
load_wb = app.books.open('origin_excel.xlsx')
# # 打开活动的工作薄的活动工作簿，或者指定的工作簿
load_ws = load_wb.sheets.active
# load_ws = load_wb.sheets['Sheet']

# 获取总行数（存在数据）
rows = load_ws.api.UsedRange.Rows.count
cols = load_ws.api.UsedRange.Columns.count
# print('该表格总共有：'+str(rows)+' 行')
# print('该表格总共有：'+str(cols)+' 列')
# exit()


# 1-①在第二行前插入2行(可理解为: 在第2-4行插入空白行)
load_ws.api.rows('2:4').insert
# 1-②删除第2-4行
# load_ws.api.rows('2:4').delete
# 2-①在第二列前插入2列（这里处理的不是很好，其实是增加了对应区域的单元格，并未直接增加列）
# load_ws.range('B1:C'+str(cols)).api.insert
# 2-②删除第2-4列
# load_ws.range('B1:C'+str(cols)).api.delete

# ============== 第三部分，修改指定单元格的值 ========================
# load_ws.range('A1').value = 'x11'

# ============== 第四部分，合并单元格 ========================
# load_ws.range('A1:A2').api.merge

# ============== 第五部分，获取单元格横纵坐标index ========================
rng=xw.Range('B2')
# 返回当前格子的行值
print(rng.row)
# 返回当前格子的列值
print(rng.column)
# 返回和设置当前格子的高度和宽度
print(rng.width)
print(rng.height)
rng.row_height=40
rng.column_width=50
# 指定单元格的高度和宽度自适应
# rng.columns.autofit()
rng.rows.autofit()
print(rng.width)
print(rng.height)
# load_ws.range('A1:A2').api.height = 20


# ============== 第六部分，其它 ========================
# lst=load_ws.range('A1:A'+str(load_ws['A1048576'].end('up').row)).value #把excel单列值读取到列表中
# lst1=load_ws.range('A1:C'+str(load_ws['A1048576'].end('up').row)).value # 把excel连续两个列的值读取到列表中
# lst=load_ws.range('A1:A'+str(load_ws['A1048576'].end('up').row)).value #A列的值
# lst2=load_ws.range('C1:C'+str(load_ws['A1048576'].end('up').row)).value#C列的值
# lst3=list(zip(lst,lst2))#合并起来然后转为列表
# dicta=dict(lst3)#列表转为字典

# ============== 第七部分，Office操作文档 ========================
# https://docs.microsoft.com/en-us/office/vba/api/excel.range(object)



#load_wb.save()
load_wb.save('sample.xlsx')
load_wb.close()
app.quit()

if __name__ == '__main__':
    pass#rw()