import time
import threading
import asyncio
from multiprocessing import Process


def cal_average(num):  # Average function used for sequential programming, threading, and multiprocessing
  print('Start of Helper (seq):')
  sum_num = 0
  for t in num:
    sum_num = sum_num + t
  avg = sum_num / len(num)
  time.sleep(1)
  print('Average:', avg)
  return avg

def main_sequential(list1, list2, list3):  # Main wrapper for sequential example
  s = time.perf_counter()
  cal_average(list1)
  cal_average(list2)
  cal_average(list3)

  elapsed = time.perf_counter() - s
  print("Sequential Programming Elapsed Time: " + str(elapsed) + " seconds")

async def cal_average_async(num):  # Average function used for asynchronous programming only ( needs await asyncio.sleep() )
  print('Start of Helper(async):')
  sum_num = 0
  for t in num:
    sum_num = sum_num + t
  avg = sum_num / len(num)
  await asyncio.sleep(1)
  print('Average:', avg)
  return avg

async def main_async(list1, list2, list3):  # Main wrapper for asynchronous example
  s = time.perf_counter()
  tasks = [cal_average_async(list1), cal_average_async(list2), cal_average_async(list3)]
  await asyncio.gather(*tasks)
  elapsed = time.perf_counter() - s
  print("Asynchronous Programming Elapsed Time: " + str(elapsed) + " seconds")

def main_threading(list1, list2, list3):  # Main wrapper for threading example
  s = time.perf_counter()
  lists = [list1, list2, list3]
  threads = list()
  for i in range(len(lists)):
    x = threading.Thread(target=cal_average, args=(lists[i],))
    threads.append(x)
    x.start()
  for t in threads:
    t.join()
  elapsed = time.perf_counter() - s
  print("Threading Elapsed Time: " + str(elapsed) + " seconds")

def main_multiprocessing(list1, list2, list3):  # Main wrapper for multiprocessing example
  s = time.perf_counter()
  lists = [list1, list2, list3]
  p = [Process(target=cal_average, args=(l,)) for l in lists]
  [process.start() for process in p]
  [process.join() for process in p]
  elapsed = time.perf_counter() - s
  print("Multiprocessing Elapsed Time: " + str(elapsed) + " seconds")


if __name__ == '__main__':  # Need to use this if-statement so multiprocessing doesn't cause an infinite loop
  l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  l2 = [2, 4, 6, 8, 10]
  l3 = [1, 3, 5, 7, 9, 11]
  main_sequential(l1, l2, l3)
  loop = asyncio.get_event_loop()
  loop.run_until_complete(main_async(l1, l2, l3))
  main_threading(l1, l2, l3)
  main_multiprocessing(l1, l2, l3)
