import unittest
from selenium import webdriver
import time

class TestDome(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_HTMLVideoPalys(self):

        url = 'http://www.w3school.com.cn/tiy/t.asp?f=html5_video_all'
        #访问html5语言实现的播放器
        self.driver.get(url)
        #打印出源码用于学习
        # print(self.driver.page_source)
        #定位获取页面中video元素对象
        self.driver.switch_to.frame(1)
        videoPlayer = self.driver.find_element_by_xpath('/html/body/video')
        #使用javascript语句，通过播放器内部
        #currentSrc属性获取视屏文件的网络存储位置
        videosrc = self.driver.execute_script("return arguments[0].currentSrc;",videoPlayer)
        print(videosrc)
        #断言视屏存储地址是否符合预期
        self.assertEqual(videosrc,'http://www.w3school.com.cn/i/movie.ogg')
        #通过javascript 通过视屏内部duration属性获取视屏文件的播放时长
        videoDuration = self.driver.execute_script('return arguments[0].duration;',videoPlayer)
        self.assertEqual(int(videoDuration),3)
        #通过paly实现视屏播放
        self.driver.execute_script('return arguments[0].play();',videoPlayer)
        #播放5秒，便于人工识别
        time.sleep(2)
        #通过pause实现暂停
        self.driver.execute_script('return arguments[0].pause();',videoPlayer)
        # 暂停3秒，便于人工识别
        time.sleep(3)
        self.driver.save_screenshot('F:\gitstorehouse\selenium3.0\webdriverAPI接口\截图\\video.jpg')