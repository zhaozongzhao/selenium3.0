import pymysql
from DataDriverProject.Sql import *


class DataBaseInit(object):
    #本类用于完成初始化数据操作
    #创建数据库，数据表，想表中插入测试数据
    def __init__(self,host,port,dbname,username,password,charset):
        self.host = host
        self.port = port
        self.db = dbname
        self.username = username
        self.password = password
        self.charset = charset

    def create(self):
        try:
            #连接数据库
            conn = pymysql.connect(
                host = self.host,
                port = self.port,
                user = self.username,
                password = self.password,
                charset = self.charset
            )
            #获取数据库游标
            cur = conn.cursor()
            #创建数据库
            # cur.execute(create_database)
            #选择已经创建好的数据库
            conn.select_db('gloryrody1')
            #创建测试表
            cur.execute(create_table)
        except Exception as e:
            print(e)
        else:
            #关闭游标
            cur.close()
            #提交操作
            conn.commit()
            #关闭连接
            conn.close()
            print('创建数据表成功')

    def inserDatas(self):
        try:
            #连接mysql数据库中具体某个库
            conn = pymysql.connect(
                host=self.host,
                port=self.port,
                db =self.db,
                user=self.username,
                password=self.password,
                charset=self.charset
            )
            cur = conn.cursor()
            sql = 'INSERT INTO testdata(id,bookname,author) VALUES(%s,%s,%s);'
            res = cur.executemany(sql,[(4,'selenium','sssss'),(5,'Http权威指南','古吉尔')])
        except Exception as E:
            print(E)
        else:
            conn.commit()
            cur.execute('select * from testdata;')
            for i  in cur.fetchall():
                print(i[1],i[2])
            cur.close()
            conn.close()


if __name__ == '__main__':
      db = DataBaseInit(
            host = 'localhost',
            port = 3306,
            dbname = 'gloryrody1',
            username = 'root',
            password = '123456',
            charset = 'utf8'
        )
      # db.create()
      db.inserDatas()
      print('数据初始化完成')



