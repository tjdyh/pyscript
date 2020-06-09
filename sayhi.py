# -*- coding: utf-8 -*-

from threading import Thread
import time

class Sayhi(Thread):
    def __init__(self,name):
        super().__init__()
        self.name = name
    def run(self):
        time.sleep(2)
        print('%s say hello' % self.name)


if __name__ == '__main__':
    t = Sayhi('blg')
    t.start()
    print('主线程')