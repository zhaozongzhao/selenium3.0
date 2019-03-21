
from selenium import webdriver
from selenium.common.exceptions import WebDriverException,TimeoutException,NoSuchElementException
import unittest,traceback,time,os
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# 更改页面对象的额属性
def addAttribute(driver, elementobj, attributeName, value):
    #封装向页面标签中添加新属性的方法
    #调用javascript 代码给页面标签添加属性，arguments[0].%s=arguments[1]分别会用后面的element，attributeName
    #和value参数进行替换
    #添加属性 javascript 语法 ；element.attributeName = value
    #例如 input.name = 'test'
    driver.execute_script("arguments[0].%s=arguments[1]" %attributeName, elementobj, value)

def setAttribute(driver, elementobj, attributeName, value):
    #封装设置页面对象的属性值得方法
    #调用javascript代码修改页面元素的属性值 arguments[0]~arguments[2] 分别会用后面的element，attributeName
    #和value参数进行替换
    driver.execute_script("arguments[0].setAttribute(arguments[1],arguments[2])",elementobj, attributeName, value)


def get_arribute( elementobj, value):
    #封装获取页面属性值得方法
    return elementobj.get_attribute(value)


def removeAttribute(driver, elementobj, attributeName):
    #封装删除页面元素的属性的方法
    #调用javascript 删除页面元素的指定属性 arguments[0]~arguments[2] 分别会用后面的element，attributeName
    #参数进行替换
    driver.execute_script("arguments[0].removeAttribute(arguments[1])",elementobj,attributeName)

