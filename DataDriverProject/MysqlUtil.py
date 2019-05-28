import pymysql
from DataDriverProject.DataBaseInit import  DataBaseInit
from DataDriverProject.Sql import *

class mymysql(object):

    def __init__(self, host, port, dbname, username, password, charset):
        #连接数据库进行数据初始化操作
          self.host = host
          self.port = port
          self.db = dbname
          self.username = username
          self.password = password
          self.charset = charset
          self.conn = pymysql.connect(
             host=self.host,
             port=self.port,
             db = dbname,
             user=self.username,
             password=self.password,
             charset=self.charset
          )
          self.cur = self.conn.cursor()

    def getDataFromDataBase(self):
        #从测试表中获取测试数据
        self.cur.execute(select_table)
        datasTuple = self.cur.fetchall()
        print(type(datasTuple))
        return datasTuple

    def closeDatabase(self):
        self.cur.close()
        self.conn.commit()
        self.conn.close()

if __name__ == '__main__':
    db = mymysql(
        host='localhost',
        port=3306,
        dbname='gloryrody1',
        username='root',
        password='123456',
        charset='utf8'
    )
    print(db.getDataFromDataBase())
    db.closeDatabase()





