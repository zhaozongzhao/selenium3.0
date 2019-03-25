from PIL import Image
from selenium import webdriver
import unittest,time

class ImageCompare(object):
    # "本类实现了对两张通过图片的像素算法对比,获取文件的像素个数大小,然后使用了循环的方式将两张图片的所有项目进行一一对比"
    # "并计算对比相似度百分比"

    def make_regalur_image(self,img,size=(256,256)):
        #创建一个有规律的图片
        #将图片尺寸强制规范为特定的大小,然后再将其转换为'RGB'
        return img.resize(size).convert('RGB')

    def split_image(self,img,part_size = (64,64)):
        #将图片按给定大小切分
        w,h = img.size
        pw,ph =part_size
        assert w % pw == h % ph == 0
        #img.crop指在图像上截剪一个box矩形区域,然后显示出来,box是一个有四个数字的元组(upper_left_x,upper_left_y,lower_right_x,
        # lower_right_y),分别表示裁剪矩形区域的左上角x,y坐标,右下角的x,y坐标,规定图像的最左上角的坐标为原点(0,0),宽度的方向为x轴，
        # 高度的方向为y轴，每一个像素代表一个坐标单位。crop()返回的仍然是一个Image对象
        return [img.crop((i,j,i+pw,j+ph)).copy()
                for i in range(0,w,pw) for j in range(0,h,ph)]

    def hist_similar(self,lh,rh):
        #统计图片每部分的相似度
        assert len(lh) == len(rh)
        return sum(1 - (0 if l == r else float(abs(1 - r)) / max(1,r))
                   for l,r in zip(lh,rh)) / len(lh)

    def clar_similar(self,li,ri):
        #计算两张图片的相似度
        print(self.split_image(li))
        return sum(self.hist_similar(l.histogram(),r.histogram())
                   for l,r in zip(self.split_image(li),self.split_image(ri)))/16.0


    def calr_similar_by_path(self,lf,rf):
        # 通过路径计算相抵度
        #img.open 打开显示图片
        li,ri = self.make_regalur_image(Image.open(lf)),self.make_regalur_image(Image.open(rf))
        return self.clar_similar(li,ri)

class TestDome(unittest.TestCase):
    def setUp(self):
        self.IC = ImageCompare()
        self.driver =  webdriver.Chrome()

    def tearDown(self):
        self.driver.quit()

    def test_ImageComparioson(self):
        # url = 'http://www.sogou.com'
        # self.driver.get(url)
        # time.sleep(3)
        # self.driver.save_screenshot('/Users/hnbl009/gitfile/selenium3.0/webdriverAPI接口/测试页面/test1.png')
        # self.driver.get(url)
        # time.sleep(3)
        # self.driver.get_screenshot_as_file('/Users/hnbl009/gitfile/selenium3.0/webdriverAPI接口/测试页面/test2.png')
        # time.sleep(3)
        print(self.IC.calr_similar_by_path('/Users/hnbl009/gitfile/selenium3.0/webdriverAPI接口/测试页面/test1.png',
                                           '/Users/hnbl009/gitfile/selenium3.0/webdriverAPI接口/测试页面/test2.png') * 100)

