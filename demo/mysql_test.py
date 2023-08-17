import pymysql

#调用connect()函数生成connection链接对象
db = pymysql.connect(host='localhost',user='root',password='welcome123',database='test')
# 调用cursor()方法，创建Cursor对象
cursor = db.cursor()
# 执行SQL语句
cursor.execute('select version()')
data = cursor.fetchone()
print(data)
# 关闭链接
cursor.close()
db.close()