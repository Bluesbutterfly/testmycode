"""
创建进程
os.fork()函数 （只支持linux系统）
multiprocessing模块Process类
Process类的子类
Pool进程池
"""
# 使用Process类的子类创建进程
from collections.abc import Callable, Iterable, Mapping
from multiprocessing import Process
import time
import os
from typing import Any
class SubProcess(Process):
  def __init__(self, interval, name = ''):
    # super(SubProcess,self).__init__()
    Process.__init__(self)
    self.interval = interval
    if name:
      self.name = name
  def run(self):
    print("子进程(%s)开始执行，它的父进程是(%s)" %(os.getpid(),os.getppid()))
    t_start = time.time()
    time.sleep(self.interval)
    t_end = time.time()
    print("子进程(%s)执行时间为%0.2f秒" %(os.getpid(),t_end - t_start))
def main():
  print("主进程开始")
  print("主进程的PID:%s" % os.getpid())
  p1 = SubProcess(interval=1,name="food")
  p2 = SubProcess(interval=2)
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