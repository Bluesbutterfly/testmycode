
# import pymysql
# #调用connect()函数生成connection链接对象
# db = pymysql.connect(host='localhost',user='root',password='welcome123',database='user',charset='utf8')
# # 调用cursor()方法，创建Cursor对象
# cursor = db.cursor()
# cursor.execute('drop table if exists userinfo')
# # 执行SQL语句
# sql = """
# CREATE TABLE userinfo(
# id int(8) NOT NULL AUTO_INCREMENT,
# name varchar(50) NOT NULL,
# emain varchar(50) NOT NULL,
# telphone varchar(50) NOT NULL,
# userName varchar(50) NOT NULL,
# nickName varchar(50) NOT NULL,
# identityCard varchar(50) NOT NULL,
# password varchar(50) DEFAULT NULL,
# publish_time date DEFAULT NULL,
# downline_time date DEFAULT NULL,
# PRIMARY KEY (id)
# )ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
# """
# cursor.execute(sql)
# # 关闭链接
# cursor.close()
# db.close()
SECRET_KEY = '1315as4dvf45das8eq5as3215z5asq'
nums= [0,0,1,1,1,2,2,3,3,4]


