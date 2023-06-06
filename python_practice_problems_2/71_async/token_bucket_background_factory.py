#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 16:37:37 2023

@author: johnmorgan
"""

from threading import Thread
from threading import Condition
from threading import current_thread
import time

class TokenBucketFilterFactory:

    @staticmethod
    def makeTokenBucketFilter(capacity):
        tbf = MultithreadedTokenBucketFilter(capacity)
        tbf.initialize();
        return tbf;


class MultithreadedTokenBucketFilter:
    def __init__(self, maxTokens):
        self.MAX_TOKENS = int(maxTokens)
        self.possibleTokens  = int(0)
        self.ONE_SECOND = int(1)
        self.cond = Condition()

    def initialize(self):
        dt = Thread(target = self.daemonThread);
        dt.setDaemon(True);
        dt.start();
                
    def daemonThread(self):
        while True:
            self.cond.acquire()
            if self.possibleTokens < self.MAX_TOKENS:
                self.possibleTokens = self.possibleTokens + 1;
            self.cond.notify() 
            self.cond.release()
            
            time.sleep(self.ONE_SECOND);
    
    def getToken(self):
        self.cond.acquire()
        while self.possibleTokens == 0:
            self.cond.wait()
        self.possibleTokens = self.possibleTokens - 1
        self.cond.release()

        print("Granting " + current_thread().getName() + " token at " + str(time.time()))
    
if __name__ == "__main__":
    threads_list = [];
    bucket = TokenBucketFilterFactory.makeTokenBucketFilter(5)
    
    time.sleep(3)

    for x in range(12):
        workerthread =  Thread(target=bucket.getToken)
        workerthread.name = "Thread_" + str(x+1)
        threads_list.append(workerthread)
        
    
    for t in threads_list:
        t.start()
        
    for t in threads_list:
        t.join()