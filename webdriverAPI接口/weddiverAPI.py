from selenium import webdriver
import unittest
from time import sleep

class visitBysou(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
    def tearDown(self):
        self.driver.close()

    #访问某个网址
    def test_visitURL(self):
        visitURL = 'http://www.sogou.com'
        self.driver.get(visitURL)
        assert self.driver.title.find('搜狗') >= 0,'assert error'

    #网页的前进与后退
    def test_visitRecenURL(self):
        firstVisitURL = 'http://www.sogou.com'
        secondVisitURl = 'http://www.baidu.com'
        self.driver.get(firstVisitURL)
        self.driver.get(secondVisitURl)
        self.driver.back()
        self.driver.forward()

    #刷新当前网页
    def test_refreshCurrentpage(self):
        URL = 'http://www.sogou.com'
        self.driver.get(URL)
        self.driver.refresh()


    #窗口放大
    def test_maxmizeWindow(self):
        URL = 'http://www.sogou.com'
        self.driver.get(URL)
        self.driver.maximize_window()

    #获取并设置当前窗口的位置
    def test_window_position(self):
        URL = 'http://www.sogou.com'
        self.driver.get(URL)
        position =  self.driver.get_window_position()
        print('##################################')
        print(position['x'],position['y'])
        print('##############################')
        self.driver.set_window_position(y=200,x=400)
        sleep(5)
        print(self.driver.get_window_position())

    #获取并设置当前窗口的大小
    def test_window_size(self):
        URL = 'http://www.sogou.com'
        self.driver.get(URL)
        sizeDict = self.driver.get_window_size()
        print('#############')
        print(sizeDict['width'],sizeDict['height'])
        #设置大小
        self.driver.set_window_size(width=200,height=400,windowHandle='current')
        print(self.driver.get_window_size())

    #获取打开当前页面的title值
    def test_getTitle(self):
        URL = 'http://www.sogou.com'
        self.driver.get(URL)
        title = self.driver.title
        print('当前页面的title属性是',title)
        self.assertEqual(title,'搜狗搜索引擎 - 上网从搜狗开始','页面显示错误')

    #获取当前页面的html源码
    def test_getPageSource(self):
        URL = 'http://www.sogou.com'
        self.driver.get(URL)
        pagesource = self.driver.page_source
        print(pagesource)
        self.assertTrue('搜狗' in pagesource,'页面显示错误')
        self.assertIn('搜狗',pagesource,'页面展示错误')

    #获取当前页面的url地址
    def test_getUrl(self):
        URL = 'http://www.sogou.com'
        self.driver.get(URL)
        Url = self.driver.current_url
        print(Url)
        self.assertEqual(Url,'https://www.sogou.com/','页面展示错误')



     #获取与切换浏览器句柄
    def test_operatewindowhandle(self):
        URL = 'https://www.baidu.com'
        self.driver.get(URL)
        #获取当前句柄
        now_handle = self.driver.current_window_handle
        print(now_handle)
        self.driver.find_element(by='xpath',value='//*[@id="kw"]').send_keys('w3cshool')
        self.driver.find_element_by_xpath('//*[@id="su"]').click()
        import time
        time.sleep(3)
        self.driver.find_element_by_xpath('//*[@id="1"]/h3/a').click()
        time.sleep(5)
        all_handle = self.driver.window_handles
        print(all_handle)
        print(all_handle[-1])
        for handle in all_handle:
            if handle != now_handle:
                print('########################')
                print(handle)
        self.driver.switch_to.window(now_handle)
        time.sleep(1)
        # self.driver.close()
        print(now_handle)
        self.driver.switch_to.window(all_handle[-1])
        time.sleep(1)

    #获取页面元素
    def test_getBasicinfo(self):
        URL = 'https://www.baidu.com'
        self.driver.get(URL)
        sleep(5)
        newelement = self.driver.find_element_by_partial_link_text('新闻')
        print(newelement.tag_name,newelement.size)

    #获取页面元素的文本内容
    def test_getwebElement(self):
        URL = 'https://www.baidu.com'
        self.driver.get(URL)
        sleep(4)

        newelement = self.driver.find_element_by_partial_link_text('新闻')
        a_test = newelement.text
        self.assertEqual(a_test,'新闻')

   #判断元素是否可以操作
    def test_getwebElementIsEnabled(self):
            URL = 'F:\gitstorehouse\selenium3.0\webdriverAPI接口\测试页面\不可见元素.html'
            self.driver.get(URL)
            sleep(4)
            input1 =  self.driver.find_element_by_id('input1')
            print(input1.is_enabled())
            input1 = self.driver.find_element_by_id('input2')
            print(input1.is_enabled())
            input1 = self.driver.find_element_by_id('input3')
            print(input1.is_enabled())

    #获取页面元素css属性值
    def test_getwebelementcssValue(self):
        URL = 'http://www.sogou.com'
        self.driver.get(URL)
        searchBox = self.driver.find_element_by_id('query')
        print(searchBox.value_of_css_property('height'))
        print(searchBox.value_of_css_property('width'))
        print(searchBox.value_of_css_property('font-family'))

    # 获取页面元素的属性
    def test_getwebelementAttribute(self):
        URL= 'http://www.sogou.com'
        self.driver.get(URL)
        searchBox = self.driver.find_element_by_id('query')
        print(searchBox.get_attribute('name'))
        searchBox.send_keys('测试输入')
        print(searchBox.get_attribute('value'))
        print(searchBox.get_property('name'))

    #双击某个元素
    def test_dobleclick(self):
        URL = 'F:\gitstorehouse\selenium3.0\webdriverAPI接口\测试页面\双击.html'
        self.driver.get(URL)
        inputbox = self.driver.find_element_by_id('input1')
        from selenium.webdriver import ActionChains
        action_chains = ActionChains(self.driver)
        action_chains.double_click(inputbox).perform()
        sleep(5)

    #遍历下拉框所有元素并打印选择项的文本和内容
    def test_printselectText(self):
        URL = 'F:\gitstorehouse\selenium3.0\webdriverAPI接口\测试页面\下拉框.html'
        self.driver.get(URL)
        select = self.driver.find_element_by_name('fruit')
        all_options = select.find_elements_by_tag_name('option')
        for option in all_options:
            print(option.text)
            #attribute 属性
            print(option.get_attribute('value'))
            option.click()
            sleep(3)

    #定位下拉框的三种方式
    def test_operateDropList(self):
        URL = 'F:\gitstorehouse\selenium3.0\webdriverAPI接口\测试页面\下拉框.html'
        self.driver.get(URL)
        from selenium.webdriver.support.ui import Select
        select_element = Select(self.driver.find_element_by_name('fruit'))
        #打印默认选择的文本
        print(select_element.first_selected_option.text)
        #获取所有的页面元素对象
        all_options = select_element.options
        print(len(all_options))
        '''
        is_enabled() 判断元素是否存在
        is_selected() 判断元素是否被选中
        '''
        if all_options[1].is_enabled() and not all_options[1].is_selected():
            #方法一：通过序号选择第二个元素，序号从零开始
            select_element.select_by_index(1)
            print(select_element.all_selected_options[0].text)
            print(type(select_element.all_selected_options))
            self.assertEqual(select_element.all_selected_options[0].text,'西瓜')
            sleep(3)
        #方法二通过显示文本定位
        select_element.select_by_visible_text('橘子')
        print(select_element.all_selected_options[0].text)
        self.assertEqual(select_element.all_selected_options[0].text,'橘子')
        #通过选项value值进行定位
        select_element.select_by_value('shanzha')
        print(select_element.all_selected_options[0].text)
        self.assertEqual(select_element.all_selected_options[0].text,'山楂')

    #对下拉框的所有内容进行验证
    def test_checkSelectText(self):
        URL = 'F:\gitstorehouse\selenium3.0\webdriverAPI接口\测试页面\下拉框.html'
        self.driver.get(URL)
        from selenium.webdriver.support.ui import Select
        #定位元素
        select_element = Select(self.driver.find_element_by_name('fruit'))
        #获取所有下拉元素
        all_options =  select_element.options
        element_list = ['桃子', '西瓜', '橘子', '山楂', '荔枝']
        print(type(element_list))
        actual_options = map(lambda options:options.text,all_options)
        print(type(actual_options))
        self.assertListEqual(element_list,list(actual_options))

    #操作多选的选择列表
    def test_operMutipleoptionsDropList(self):
        URL = 'F:\gitstorehouse\selenium3.0\webdriverAPI接口\测试页面\下拉框.html'
        self.driver.get(URL)
        from selenium.webdriver.support.ui import Select
        select_element = Select(self.driver.find_element_by_name('fruit'))
        #选择元素，多选
        select_element.select_by_index(1)
        select_element.select_by_visible_text('山楂')
        select_element.select_by_value('lizhi')
        for  optins in select_element.all_selected_options:
            print(optins.text)
        #取消所选元素
        select_element.deselect_all()
        for  optins in select_element.all_selected_options:
            print(optins.text)
        sleep(5)
        print('###########################################')
        #重新选择元素
        select_element.select_by_index(2)
        select_element.select_by_visible_text('山楂')
        select_element.select_by_value('lizhi')
        for  optins in select_element.all_selected_options:
            print(optins.text)
        sleep(2)
        #取消选择元素
        select_element.deselect_by_index(1)
        select_element.deselect_by_value('lizhi')
        select_element.deselect_by_visible_text('山楂')
        sleep(5)

    ########################################################################################################
    #操作可以输入的下拉列表（输入同时）
    def test_operateMulitileOptionDropList(self):
        url = 'F:\gitstorehouse\selenium3.0\webdriverAPI接口\测试页面\可以输入的下拉列表.html'
        self.driver.get(url)
        from selenium.webdriver.common.keys import Keys
        self.driver.find_element_by_id('select').clear()
        sleep(2)
        self.driver.find_element_by_id('select').send_keys('F',Keys.ARROW_DOWN)
        sleep(1)
        self.driver.find_element_by_id('select').send_keys(Keys.ARROW_DOWN)
        sleep(10)

    #操作单选框
    def test_operateRadio(self):
        url = 'F:\gitstorehouse\selenium3.0\webdriverAPI接口\测试页面\操作单选框.html'
        self.driver.get(url)
        berryRadio =  self.driver.find_element_by_xpath('/html/body/form/input[1]')
        berryRadio.click()
        #断言‘草莓'
        self.assertTrue(berryRadio.is_selected(),'草莓没选中')
        if berryRadio.is_selected():
            watermelonRadion = self.driver.find_element_by_xpath('/html/body/form/input[2]')
            watermelonRadion.click()
            self.assertFalse(berryRadio.is_selected())
        #查找所有name属性是‘fruit’的单选元素对象
        radioList = self.driver.find_elements_by_tag_name('input')
        #循环遍历radioList中的每个但选按钮，查找value值为‘orange’的单选框
        #如果找到此单选框后，发现未处于选中状态，则调用click方法
        for rado in radioList:
            if rado.get_attribute('value')=='orange':
                if not rado.is_selected():
                    rado.click()
                    sleep(5)
                    self.assertEqual(rado.get_attribute('value'),'orange')


    #操作复选框
    def test_operateCheckBox(self):
       url = 'F:\gitstorehouse\selenium3.0\webdriverAPI接口\测试页面\复选框.html'
       self.driver.get(url)
       #定位其中一个元素选择中
       berryCheckBox = self.driver.find_element_by_xpath('/html/body/form/input[1]')
       berryCheckBox.click()
       self.assertTrue(berryCheckBox.is_selected(),'复选框没有被选择')
       if berryCheckBox.is_selected():
           berryCheckBox.click()
           self.assertFalse(berryCheckBox.is_selected())
       radioList = self.driver.find_elements_by_tag_name('input')
       for rado in radioList:
           if  not rado.is_selected():
               rado.click()
       sleep(2)


    #断言页面源码中的关键字
    def test_assertKeyWord(self):
        hurl = 'http://www.baidu.com'
        self.driver.get(hurl)
        self.driver.find_element_by_xpath('//*[@id="kw"]').send_keys('光荣之路')
        sleep(5)
        assert '光荣之路' in self.driver.page_source,'不存在'

   #对当前浏览器窗口截图
    def test_captureScreenInCurrentWindow(self):
        hurl = 'http://www.baidu.com'
        self.driver.get(hurl)
        try:
           self.driver.find_element_by_xpath('//*[@id="kw"]').send_keys('光荣之路')
           result = self.driver.get_screenshot_as_file('F:\gitstorehouse\selenium3.0\webdriverAPI接口\截图/1.jpg')
           print(result)
        except IOError as e:
            raise e

    #拖拽页面元素
    def test_dragPageElement(self):
        url = 'http://jqueryui.com/resources/demos/draggable/scroll.html'
        self.driver.get(url)
        sleep(5)
        #定位三个可拖动元素
        oneelement = self.driver.find_element_by_xpath('//*[@id="draggable"]')
        twoelement = self.driver.find_element_by_xpath('//*[@id="draggable2"]')
        threenelement = self.driver.find_element_by_xpath('//*[@id="draggable3"]')
        #导入可提供拖拽元素的模块ActionChain
        from selenium.webdriver import ActionChains
        #实例化一个新的ActionChains
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(oneelement,twoelement).perform()
        sleep(2)
        #将页面上的元素向右下角拖动10个元素，拖动5次
        for i in range(5):
             action_chains.drag_and_drop_by_offset(threenelement,10,10).perform()
             sleep(2)

    #模拟键盘单个按键操作 浏览器版本过高
    def test_simualteASingleKing(self):
        hurl = 'http://www.baidu.com'
        self.driver.get(hurl)
        #导入按键模块
        from selenium.webdriver.common.keys import Keys
        from selenium.webdriver import ActionChains
        action_chains = ActionChains(self.driver)
        query = self.driver.find_element_by_xpath('//*[@id="kw"]')
        sleep(3)
        #点击F12
        action_chains.key_down(Keys.F12).key_up(Keys.F12).perform()
        # query.send_keys(Keys.F12)
        query.send_keys('selenium')
        #点击回车
        query.send_keys(Keys.ENTER)
        sleep(3)

    #tong过内建模块实现全选，剪切以及粘贴
    def test_simuationCombinatKeys(self):
        from selenium.webdriver import ActionChains
        from selenium.webdriver.common.keys import Keys
        hurl = 'http://www.baidu.com'
        self.driver.get(hurl)
        input = self.driver.find_element_by_xpath('//*[@id="kw"]')
        input.click()
        input.send_keys('光荣之路')
        sleep(2)
        action_chains = ActionChains(self.driver)
        action_chains.key_down(Keys.CONTROL).send_keys('a').key_up(Keys .CONTROL).perform()
        sleep(2)
        action_chains.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
        self.driver.get(hurl)
        self.driver.find_element_by_xpath('//*[@id="kw"]').click()
        action_chains.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform() 
        sleep(5)


    




if __name__== '__main__':
    unittest.main()