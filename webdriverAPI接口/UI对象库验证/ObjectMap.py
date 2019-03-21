from selenium.webdriver.support.ui import WebDriverWait
import configparser
import os

class objectmap(object):

    def __init__(self):
        #获取文件地址
        self.uiobjectpath =  os.path.dirname(os.path.abspath(__file__))+'\\UiobjectMap.ini'
        print(self.uiobjectpath)

    def getElementObjext(self,driver,websiteName,elementName):

        try:
            #创建一个实类
            cf = configparser.ConfigParser()
            cf.read(self.uiobjectpath)
            locatos = cf.get(websiteName,elementName).split('>')
            locatorMethod = locatos[0]
            locatorExpresson = locatos[1]
            element = WebDriverWait(driver,10).until(lambda x:x.find_element(locatorMethod,locatorExpresson))

        except Exception as e:
            raise e
        else:
            return element
