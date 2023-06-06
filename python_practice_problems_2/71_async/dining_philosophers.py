#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 11:25:07 2023

@author: johnmorgan
"""

from threading import Semaphore
from threading import Thread
import random
import time

class DiningPhilosopherProblem:
    
    def __init__(self):
        self.forks = [None] * 5
        self.forks[0] = Semaphore(1)
        self.forks[1] = Semaphore(1)
        self.forks[2] = Semaphore(1)
        self.forks[3] = Semaphore(1)
        self.forks[4] = Semaphore(1)
        
        self.max_diners = Semaphore(4)
        
        self.exit = False
        
    def philo_action(self, phil_id):
        while self.exit is False:
            self.contemplate()
            self.eat(phil_id)
            
    def contemplate(self):
        sleep_for = random.randint(100, 500) / 1000
        time.sleep(sleep_for)
        
    def eat(self, phil_id):
        self.max_diners.acquire()
        
        self.forks[phil_id].acquire()
        self.forks[(phil_id + 4) % 5].acquire()
        
        print("Philosopher {0} is eating".format(phil_id))
        
        self.forks[phil_id].release()
        self.forks[(phil_id + 4) % 5].release()
    
        self.max_diners.release()
        
        
if __name__ == "__main__":
    problem = DiningPhilosopherProblem()
    philos = list()
    
    for phil_id in range(5):
        philos.append(Thread(target=problem.philo_action, args=(phil_id,)))
        
    for phil in philos:
        phil.start()
        
    time.sleep(6)
    
    problem.exit = True
    
    for phil in philos:
        phil.join()