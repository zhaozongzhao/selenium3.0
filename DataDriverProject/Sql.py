#创建数据库语句
create_database = ' CREATE DATABASE IF NOT EXISTS gloryrody DEFAULT CHARSET utf8 COLLATE utf8_general_ci; '

#创建数据表
create_table = '''
create table testdata(
id int(11) not null auto_increment,
bookname varchar(20),
author varchar(20),
PRIMARY KEY(id)
)engine=InnoDB DEFAULT CHARSET=utf8;
'''