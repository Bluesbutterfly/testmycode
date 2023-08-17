# 导入模块
import sqlite3
# 创建链接对象
conn = sqlite3.connect('datadb/mrsoft.db')
# 创建游标对象
cursor = conn.cursor()
# 执行SQL语句
cursor.execute('create table user(id int(10) primary key, name varchar(20))')
# 关闭游标
cursor.close()
# 关闭链接
conn.close()