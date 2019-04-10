class Table(object):

    def __init__(self,Table):
        #构造table类
        self.setTable(Table)

    def setTable(self,table):
        #对私有属性__table进行赋值
        self.__table = table

    def getTable(self):
        #获取私有属性table的值
        return  self.__table

    def getRowCount(self):
        #返回table对象所有的行tr个数
        return len(self.__table.find_elements_by_tag_name('tr'))

    def getColumnCount(self):
        #返回table对象所有列的数
        return len(self.__table.find_elements_by_tag_name('tr')[0].find_elements_by_tag_name('td'))

    def getCell(self,rowNo,colNo):
        #获取表格内某行某列的单元格对象
        try:
            #表格的行号从0开始，所以输入行号减一
            #根据输入的行号定位所在的行对象
            currentRow = self.__table.find_elements_by_tag_name('tr')[rowNo-1]
            #在找到行的基础上，根据列号定位单元对象
            currentCol = currentRow.find_elements_by_tag_name('td')[colNo-1]
            return currentCol
        except Exception  as e:
            raise e

    def getWebElementInCell(self,rowNo,colNo,by,value):
        #获取表格内某行某列的单元格对象中某个元素的对象
        try:
            # 表格的行号从0开始，所以输入行号减一
            # 根据输入的行号定位所在的行对象
            currentRow = self.__table.find_elements_by_tag_name('tr')[rowNo - 1]
            # 在找到行的基础上，根据列号定位单元对象
            currentCol = currentRow.find_elements_by_tag_name('td')[colNo - 1]
            #获取某个单元格中元素的对象
            element = currentCol.find_element(by=by,value=value)
            return element
        except Exception as e:
            raise e
