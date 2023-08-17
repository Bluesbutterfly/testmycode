"""
互斥锁
"""
# 1.创建锁
# import threading
# mutex= threading.Lock()
# # 2.锁定
# mutex.acquire(False)

# # 3.释放锁
# mutex.release()
from threading import Thread,Lock

import time

n=100
def task():
  global n
  mutex.acquire()
  time.sleep(0.1)
  n-=1
  print("购买成功，剩余%d张电影票" % n)
  mutex.release()
  
if __name__ == '__main__':
  mutex= Lock()
  t_l = []
  for i in range(10):
    t = Thread(target=task)
    t_l.append(t)
    t.start()
  for t in t_l:
    t.join()