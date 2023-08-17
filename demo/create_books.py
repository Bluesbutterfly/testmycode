import pymysql

#调用connect()函数生成connection链接对象
db = pymysql.connect(host='localhost',user='root',password='welcome123',database='test')
# 调用cursor()方法，创建Cursor对象
cursor = db.cursor()
cursor.execute('drop table if exists books')
# 执行SQL语句
sql = """
CREATE TABLE books(
  id int(8) NOT NULL AUTO_INCREMENT,
  name varchar(50) NOT NULL,
  category varchar(50) NOT NULL,
  price decimal(10,2) DEFAULT NULL,
  publish_time date DEFAULT NULL,
  PRIMARY KEY (id)
)ENGINE=MyISAM AUTO_INCREMENT=1 DEFAULT CHARSET=utf8;
"""
cursor.execute(sql)
# 关闭链接
cursor.close()
db.close()