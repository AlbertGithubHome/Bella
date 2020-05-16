#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Date     : 2020-5-16 12:40:09
# @Author   : Albert Shi
# @Link     : http://blog.csdn.net/albertsh
# @Github   : https://github.com/AlbertGithubHome
__author__ = 'AlbertS'
# @Subject  : 使用基准表替换目标表格的数据

# 注意：1. xlwings最好用来操作 .xlsx 格式的文件
#       2. 使用标准表格的表头更新目标表格的表头
#       3. 采用列对列的方式更新，在标准表格中不存在的列，在目标表格中用TRUE补齐

import os
import sys
import datetime
import xlwings as xw
from datetime import datetime

# 遍历指定目录下所有xlsx文件
def get_xlsx_list(path):
    result_list = []
    for root_path, dir_name_list, file_namelist in os.walk(path):
        for file_name in file_namelist:
            if '.xlsx' in file_name and '$' not in file_name: # 找到xlsx文件，并排除打开的临时文件
                result_list.append(os.path.join(root_path, file_name))
    return result_list;

# 获得要处理的目录，从控制台参数获取
def get_target_directory():
    return "" if len(sys.argv) < 2 else sys.argv[1]

# Excel处理工具类
class ExcelTool(object):
    def __init__(self, app):
        self.app = app
        self.base_col_set = {}       # {"sheetname1" : set(), "sheetname2" : set()}
        self.base_row_data_dict = {} # {"sheetname1" : {"colname1" : ["value1"], "colname2" : ["value2"]}}
        self.base_rows_cols = {}     # {"sheetname1" : (10,11), "sheetname2" : (10,13)}
        self.error_list = []

    # 日志记录
    def write_log(self, msg, append_error=False):
        print(msg)

        with open('./log/'+self.datetime_str+'.log', 'a', encoding='UTF-8') as file:
            file.write(msg+'\n')

        if append_error:
            self.error_list.append(msg)

    # 输出ErrorList
    def list_error(self):
        if self.error_list:
            self.write_log("\n\n完整错误列表如下：\n")
        else:
            self.write_log("\n\n执行完成未发现错误\(^o^)/~\n")

        for msg in self.error_list:
            self.write_log(msg)

    '''
    初始化行数
    base_dir：存放基准表的目录
    xlsx_list：需要修改的xlsx表
    check_row：检查第几行的表头，如果不匹配则插入
    check_str：检查单元格的内容
    add_rows：插入的行数
    add_rows_name：增加行的第一列的名称
    force_insert：当需要插入行，但是找不到基准表的时候是否强制插入默认两行
    '''
    def init_auto_replace_params(self, base_dir, xlsx_list, force_insert=False, check_row=8, check_str="Desc", add_rows=2, add_rows_name=['Server', 'Client']):
        self.base_dir = base_dir
        self.target_xlsx_list = xlsx_list
        self.check_row = check_row
        self.check_str = check_str
        self.add_rows = add_rows
        self.add_rows_name = add_rows_name
        self.force_insert = force_insert # 当需要插入行，但是找不到基准表的时候是否强制插入默认两行
        self.datetime_str = datetime.strftime(datetime.now(),'%Y-%m-%d %H%M%S')

    def collect_base_data(self, file_name):
        base_file_name = os.path.join(self.base_dir, file_name)
        base_file_exist = os.path.exists(base_file_name)
        contains_valid_data = False

        # 统计Base表数据
        if base_file_exist:
            load_wb = self.app.books.open(base_file_name)
            for load_ws in load_wb.sheets:
                if 'property' not in load_ws.name.lower():
                    continue;

                rows = load_ws.api.UsedRange.Rows.count
                cols = load_ws.api.UsedRange.Columns.count
                self.base_rows_cols[load_ws.name] = (rows, cols)

                if rows <= self.check_row + self.add_rows or cols <= 0:
                    continue;

                is_skip = False
                for row in range(self.add_rows):
                    cell_data = load_ws[self.check_row + row,0].value
                    if not cell_data or cell_data != self.add_rows_name[row]:
                        is_skip = True;

                if is_skip: # 不包含给目标表格增加的行
                    continue;

                # 统计列名和指定行数据
                cols_set = set()
                data_dict = {}
                for col in range(cols):
                    col_name = load_ws[0,col].value;
                    if not col_name or "" == col_name:
                        break;

                    cols_set.add(col_name)
                    value_list = []
                    for row in range(self.add_rows):
                        cell_data = load_ws[self.check_row + row,col].value
                        value_list.append(cell_data)
                    data_dict[col_name] = value_list

                self.base_col_set[load_ws.name] = cols_set
                self.base_row_data_dict[load_ws.name] = data_dict
                contains_valid_data = True
            load_wb.close()

        return base_file_exist, contains_valid_data

    def single_xlsx_handle(self, full_file_name):

        file_path, file_name = os.path.split(full_file_name)
        load_wb = self.app.books.open(full_file_name)
        for load_ws in load_wb.sheets:
            if 'property' not in load_ws.name.lower():
                continue;

            # 取基础表数据
            base_col_set = self.base_col_set.get(load_ws.name)
            base_row_data_dict = self.base_row_data_dict.get(load_ws.name)
            base_rows_cols = self.base_rows_cols.get(load_ws.name)
            # print(load_ws.name)
            # print(base_col_set)
            # print(base_row_data_dict)
            # print(base_rows_cols)

            if not base_col_set or not base_row_data_dict or not base_rows_cols:
                msg = "{0} 基准表格的 [{1}] 页签结构不完整，无法更新目标表格".format(file_name, load_ws.name)
                self.write_log(msg, True)
                continue;

            rows = load_ws.api.UsedRange.Rows.count
            cols = load_ws.api.UsedRange.Columns.count
            msg = "{0} 两个表格的 [{1}] 页签行列数据 Base({2}, {3}), Target({4}, {5}), Diff[target->base]({6}, {7})".format(file_name, load_ws.name,
                base_rows_cols[0], base_rows_cols[1], rows, cols, base_rows_cols[0] - rows, base_rows_cols[1] - cols)
            self.write_log(msg)

            if rows <= self.check_row or cols <= 0:
                msg = "{0} 目标表格的 [{1}] 页签结构不完整，无法进行更新".format(file_name, load_ws.name)
                self.write_log(msg, True)
                continue;

            # 检查是否要插入新行
            check_data = load_ws[self.check_row,0].value
            if load_ws[self.check_row,0].value and load_ws[self.check_row,0].value.lower() == self.check_str.lower():
                # 需要加行
                for col in range(self.add_rows):
                    load_ws.api.rows('{0}:{0}'.format(self.check_row+1)).insert

                msg = "{0} 目标表格的 [{1}] 页签，增加了 [{2}] 行表头".format(file_name, load_ws.name, self.add_rows)
                self.write_log(msg)

            elif not load_ws[self.check_row,0].value or load_ws[self.check_row,0].value != self.add_rows_name[0] or\
                not load_ws[self.check_row+1,0].value or load_ws[self.check_row+1,0].value != self.add_rows_name[1]:
                msg = "{0} 目标表格的 [{1}] 页签不需要加行，但表头格式不标准，无法进行更新".format(file_name, load_ws.name)
                self.write_log(msg, True)
                continue;

            else:
                msg = "{0} 目标表格的 [{1}] 页签不需要增加新行，只更新表头指定 [{2}] 行".format(file_name, load_ws.name, self.add_rows)
                self.write_log(msg)

            # 开始更新数据
            target_col_set = set()
            for col in range(cols):
                col_name = load_ws[0,col].value;
                if not col_name or "" == col_name:
                    break;

                target_col_set.add(col_name)
                # 处理在基准表中不包含的列
                base_data = base_row_data_dict.get(col_name)
                if not base_data:
                    msg = "{0} 基准表格的 [{1}] 页签不包含 {2} 列，在目标表格中使用TRUE补充".format(file_name, load_ws.name, col_name)
                    self.write_log(msg)
                    base_data = ["TRUE" for x in range(self.add_rows)]

                for row in range(self.add_rows):
                    load_ws[self.check_row + row,col].value = base_data[row]

            # print(target_col_set)
            # print(base_col_set)
            B_TSet = base_col_set.difference(target_col_set) # 增加的列
            T_BSet = target_col_set.difference(base_col_set) # 删除的列
            if B_TSet:
                msg = "{0} 目标表格到基准表格 [增加] 列：{1} =====> 无需处理，有时间可以检查一下 <=====".format(file_name, ','.join(list(B_TSet)))
                self.write_log(msg, True)
            if T_BSet:
                msg = "{0} 目标表格到基准表格 [删除] 列：{1} =====> 自动处理，有时间可以检查一下 <=====".format(file_name, ','.join(list(T_BSet)))
                self.write_log(msg, True)


        load_wb.save(full_file_name)
        load_wb.close()

    def main_auto_replace(self):
        for full_file_name in self.target_xlsx_list:
            file_path, file_name = os.path.split(full_file_name)
            self.write_log("\n{0} to be processed ...".format(file_name))

            try:
                exist_file, valid_data = self.collect_base_data(file_name)
                if not exist_file:
                    msg = "{0} 基准表格需要作为修改目标表格的依据，但它不存在".format(os.path.join(self.base_dir, file_name))
                    self.write_log(msg, True)
                    continue;
                if not valid_data:
                    msg = "{0} 基准表格需要作为修改目标表格的依据，但它表头不正确".format(os.path.join(self.base_dir, file_name))
                    self.write_log(msg, True)
                    continue;
            except Exception as e:
                raise e;
                self.write_log("{0} 基准表统计时打开失败， {1}".format(file_name, str(e)))
                return;

            try:
                self.single_xlsx_handle(full_file_name)
            except Exception as e:
                raise e;
                self.write_log("{0} 目标表修改时打开失败， {1}".format(file_name, str(e)))
                return;

def auto_replace_row_data_by_col():
    target_dir = get_target_directory()
    if '' == target_dir:
        print("输入的目录无效")
        return

    print("\n需要更新的目录为 {0}".format(target_dir))
    xlsx_list = get_xlsx_list(target_dir)
    if not xlsx_list:
        print("输入的目录不包含xlsx文件")
        return

    # 设置Excel程序不可见
    app = xw.App(visible=False, add_book=False)

    # 创建工具实例
    tool = ExcelTool(app)

    # 初始化参数
    tool.init_auto_replace_params('BaseExcel', xlsx_list, False)
    # 启动处理程序
    tool.main_auto_replace()
    # 列举遇到的错误
    tool.list_error()

    app.quit()


if __name__ == '__main__':
    auto_replace_row_data_by_col();