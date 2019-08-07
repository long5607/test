# -*- coding: utf-8 -*-
# @Time    : 2018/9/20 15:26
# @Author  : Guo
# @Email   : 314171455@qq.com
# @File    : operateExcel.py
# @Software: PyCharm

import xlrd


class ExcelUtil:
    # def __init__(self, excel_path, sheet_name):
    def __init__(self, excel_path,sheet_id=0):
        self.data = xlrd.open_workbook(excel_path)
        # 这个可以根据传入进来的sheet表名字来获取
        # self.table = self.data.sheet_by_name(sheet_name)
        # 直接获取第一个sheet表
        self.table = self.data.sheets()[sheet_id]
        # 获取第一行作为key值
        self.keys = self.table.row_values(sheet_id)
        # 获取总行数
        self.rowNum = self.table.nrows
        # 获取总列数
        self.colNum = self.table.ncols
    def get_cell_value(self,i,j):
        value=self.table.cell_value(i,j)
        return value
    def get_line_values(self,i):
        values=self.table.row_values(i)
        return values
    def get_list_values(self, i):
        values = self.table.col_values(i)
        return values
    def dict_data(self):
        if self.rowNum <= 1:
            print("总行数小于1")
        else:
            r = []
            j = 1
            for i in range(self.rowNum - 1):
                s = {}
                # 从第二行取对应values值
                values = self.table.row_values(j)
                for x in range(self.colNum):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j += 1
            return r


if __name__ == "__main__":
    # excel文件路径
    filePath = "./img.xlsx"
    # sheet表名字传参
    # sheetName = "企业在线产品列表"
    # data = ExcelUtil(filePath, sheetName)
    data = ExcelUtil(filePath,0)
    # 打印最后信息
    print(data.get_cell_value(0,0))
    print(data.colNum,data.rowNum)
    print(data.get_line_values(1))




