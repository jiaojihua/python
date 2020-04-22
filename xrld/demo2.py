#coding:utf-8
import xlrd

""" 打开excel表格"""
workbook = xlrd.open_workbook("C:\\Users\Administrator\Desktop\支出.xls")
print(workbook)             # 结果：<xlrd.book.Book object at 0x000000000291B128>

""" 获取所有sheet名称"""
sheet_names = workbook.sheet_names()
print(sheet_names)          # 结果：['表1', 'Sheet2']

""" 获取所有或某个sheet对象"""
# 获取所有的sheet对象
sheets_object = workbook.sheets()
print(sheets_object)        # 结果：[<xlrd.sheet.Sheet object at 0x0000000002956710>, <xlrd.sheet.Sheet object at 0x0000000002956AC8>]
# 通过index获取第一个sheet对象
sheet1_object = workbook.sheet_by_index(0)
print(sheet1_object)        # 结果：<xlrd.sheet.Sheet object at 0x0000000002956710>
# 通过name获取第一个sheet对象
sheet1_object = workbook.sheet_by_name(sheet_name="导出数据")
print(sheet1_object)        # 结果：<xlrd.sheet.Sheet object at 0x0000000002956710>

""" 判断某个sheet是否已导入"""
# 通过index判断sheet1是否导入
sheet1_is_load = workbook.sheet_loaded(sheet_name_or_index=0)
print(sheet1_is_load)       # 结果：True
# 通过sheet名称判断sheet1是否导入
sheet1_is_load = workbook.sheet_loaded(sheet_name_or_index="导出数据")
print(sheet1_is_load)       # 结果：True

""" 对sheet对象中的行执行操作：如有效行数、某行从n1到n2列的数据、某行的单元和类型、某行的长度...... """
# 获取sheet1中的有效行数
nrows = sheet1_object.nrows
print(nrows)                # 结果：5
# 获取sheet1中第3行的数据
all_row_values = sheet1_object.row_values(rowx=2)
print(all_row_values)           # 结果：[3.0, 'b', 1, '']
row_values = sheet1_object.row_values(rowx=2, start_colx=1, end_colx=3)
print(row_values)               # 结果：['b', 1]
# 获取sheet1中第3行的单元对象
row_object = sheet1_object.row(rowx=2)
print(row_object)               # 结果：[number:3.0, text:'b', bool:1, empty:'']
# 获取sheet1中第3行的单元
row_slice = sheet1_object.row_slice(rowx=2)
print(row_slice)                # 结果：[number:3.0, text:'b', bool:1, empty:'']
# 获取sheet1中第3行的单元类型
row_types = sheet1_object.row_types(rowx=2)
print(row_types)                # 结果：array('B', [2, 1, 4, 0])
# 获取sheet1中第3行的长度
row_len = sheet1_object.row_len(rowx=2)
print(row_len)                  # 结果：4
# 获取sheet1所有行的生成器
rows_generator = sheet1_object.get_rows()
print(rows_generator)           # 结果：<generator object Sheet.get_rows.<locals>.<genexpr> at 0x00000000028D8BA0>

""" 对sheet对象中的列执行操作："""
# 获取sheet1中的有效列数
ncols = sheet1_object.ncols
print(ncols)                # 结果：4
# 获取sheet1中第colx+1列的数据
col_values = sheet1_object.col_values(colx=1)
print(col_values)           # 结果：['测试', 'a', 'b', 'c', 'd']
col_values1 = sheet1_object.col_values(1, 1, 3)
print(col_values1)          # 结果：['a', 'b']
# 获取sheet1中第2列的单元
col_slice = sheet1_object.col_slice(colx=1)
print(col_slice)            # 结果：[text:'测试', text:'a', text:'b', text:'c', text:'d']
# 获取sheet1中第2列的单元类型
col_types = sheet1_object.col_types(colx=1)
print(col_types)            # 结果：[1, 1, 1, 1, 1]

"""对sheet对象中的单元执行操作"""
# 获取sheet1中第rowx+1行，第colx+1列的单元对象
cell_info = sheet1_object.cell(rowx=1, colx=2)
print(cell_info)           # 结果: text:'m'
print(type(cell_info))     # 结果：<class 'xlrd.sheet.Cell'>
# 获取sheet1中第rowx+1行，第colx+1列的单元值
cell_value = sheet1_object.cell_value(rowx=1, colx=2)
print(cell_value)           # 结果: m
# 获取sheet1中第rowx+1行，第colx+1列的单元类型值
cell_type = sheet1_object.cell_type(rowx=1, colx=2)
print(cell_type)            # 结果：1