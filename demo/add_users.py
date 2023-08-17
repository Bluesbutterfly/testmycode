# 导入模块
import sqlite3
# 创建链接对象
conn = sqlite3.connect('datadb/mrsoft.db')
# 创建游标对象
cursor = conn.cursor()
# 执行SQL语句
"""
增加
使用?占位符避免SQ注入
"""
sql = 'insert into user(id,name) values(?,?)'
cursor.execute(sql,(2,'xiaoming'))
# 插入多条记录
data = [
    (3,'andy'),(4,'kobi'),(5,'litter')
]
cursor.executemany(sql,data)
# 查询结果集
# sql1 = 'select * from user where id>3'
# cursor.execute(sql)
# 获取一条结果集
# result1 = cursor.fetchone()
# 获取指定结果
# result1 = cursor.fetchmany(2)
# 获取所有结果集
# result1 = cursor.fetchall()
# print(result1)
"""
修改语句
"""
sql = 'update user set name= ? where id = ?'
cursor.execute(sql,('mr',1))
"""
删除
"""
sql = 'delete from user where id = ?'
cursor.execute(sql,(1,))
# 关闭游标
cursor.close()
"""
提交事务
查询语句是不需要提交事务的
"""
conn.commit()
# 关闭链接
conn.close()