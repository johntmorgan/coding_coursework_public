#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 16:06:01 2023

@author: johnmorgan
"""

from threading import Thread
from threading import current_thread
from threading import Semaphore
from threading import current_thread
from threading import Lock
from threading import Barrier
import random
import time

class TokenBucketFilter:
    def __init__(self, MAX_TOKENS):
        self.MAX_TOKENS = MAX_TOKENS
        self.last_request_time = time.time()
        self.possible_tokens = 0
        self.lock = Lock()

    def get_token(self):
        with self.lock:
            # Is it a problem time.time() called in separate spots without
            # being set in a fixed way? - JM
            self.possible_tokens += int((time.time() - self.last_request_time))
            if self.possible_tokens > self.MAX_TOKENS:
                self.possible_tokens = self.MAX_TOKENS
            if self.possible_tokens == 0:
                time.sleep(1)
            else:
                self.possible_tokens -= 1
            self.last_request_time = time.time()

            print("Granting {0} token at {1} ".format(current_thread().
                    getName(), int(time.time())));


if __name__ == "__main__":

    token_bucket_filter = TokenBucketFilter(1)

    # time.sleep(10)

    threads = list()
    for _ in range(0, 10):
        threads.append(Thread(target=token_bucket_filter.get_token))

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()
