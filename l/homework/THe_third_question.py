# 补充缺失的代码：用代码实现以下中文内容
# def print_directory_contents(sPath):
#
# """
# 这个函数接受文件夹的名称作为输入参数，
# 返回该文件夹中文件的路径，
# 以及其包含文件夹中文件的路径。
import os
def print_directory_contents(sPath):
     for root, dirs, files in os.walk(sPath):
            # root #当前目录路径 dirs #当前路径下所有子目录files) #当前路径下所有非目录子文件
        for i in files:
            print(os.path.abspath(i))
if __name__ == '__main__':
    print_directory_contents('D:\\test')