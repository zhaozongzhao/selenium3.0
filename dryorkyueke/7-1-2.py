import unittest

#被测试类
class mycalss(object):
    @classmethod
    def sum(cls,a,b):
        return a + b

    @classmethod
    def  sub(cls,a,b):
        return a - b

class mytest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        '''初始化类固件'''
        print('-----setupclass')

    @classmethod
    def tearDownClass(cls):
        '''重构类固件'''
        print('-----teardownclass')

    def setUp(self):
        self.a = 3
        self.b = 1
        print('----setup')

    def tearDown(self):
        print('----teardown')

    def testsum(self):
        self.assertEqual(mycalss.sum(self.a,self.b),4,'test sum fail')

    def testsub(self):
        self.assertEqual(mycalss.sub(self.a,self.b),2,'test sub fail')

if __name__ == '__main__':
    unittest.main()