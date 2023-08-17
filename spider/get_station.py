import requests
import re
import os

def  getstation():
  url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9272'
  response = requests.get(url,verify=True)
  """
  信息筛选
  返回中文以及大写字母
  """
  stations = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)',response.text)
  stations = dict(stations) #转换成字典
  stations = str(stations) #转换为字符串类型,否则无法写入文件
  write(stations) #调用写入方法，实现下载本站文件

def write(stations):
  # 写入模式打开文件
  file = open('spider/stations.text','w',encoding='utf-8_sig')
  file.write(stations) #写入文件
  file.close()
def read():
  #以写模式打开文件
  file = open('spider/stations.text','r',encoding='utf-8_sig')
  data = file.readline() #读取文件
  file.close()
  return data
def isStations():
  #判断车站文件是否存在
  istations = os.path.exists('spider/stations.text')
  return istations
if isStations() == False:
  getstation()
  # read()
else:
  print('该文件已存在')
