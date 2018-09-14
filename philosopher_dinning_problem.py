# -*- encoding:utf8 -*-
import random
import time
from threading import Semaphore, Thread

TOTAL_COUNT = 5

forks = [Semaphore(1) for _ in range(TOTAL_COUNT)]


def think():
    time.sleep(random.randint(1, 5))


def eat(i):
    print("%s 拿到了两个勺子，开始吃饭" % i)
    time.sleep(random.randint(1, 5))
    print("%s 吃饭完毕" % i)


def get_fork(i):
    if i == 0:
        forks[(i + 1) % TOTAL_COUNT].acquire()
        forks[i].acquire()
    else:
        forks[i].acquire()
        forks[(i + 1) % TOTAL_COUNT].acquire()


def put_fork(i):
    if i == 0:
        forks[(i + 1) % TOTAL_COUNT].release()
        forks[i].release()
    else:
        forks[i].release()
        forks[(i + 1) % TOTAL_COUNT].release()


def loop(i):
    while True:
        think()
        get_fork(i)
        eat(i)
        put_fork(i)


for i in range(TOTAL_COUNT):
    Thread(target=loop, args=(i,)).start()

