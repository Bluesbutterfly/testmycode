"""
使用队列在线程间通信
"""
from collections.abc import Callable, Iterable, Mapping
from queue import Queue
from threading import Thread
import time
import random
class Producer(Thread):
  def __init__(self, name, queue):
    Thread.__init__(self,name=name)
    self.data = queue
  def run(self):
    for i in range(5):
      print("生产者%s将产品%d加入队列"%(self.name,i))
      self.data.put(i)
      time.sleep(random.random())
    print("生产者%s完成！"%(self.name))
class Consumer(Thread):
  def __init__(self, name, queue):
    Thread.__init__(self,name=name)
    self.data = queue
  def run(self):
    for i in range(5):
      val = self.data.get()
      print("消费者%s将产品%d从队列中取出"%(self.name,val))
      time.sleep(random.random())
    print("消费者%s完成！"%(self.name))
if __name__ == '__main__':
  print("--主线程开始--")
  queue = Queue()
  producer = Producer('Producer',queue)
  consumer = Consumer("Consumer",queue)
  producer.start()
  consumer.start()
  producer.join()
  consumer.join()
  print("--主线程结束--")