import pymysql

#调用connect()函数生成connection链接对象
db = pymysql.connect(host='localhost',user='root',password='welcome123',database='test',charset='utf8')
# 调用cursor()方法，创建Cursor对象
cursor = db.cursor()
data = [("基础","python","79.80","2018-11-11"),("基础","python","79.80","2018-11-11"),("基础","python","79.80","2018-11-11")]
try:
  # 执行SQL语句
  sql = "insert into books(name,category,price,publish_time) values (%s,%s,%s,%s)"
  # 插入一条记录
  # cursor.execute(sql,data)
  # 插入多条记录
  cursor.executemany(sql,data)
  db.commit()
except:
    # 执行回滚操作
    db.rollback()

# 关闭链接
cursor.close()
db.close()