"""
创建进程
os.fork()函数 （只支持linux系统）
multiprocessing模块Process类
Process类的子类
Pool进程池
"""
# 使用multiprocessing模块创建进程
from multiprocessing import Process
import time
import os
def child_1(intervel):
  print("子进程(%s)开始执行，它的父进程是(%s)" %(os.getpid(),os.getppid()))
  t_start = time.time()
  time.sleep(intervel)
  t_end = time.time()
  print("子进程(%s)执行时间为%0.2f秒" %(os.getpid(),t_end - t_start))
def child_2(intervel):
  print("子进程(%s)开始执行，它的父进程是(%s)" %(os.getpid(),os.getppid()))
  t_start = time.time()
  time.sleep(intervel)
  t_end = time.time()
  print("子进程(%s)执行时间为%0.2f秒" %(os.getpid(),t_end - t_start))

def main():
  print("主进程开始")
  print("主进程的PID:%s" % os.getpid())
  p1 = Process(target=child_1,args=(1,))
  p2 = Process(target=child_2,name="softname",args=(2,))
  p1.start()
  p2.start()
  print('p1.is_alive=%s' % p1.is_alive())
  print('p2.is_alive=%s' % p2.is_alive())
  print('p1.name = %s' % p1.name)
  print('p1.pid = %s' % p1.pid)
  print('p2.name = %s' % p2.name)
  print('p2.pid = %s' % p2.pid)
  p1.join()
  p2.join()
  print("主进程结束")

if __name__ == '__main__':
  main()