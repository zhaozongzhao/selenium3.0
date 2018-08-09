from configparser import ConfigParser

class ParsePageObjectRepository(object):

    def __init__(self,config_path):
        self.cf = ConfigParser()
        self.cf.read(config_path,encoding='UTF8')

    def getItemSection(self,sectionName):
        return  dict(self.cf.items(sectionName))

    def getOptionValue(self,sectionName,optionName):
        return self.cf.get(sectionName,optionName)

if __name__ == '__main__':
    pp = ParsePageObjectRepository('F:\gitstorehouse\selenium3.0\data_driven\Conf\/1.ini')
    print(pp.getItemSection('qqmail_login'))
    print(pp.getOptionValue('qqmail_addcontactspage','addcontacts_page.createcontactsbtn'))






