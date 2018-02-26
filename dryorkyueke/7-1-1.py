import unittest
import random

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        #初始化一个递增序列
        self.seq = range(10)

    '''通过runtest执行方法，叫做静态方法'''
    def runTest(self):
        element = random.choice(self.seq)
        self.assertTrue(element in self.seq)

# class TestDictValueFormatFuntions(unittest.TestCase):
#     def setUp(self):
#         #初始化一个递增序列
#         self.seq = range(10)
#
#     def test_shuffle(self):
#         #随机打乱seq的顺序
#         random.shuffle(self.seq)
#         self.assertEqual(self.seq,range(10))
#         self.assertRaises(TypeError,random.shuffle,(1,2,3))



if __name__ == '__main__':
    unittest.main()