class TestDemo(unittest.TestCase):

    def setUp(self):
        print('启动chrome')
        self.driver = webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    # 在webDriver脚本代码执行JavaScript代码，来实现对页面元素的操作，此时方式主要用于解决某些情况下与页面元素的click（）方法
    # 无法等问题
    def test_executeScript(self):
        url = 'http://www.baidu.com'
        self.driver.get(url)

        searfchInputBoxjs = 'document.getElementByid("kw").value=“光荣之路”'
        searfchButtonjs = 'document.getElementByid("su").click()'

        try:
            self.driver.execute_script(searfchInputBoxjs)
            time.sleep(2)
            self.driver.execute_script(searfchButtonjs)
            time.sleep(2)
            self.assertEqual('百度百科' in self.driver.page_source)
        except WebDriverException as e:
            print('没有找到元素')
        except AssertionError as e:
             print('页面不存在断言的关键字')
        except Exception as e:
            print(traceback.print_exc())

    #使用JavaScript代码实现下拉框操作
    def test_scroll(self):
        url = 'http://www.docin.com/p-1331019547.html'
        #访问selenium官网首页
        try:
            self.driver.get(url)
            #使用javascript的scroll函数和document.body.scrollHeihgt参数
            #将页面滑动(左右滚动)
            self.driver.execute_script('window.scrollTo(100,document.body.scrollHeihgt);')
            time.sleep(5)

            #使用javascript的scrollIntoView函数将被遮挡的元素滚动的元素到可见屏幕上
            # 表示将元素滚动到屏幕底部
            self.driver.execute_script('document.documentElement.scrollTop=10000;')
            time.sleep(5)
            # 表示将元素滚动屏幕顶部
            self.driver.execute_script('document.documentElement.scrollTop=0;')
            time.sleep(3)

            #使用javascript的scrollby方法，使用呢0和400横纵坐标参数
            #将页面向下0400元素
            self.driver.execute_script('window.scrollBy(100,400)')
            time.sleep(3)

        except Exception as e:
            print(traceback.print_exc())


    #操作ajax方式产生的浮动框，单击选择包含某个关键字的选项
    #方式1通过键盘操作
    def test_AjaxDivoptionByKeys(self):
        url = 'http://sogou.com/'
        self.driver.get(url)
        searbox = self.driver.find_element(By.ID,'query')
        searbox.send_keys('光荣之路')
        time.sleep(2)
        for i in range(3):
            searbox.send_keys(Keys.DOWN)
            time.sleep(3)
        searbox.send_keys(Keys.ENTER)
        time.sleep(3)

    #方法2模糊查询
    def test_AjaxDivoptionBywords(self):
        url = 'http://sogou.com/'
        self.driver.get(url)
        try:
            searbox = self.driver.find_element(By.ID, 'query')
            searbox.send_keys('光荣之路')
            time.sleep(2)
            sugettion_option = self.driver.find_element_by_xpath("//ul/li[contains(.,'电影')]")
            sugettion_option.click()
            time.sleep(3)
        except Exception as e:
            print(traceback.print_exc())

    #方法，按照顺序定位
    def test_AjaxDivoptionByIndex(self):
        url = 'http://sogou.com/'
        self.driver.get(url)
        try:
            searbox = self.driver.find_element(By.ID, 'query')
            searbox.send_keys('光荣之路')
            time.sleep(2)
            sugettion_option = self.driver.find_element_by_xpath("//*[@id='vl']/div[1]/ul/li[4]")
            sugettion_option.click()
            time.sleep(3)
        except Exception as e:
            print(traceback.print_exc())

    #结束window中浏览器的进程
    def test_killWindowProcess(self):
        import os
        returncode = os.system("taskkill /F /iM chrome.exe")
        if returncode== 0 :
            print('结束浏览器')
        else:
            print('结束失败')


    #对页面元素的增加，修改，删除都是临时的，当前会话结束后失效
    def test_dataPicker(self):
        url = 'F:\gitstorehouse\selenium3.0\webdriverAPI接口\测试页面\更改一个页面对象的属性值.html'
        self.driver.get(url)
        #定位元素位置
        element = self.driver.find_element_by_xpath('//*[@id="text"]')
       #向文本框中的input标签添加新元素name = ‘sratch"’
        addAttribute(self.driver,element,'name',"sratch")
        print(get_arribute(element,'name'))

        #查看修改前input 元素中value的属性值
        print(get_arribute(element,'value'))
        #更改元素value的属性值
        setAttribute(self.driver,element,'value','修改后的文字内容')
        #查看修改后的顺序属性值
        print(get_arribute(element, 'value'))

        # 查看修改前input 元素中size的属性值
        print(get_arribute(element, 'size'))
        # 更改元素value的属性值
        setAttribute(self.driver, element, 'size', '20')
        time.sleep(2)
        # 查看修改后的顺序属性值
        print(get_arribute(element, 'size'))


        #查看删除input页面元素value属性value属性值
        print(get_arribute(element,'value'))
        #删除文本框value的值
        removeAttribute(self.driver,element,'value')
        #删除后查看属性value的值
        print('删除后的属性值',get_arribute(element,'value'))

    #无人工干预下自动下载某个文件

    # def test_dataPicker(self):
    #      url = "www.baidu.com"
    #      self.driver  = webdriver.Firefox()
    #      self.driver.get(url)


    #无人干预上传文件
    def test_uploadFileBySendKeys(self):
        url = 'F:\gitstorehouse\selenium3.0\webdriverAPI接口\测试页面\上传文件.html'
        self.driver.get(url)
        try:
            #创建一个显示等待
            wait = WebDriverWait(self.driver,5,0.5)
            #判断被测上传按钮是否处于克点击状态
            wait.until(EC.element_to_be_clickable((By.ID,'file')))
        except TimeoutException as e:
            traceback.print_exc()
        except NoSuchElementException as e:
            traceback.print_exc()
        except Exception as e:
            traceback.print_exc()
        else:
            fileb0x =  self.driver.find_element(By.XPATH,'//*[@id="file"]')
            #在文件上传框输入文件目录
            fileb0x.send_keys('F:\gitstorehouse\selenium3.0\webdriverAPI接口\测试页面\javaScript的alert弹框.html')
            time.sleep(4)
            #定位提交按钮，
            filesumbitButton = self.driver.find_element(By.ID,'filesubmit')
            #点击提交按钮完成文件上传操作
            filesumbitButton.click()

        #使用第三方Autoit 上传文件

    def test_uploadfileByAutoit(self):
        url = 'F:\gitstorehouse\selenium3.0\webdriverAPI接口\测试页面\上传文件.html'
        self.driver.get(url)
        try:
            # 创建一个显示等待
            wait = WebDriverWait(self.driver, 5, 0.5)
            # 判断被测上传按钮是否处于克点击状态
            wait.until(EC.element_to_be_clickable((By.ID, 'file')))
        except TimeoutException as e:
            traceback.print_exc()
        except NoSuchElementException as e:
            traceback.print_exc()
        except Exception as e:
            traceback.print_exc()
        else:
            fileb0x = self.driver.find_element(By.XPATH, '//*[@id="file"]')
            # 点击调出文件上传框
            fileb0x.click()
            #通过os模块执行system方法执行生成的test.exe文件
            os.system('D:\\test.exe')
            time.sleep(5)
            filesumbitButton = self.driver.find_element(By.ID, 'filesubmit')
            # 点击提交按钮完成文件上传操作
            filesumbitButton.click()





