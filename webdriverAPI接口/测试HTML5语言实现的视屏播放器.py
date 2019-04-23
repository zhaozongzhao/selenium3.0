import unittest
from selenium import webdriver
import time

class TestDome(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        # self.driver = webdriver.Chrome()
    def test_HTMLVideoPalys(self):

        url = 'http://www.runoob.com/try/try.php?filename=tryjsref_video_play'
        #访问html5语言实现的播放器
        self.driver.get(url)
        #打印出源码用于学习
        # print(self.driver.page_source)
        #定位获取页面中video元素对象
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('//*[@id="iframeResult"]'))
        videoPlayer = self.driver.find_element_by_xpath('//*[@id="myVideo"]')
        #使用javascript语句，通过播放器内部
        #currentSrc属性获取视屏文件的网络存储位置
        videosrc = self.driver.execute_script("return arguments[0].currentSrc;",videoPlayer)
        print(videosrc)
        # #断言视屏存储地址是否符合预期
        # self.assertEqual(videosrc,'http://www.runoob.com/try/demo_source/mov_bbb.mp4')
        # #通过javascript 通过视屏内部duration属性获取视屏文件的播放时长
        # videoDuration = self.driver.execute_script('return arguments[0].duration;',videoPlayer)
        # self.assertEqual(int(videoDuration),10)
        #通过paly实现视屏播放
        time.sleep(5)
        self.driver.execute_script('return document.getElementById("myVideo").play();')
        self.driver.save_screenshot('F:\gitstorehouse\selenium3.0\webdriverAPI接口\截图\\video2.jpg')
        #播放5秒，便于人工识别
        time.sleep(5)
        #通过pause实现暂停
        self.driver.execute_script('return arguments[0].pause();',videoPlayer)
        # 暂停3秒，便于人工识别
        time.sleep(3)
        self.driver.save_screenshot('F:\gitstorehouse\selenium3.0\webdriverAPI接口\截图\\video.jpg')