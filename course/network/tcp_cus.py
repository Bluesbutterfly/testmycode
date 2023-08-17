"""
创建TCP客户端
"""
import socket
# 主机的IP地址
host = '127.0.0.1'
# 端口号
port = 8080
# 创建socket
client = socket.socket()
client.connect((host,port))
# 发送数据
send_data = input("请输入要发送的数据：")
client.send(send_data.encode())
recv_data = client.recv(1024).decode()
print("接收到的数据是%s"%recv_data)
client.close()