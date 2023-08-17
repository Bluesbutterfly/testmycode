import socket
# 主机的IP地址
host = socket.gethostname()
# 端口号
port = 12345
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
print("已经链接")
info = ""
while info != "byebye":
    send_data = input("请输入发送的内容：")
    s.send(send_data.encode())
    if send_data == "byebye":
        break
    info = s.recv(1024).decode()
    print("接收到的内容：%s" % info)
s.close()