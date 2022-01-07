# -*- coding: utf-8 -*-
"""

"""
"""
import xlrd


# 1. 打开excel
def get_excel_data(file_path, sheet_name):

    wb = xlrd.open_workbook(file_path, formatting_info=True)
    # 获取sheet名
    ws_name = wb.sheet_names()
    if sheet_name not in ws_name:
        print('不存在sheetName')
        return None
    ws = wb.sheet_by_name(sheet_name)
    # 读取单元格
    cell_data = ws.cell().value # 返回的是字符串，

    return cell_data


if __name__ == '__main__':
    get_excel_data()


