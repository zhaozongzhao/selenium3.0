from selenium import webdriver
import unittest
from time import sleep

class Timeout(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
    def tearDown(self):
        self.driver.close()

    #隐式等待表示在自动化实施过程中，为查找页面元素或执行命令设置一个最长等待时间，如果在 设置的最长时间范围内被找到元素
        # 或者命令被执行完毕，则进行下一步，否则继续等待直到设置的最长等等待时间截止

    def test_implictwait(self):
        #导入异常类
        from selenium.common.exceptions import NoSuchElementException,TimeoutException
        #导入堆栈类
        import traceback
        url = 'http://www.sogou.com'
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        try:
            searchBox = self.driver.find_element_by_id('query')
            searchBox.send_keys('光荣之路')
            click = self.driver.find_element_by_id('stb')
            click.click()
        except (NoSuchElementException,TimeoutException) as a:
            #打印异常堆栈信息
            traceback.print_exc()


    #显式等待
    def test_explicitwait(self):
        #导入堆栈类
        import traceback
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        #导入期望场景
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.common.exceptions import TimeoutException,NoSuchElementException

        url ='F:\gitstorehouse\selenium3.0\webdriverAPI接口\测试页面\显式等待验证.html'
        self.driver.get(url)

        try:
            wait =WebDriverWait(self.driver,10,0.2)
            wait.until(EC.title_is('你喜欢的苹果'))
            print('网页标题你喜欢的苹果')
            element = WebDriverWait(self.driver,10).until(lambda x:x.find_element_by_xpath('//input[@value="Display alert box"]'))
            element.click()
            #等待alert框出现
            alert = wait.until(EC.alert_is_present())
            print(alert.text)
            #确认警告消息
            alert.accept()
            peach = self.driver.find_element_by_id('peach')
            #判断复选框是能选中
            peachelement = wait.until(EC.element_to_be_selected(peach))
            print('下拉列表的选项‘桃子’目前处于选中状态')
            wait.until(EC.element_to_be_clickable((By.ID,'check')))
            print('复选框可见并且能被单选')
        except TimeoutException as e :
            print(traceback.print_exc())
        except NoSuchElementException as e:
            print(traceback.print_exc())
        except Exception as e:
            print(traceback.print_exc())

    #使用title属性识别和操作浏览器窗口
    def test_identifyPopUpWindomByTitle(self):
        #导入异常
        from selenium.common.exceptions import NoSuchWindowException,TimeoutException
        #导入期望场景
        from selenium.webdriver.support import expected_conditions as EC
        #导入BY类
        from selenium.webdriver.common.by import By
        from selenium.webdriver.support.ui import WebDriverWait
        import traceback
        import time
        url ='F:\gitstorehouse\selenium3.0\webdriverAPI接口\测试页面\使用title属性识别和操作新弹出的浏览器窗口.html'
        self.driver.get(url)
        WebDriverWait(self.driver,10,0.5).until(EC.element_to_be_clickable((By.LINK_TEXT,'搜索'))).click()
        #获取当去页面所有打开的句柄
        all_hamdles = self.driver.window_handles
        #打印当前浏览窗口个数
        print(self.driver.current_window_handle)
        print(len(all_hamdles))
        print(all_hamdles)
        if len(all_hamdles) >0:
            try:
                for windowHandle in all_hamdles:
                    #切换窗口
                    self.driver.switch_to.window(windowHandle)
                    WebDriverWait(self.driver,10,0.5).until(EC.title_is)
                    print(self.driver.title)
                    if self.driver.title == '搜狗®宠物天下 - 爱宠物,爱生活':
                        WebDriverWait(self.driver,10,0.5).until(lambda x:x.find_element_by_xpath('//*[@id="main"]/h1'))
            except NoSuchWindowException as e:
                 print(traceback(e))
            except TimeoutException as e:
                print(traceback(e))
            self.driver.switch_to.window(all_hamdles[0])
            print(self.driver.title)
            self.assertEqual(self.driver.title,'你喜欢的水果')

            # 使用title属性识别和操作浏览器窗口

    #使用页面内容识别和操作浏览器窗口
    def test_identifyPopUpWindomByPageSource(self):
            # 导入异常
            from selenium.common.exceptions import NoSuchWindowException, TimeoutException
            # 导入期望场景
            from selenium.webdriver.support import expected_conditions as EC
            # 导入BY类
            from selenium.webdriver.common.by import By
            from selenium.webdriver.support.ui import WebDriverWait
            import traceback
            import time
            url = 'F:\gitstorehouse\selenium3.0\webdriverAPI接口\测试页面\使用title属性识别和操作新弹出的浏览器窗口.html'
            self.driver.get(url)
            WebDriverWait(self.driver, 10, 0.5).until(EC.element_to_be_clickable((By.LINK_TEXT, '搜索'))).click()
            # 获取当去页面所有打开的句柄
            all_hamdles = self.driver.window_handles
            # 打印当前浏览窗口个数
            print(self.driver.current_window_handle)
            print(len(all_hamdles))
            print(all_hamdles)
            if len(all_hamdles) > 0:
                try:
                    for windowHandle in all_hamdles:
                        # 切换窗口
                        self.driver.switch_to.window(windowHandle)
                        pageSoure = self.driver.page_source
                        print(type(pageSoure))
                        if '搜狗' in pageSoure:
                            WebDriverWait(self.driver, 10, 0.5).until(
                                lambda x: x.find_element_by_xpath('//*[@id="main"]/h1'))
                except NoSuchWindowException as e:
                    print(traceback(e))
                except TimeoutException as e:
                    print(traceback(e))
                self.driver.switch_to.window(all_hamdles[0])
                print(self.driver.title)
                self.assertEqual(self.driver.title, '你喜欢的水果')

    #操作frame元素
    def test_HandleFrame(self):
        from selenium.webdriver.support import expected_conditions as EC
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.common.exceptions import TimeoutException
        from selenium.webdriver.common.by import By
        import traceback
        import time
        url='F:\gitstorehouse\selenium3.0\webdriverAPI接口\测试页面\\frameset.html'
        self.driver.get(url)
        #使用索引的方式进入frame
        time.sleep(5)
        self.driver.switch_to.frame(0)
        leftframetext = self.driver.find_element_by_xpath('/html/body/p')
        self.assertEqual(leftframetext.text,'这是左侧frame 页面的信息')
        self.driver.find_element(By.XPATH,'/html/body/input').click()
        try:
            alertwindow = WebDriverWait(self.driver,10,1).until(EC.alert_is_present())
            print(alertwindow.text)
            alertwindow.accept()
        except TimeoutException as e:
            print(traceback(e))
        self.driver.switch_to.default_content()
        #通过页面标签对象定位
        self.driver.switch_to.frame(self.driver.find_elements(By.TAG_NAME,'frame')[1])
        assert  '这是中间frame' in self.driver.page_source
        self.driver.find_element(By.TAG_NAME,'input').send_keys('中间')
        #返回最外层
        self.driver.switch_to.default_content()
        # 通过页面标签对象定位
        self.driver.switch_to.frame(self.driver.find_element(By.ID,'rightframe'))
        assert '这是右侧frame页面上的文字' in self.driver.page_source
        self.driver.switch_to.default_content()

    #使用frame中的源码操作frame
    def test_HandleFrameByPageSoure(self):
        url = 'F:\gitstorehouse\selenium3.0\webdriverAPI接口\测试页面\\frameset.html'
        self.driver.get(url)
        framelist = self.driver.find_elements_by_tag_name('frame')
        for frame in framelist:
            self.driver.switch_to.frame(frame)
            if '中间' in self.driver.page_source:
                p = self.driver.find_element_by_xpath('/html/body/p')
                self.assertEqual('这是中间frame',p.text)
                self.driver.switch_to.default_content()
                break
            else:
                self.driver.switch_to.default_content()

    #操作frame中的页面元素
    def test_HandleIFrame(self):
        url = 'F:\gitstorehouse\selenium3.0\webdriverAPI接口\测试页面\\frameset.html'
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        self.driver.switch_to.frame(0)
        assert '这是左侧frame 页面的信息' in self.driver.page_source

        self.driver.switch_to.frame(self.driver.find_element_by_xpath('//*[@id="showifram"]'))
        import time
        time.sleep(5)
        assert '这是iframe 页面上的文字' in self.driver.page_source

        self.driver.switch_to.default_content()
        assert 'framset页面' in self.driver.title

        self.driver.switch_to.frame(1)
        assert '这是中间frame' in self.driver.page_source

    #操作alert弹框
    def test_HandleAlert(self):
        from selenium.common.exceptions import NoAlertPresentException
        import time
        url = 'F:\gitstorehouse\selenium3.0\webdriverAPI接口\测试页面\javaScript的alert弹框.html'
        self.driver.get(url)
        button = self.driver.find_element_by_xpath('//*[@id="button"]')
        button.click()
        try:
            alert = self.driver.switch_to.alert
            time.sleep(2)
            self.assertEqual(alert.text,'这是一个alert弹出框')
            alert.accept()

        except NoAlertPresentException as e:
            self.fail('尝试操作alert框未被找到')
            print(e)


    def test_Handleconfirm(self):
        from selenium.common.exceptions import NoAlertPresentException
        import time
        url = 'F:\gitstorehouse\selenium3.0\webdriverAPI接口\测试页面\javaScript的alert弹框.html'
        self.driver.get(url)
        #通过id属性查找页面上的按钮元素
        button = self.driver.find_element_by_xpath('//*[@id="button1"]')
        #点击元素操作
        button.click()
        try:
            #较高的版本的selenium推荐使用driver.switch_to.alert方法代替
            alert = self.driver.switch_to.alert
            time.sleep(2)
            #使用alert.text属性获取confine框中的元素
            self.assertEqual(alert.text,'这是一个confirm弹出框')
            #alert.accept点击确定按钮
            alert.accept()
            # #alert.dismiss点击取消按钮
            # alert.dismiss()
        except NoAlertPresentException as e:
            self.fail('尝试操作alert框未被找到')
            print(e)


    #处理prompt弹出框
    def  test_handlePrompt(self):
        import time
        url = 'F:\gitstorehouse\selenium3.0\webdriverAPI接口\测试页面\javaScript的alert弹框.html'
        self.driver.get(url)
        eleement = self.driver.find_element_by_xpath('//*[@id="button2"]')
        eleement.click()
        time.sleep(2)
        alert = self.driver.switch_to.alert
        self.assertEqual(alert.text,'这是一个prompt弹出框')
        time.sleep(2)
        alert.send_keys(u"坚持学习，不放弃，不抛弃")
        time.sleep(5)
        # alert.accept()
        alert.dismiss()

    #操作浏览器cookie
    def test_Cookie(self):
        url = 'http://sogou.com'
        self.driver.get(url)
        #获取当前页面下所有的cookies数据
        cookies = self.driver.get_cookies()
        for cookie in cookies:
            print('domain :{}  ,name :{}, value:{},path{}'.format
                  (cookie['domain'],cookie['name'],cookie['value'],cookie['path']))
        print("#############################")
        #获取name值为suv的该条cookie
        ck = self.driver.get_cookie('SUV')
        print(ck)
        print("#############################")
        #删除部分cookie
        print(self.driver.delete_cookie('SUV'))
        print(cookies)
        print("#############################")
        cookies = self.driver.delete_all_cookies()
        print(cookies)
        print("#############################")
        self.driver.add_cookie({"name":"sssss",'value' : 'bar'})
        self.driver.add_cookie({"name": "ssssZZ", 'value': 'bar'})
        cookie = self.driver.get_cookie('ssssZZ')
        print(cookie)
        cookies = self.driver.get_cookies()
        for cookie in cookies:
            print('domain :{}  ,name :{}, value:{},path{}'.format
                  (cookie['domain'], cookie['name'], cookie['value'], cookie['path']))





