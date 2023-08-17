from wsgiref.simple_server import make_server

# wsgi接口
"""
environ环境变量
"""

def app(environ,start_response):
  start_response("200 OK",[('Content-Type','text/html; charset=utf-8'),('Date','Wed, 09 Aug 2023 07:33:10 GMT')])
  # print('*'*10)
  # print(environ['PATH_INFO'])
  # print('*'*10)
  file_name = environ['PATH_INFO'][1:] or 'index.html'
  HTML_ROOT_DRI = '../Views/'
  try:
    # 以二进制的方式读取文件
    file = open(HTML_ROOT_DRI + file_name,"rb")
  except:
    response = "File is not Fount"
  else:
    file_data = file.read()
    file.close()
    response = file_data.decode("utf-8")
  return [response.encode("utf-8")]

if __name__ == "__main__":
  ser = make_server('',8000,app)
  ser.serve_forever()