# 套接字
# import socket
# s = socket.socket()
"""
创建TCP服务器
"""
import socket
# 主机的IP地址
host = '127.0.0.1'
# 端口号
port = 8080
# 创建socket
web = socket.socket()
# 绑定IP地址和端口号
web.bind((host,port))
# 监听（最大监听）
web.listen(5)
print("服务器等待客户端链接")
while True:
  # 等待接收
  con,addr = web.accept()
  # 获取客户端请求数据（接收最大数量）
  data = con.recv(1024)
  print(data)
  # 向客户端发送数据
  con.sendall(b'HTTP/1.1 200 OK\r\n\r\n hello word')
  # 关闭
  con.close()
