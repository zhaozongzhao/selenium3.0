from openpyxl import load_workbook,Workbook
from openpyxl.styles import Border,Side,Font
import time
from PageJectVar.var import  *


class parseExcel(object):

    def __init__(self,excelpath):
        self.excelpath = excelpath
        self.wordbppk = load_workbook(excelpath)  #加载excel
        self.sheet =  self.wordbppk.active #获取第一个sheet
        self.font = Font(color=None)
        self.colorDict = {'red','FFFF3030','green','FF008b00'}

    #设置当前操作的sheet对象,通过指数index,指定sheet
    def set_sheet_by_index(self,sheet_ineex):
        sheet_name =  self.wordbppk.sheetnames
        self.sheet =  self.wordbppk[sheet_name]
        return self.sheet

    #获取sheet名称
    def get_sheet_name(self):
        return self.sheet.title

    #设置当前要操作的sheet对象,使用sheet名称获取相应的sheet

    def set_sheet_by_name(self,sheet_name):
        self.sheet  =  self.wordbppk[sheet_name]
        return self.sheet

    #获取默认sheet最大行数
    def get_sheet_max_row(self):
        return self.sheet.max_row

    #获取默认最大列
    def get_sheet_max_column(self):
        return self.sheet.max_column

    #获取sheet默认最小起始行号
    def get_min_row_no(self):
        return self.sheet.min_row

    #获取sheet默认最小起始列好
    def get_min_column_no(self):
        return self.sheet.min_column

    #获取sheet所有行对象
    def get_all_rows(self):
        return list(self.sheet.iter_rows())

    #获取sheet所有列对象
    def get_all_col(self,col_no):
        return self.get_all_cols()[col_no]

    


