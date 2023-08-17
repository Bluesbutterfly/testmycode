"""
创建线程
threading模块Thread类创建线程
使用Thread子类创建线程
线程之间数据是可以共享的
"""
# 使用multiprocessing模块创建线程
from threading import Thread
import time
import os
def plus():
  print("--子线程1开始--")
  global g_num
  g_num += 50
  print("g_num is %d" %g_num)
  print("--子线程1结束--")
def minus():
  print("--子线程2开始--")
  global g_num
  g_num -= 50
  print("g_num is %d" %g_num)
  print("--子线程2结束--")
g_num = 100
def main():
  print("主线程开始")
  print("主线程的PID:%s" % os.getpid())
  p1 = Thread(target=plus)
  p2 = Thread(target=minus)
  p1.start()
  p2.start()
  p1.join()
  p2.join()
  print("主线程结束")

if __name__ == '__main__':
  main()