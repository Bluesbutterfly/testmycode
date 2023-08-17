# import urllib.request #导入网络请求模块

# response = urllib.request.urlopen('http://www.baidu.com/?tn=54093922_35_hao_pg') #实现网络请求

# print(response.read().decode('utf-8'))
# import urllib.request
# import urllib.parse #导入解析模块
# # 创建参数
# data = bytes(urllib.parse.urlencode({"word":"Hellow"}),encoding="utf-8")
# # 发送post网络请求
# response = urllib.request.urlopen('http://httpbin.org/post',data = data)
# html = response.read()
# print(html)
# import urllib3 #导入标准库升级版模块
# #创建PoolManager对象，用于处理于线程的链接以及线程安全
# http = urllib3.PoolManager() 
# # 发送网络请求
# resp = http.request("POST", "http://httpbin.org/post",fields={"word":"Hellow"})
# print(resp.data.decode())
# import requests

# data = {"word":"Hellow"} #表单参数
# resp = requests.post("http://httpbin.org/post",data=data)
# print('状态码',resp.status_code)
# # print('请求地址',resp.url)
# # print('头部信息',resp.headers)
# # print('cookies信息',resp.cookies)
# # print('文本源码',resp.text)
# print('字节流源码',resp.content)
# import requests

# url = "https://www.whatismyip.com/"
# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'}
# response = requests.get(url,headers=headers)
# print(response.content.decode('utf-8'))
# import requests
# # 导入网络请求模块中的三种异常类
# from requests.exceptions import ReadTimeout,HTTPError,RequestException
# # 循环发送50次网络请求
# for a in range(0,50):
#     try:
#       response = requests.get("https://www.whatismyip.com/",timeout=0.5)
#       print(response.status_code)
#     except ReadTimeout:
#       print('timeout')
#     except HTTPError:
#        print('httpError')
#     except RequestException:
#        print('requireerror')
# import requests
# # 设置代理IP
# propxy = {"http":"112.124.2.212:8888",
#           "https":"111.225.153.18:8089"}
# response = requests.get('https://www.baidu.com',proxies=propxy)
# print(response.content.decode('utf-8'))
import requests
from bs4 import BeautifulSoup
response = requests.get('https://news.baidu.com')
# html_doc = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title"><b>The Dormouse's story</b></p>

# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>

# <p class="story">...</p>
# """
# soup = BeautifulSoup(html_doc,features='lxml')
# soup = BeautifulSoup(open("D:/snippet/AW/active/2023/awdouyin/h5/index.html","r",encoding="utf-8"),features='lxml')
soup = BeautifulSoup(response.text,features='lxml')
# print(soup)
# print(soup.prettify())
print(soup.find('title').text)
# print('html代码的title：',soup.title)