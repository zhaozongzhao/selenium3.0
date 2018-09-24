from configparser import ConfigParser
from data_driven.PageJectVar.var import PaserPageObject_path


class ParsePageObjectRepository(object):

    def __init__(self):
        self.cf = ConfigParser() #生成解析器
        self.cf.read(PaserPageObject_path,encoding='UTF8') #直接用变量代替

    def getItemSection(self,sectionName):
        return  dict(self.cf.items(sectionName))

    def getOptionValue(self,sectionName,optionName):
        return self.cf.get(sectionName,optionName)

if __name__ == '__main__':
    pp = ParsePageObjectRepository()
    print(pp.getItemSection('qqmail_login'))
    print(pp.getOptionValue('qqmail_addcontactspage','addcontacts_page.createcontactsbtn'))






