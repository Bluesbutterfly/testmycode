import socket

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)# 主机的IP地址
host = '127.0.0.1'
s.bind((host,8888))
print("绑定UDP到8888端口")
data , addr = s.recvfrom(1024)
data = float(data)-1.8+32
send_data = "转换后的温度（单位：华氏度）："+str(data)
print("recieved form %s:%s"%addr)
s.sendto(send_data.encode(),addr)
s.close()