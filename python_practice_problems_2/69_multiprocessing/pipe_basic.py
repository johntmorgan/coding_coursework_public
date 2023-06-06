#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 28 14:11:22 2023

@author: johnmorgan
"""

from multiprocessing import Process, Pipe
import time

def child_process(conn):
    for i in range(0, 10):
        conn.send("hello " + str(i + 1))
    conn.close()


if __name__ == '__main__':
    parent_conn, child_conn = Pipe()
    p = Process(target=child_process, args=(child_conn,))
    p.start()
    time.sleep(3)

    for _ in range(0, 10):
        msg = parent_conn.recv()
        print(msg)

    parent_conn.close()
    p.join()
