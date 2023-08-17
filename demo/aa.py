import datetime
import math
import random #导入生成随机数的模块
import os
def formatTime(longtime):
    """格式化时间"""
    import time
    return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(longtime))
def formatByte(number):
    """格式化文件大小"""
    for (scale,label) in [(1024*1024*1024,"GB"),(1024*1024,"MB"),(1024,"KB")]:
        if number >= scale: #大于等于1KB
            return "%.2f %s" %(number * 0.1 / scale, label)
        elif number == 1:
            return "1字节"
        else: #小于1KB
            byte = "%.2f" %(number or 0)
    return (byte[:-3] if byte.endswith(".00") else byte) + "字节"
# 创建多级目录
# os.makedirs("d:/pytest/test/demo")
# 创建目录
# if not os.path.exists("init"):
#     os.mkdir("init")
# else:
#     print("该目录已经存在")
# 删除目录
# if os.path.exists("test"):
# os.rmdir("test")
# 遍历目录
# path = r"D:\pytest"
# for root,dirs,files in os.walk(path,topdown = True): #遍历指定目录
#     for name in dirs:
#         print(os.path.join(root,name)) #输出遍历到的目录
#     for name in files:
#         print("\t",os.path.join(root,name)) #输出遍历到的目录
# 删除文件
# os.remove()
# 重命名文件和目录
# src = "" #原路径
# dst = "" #修改后的路径
# os.rename(src,dst)
# 获取文件基本信息
fileinfo = os.stat("aa.txt")
print("文件完整路径：",os.path.abspath("aa.txt")) #获取文件的完整路径
# 输出文件的基本信息
print("索引号：",fileinfo.st_ino)
print("设备名：",fileinfo.st_dev)
print("文件大小：",formatByte(fileinfo.st_size))
print("最后一次访问时间：",formatTime(fileinfo.st_atime))
print("最后一次修改时间：",formatTime(fileinfo.st_mtime))
print("最后一次状态变化时间：",formatTime(fileinfo.st_ctime))
# name = []
# sign = []
# dictionary = dict(zip(name,sign))
# print(datetime.datetime.now())
# # 列表推导式
# list = [random.randint(10,100) for i in range(10)]
# print(list)
# # 二维列表
# room = [
#     [1101,1102,1103,1104],
#     [2101,2102,2103,2104]
# ]
# def sign(**sign):
#     print()
#     for key,value in sign.items(): #字典遍历
#         print(key,value)
# sign(name='名字',value='字典值')
# r = 10 #半径
# # 匿名函数
# results = lambda r:math.pi*r*r
# print(results(r))
# # 访问权限
# class Swan:
#     """
#     天鹅类
#     """
#     _neck_swan = "天鹅的脖子很长" #保护类型的属性
#     __neck_swan = "天鹅的脖子很长" #私有类型的属性
#     def __init__(self):
#         print("__init__():",Swan.__neck_swan) #访问保护类型的属性
# swan = Swan() #创建Swan类的实例（对象）
# print("直接访问",swan._neck_swan)
# class Rect:
#     def __init__(self,width,height):
#         self.width = width
#         self.height = height
#     # 转换成属性
#     @property
#     def area(self):
#         return self.width * self.height #计算矩形面积
# rect = Rect(800,600) #创建类的实例
# print("面积为",rect.area)
