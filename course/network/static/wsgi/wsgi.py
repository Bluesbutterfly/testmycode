from wsgiref.simple_server import make_server

# wsgi接口

def sayhello(environ,start_response):
  start_response("200 OK",[('Content-Type','text/html; charset=utf-8'),('Date','Wed, 09 Aug 2023 07:33:10 GMT')])
  return [b'hello word']

if __name__ == "__main__":
  ser = make_server('',8000,sayhello)
  ser.serve_forever()