# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 14:16:17 2024

@author: hadeer 
"""

### creating thread or two 
from threading import Thread 
def func1(i):
    print("starting thread :",i)
    print("finishing thread :",i)
    
t1=Thread(target=func1, args=(1,))
t1.start()
##two
t2=Thread(target=func1, args=(1,))
t2.start()

#############
'''  Threading using *class* '''
import threading 
class mythread(threading.Thread):
    def __init__(self, i):
        threading.Thread.__init__(self)
        self.i=i
    def run(self):
        print("value send", self.i)
        
thread1=mythread(1)
thread1.start()
##################
''' Multi Threading using classes '''
import threading 
# our thread class 
class MyThread(threading.Thread):
    def __init__(self,x):
        self.__x=x
        threading.Thread.__init__(self)
        
    def run(self):
        print(self.__x)
        
for x in range(10):
    MyThread(x).start()
##############################################
    '''example : showing a number is a prime or not '''
    
import threading
class PrimeNumber(threading.Thread):
    prime_numbers = {} 
    lock = threading.Lock()
    
    def __init__(self, number): 
        threading.Thread.__init__(self) 
        self.Number = number
        PrimeNumber.lock.acquire() 
        PrimeNumber.prime_numbers[number] = "None" 
        PrimeNumber.lock.release() 
 
    def run(self): 
        counter = 2
        res = True
        while counter*counter < self.Number and res: 
            if self.Number % counter == 0: 
               res = False 
            counter += 1 
        PrimeNumber.lock.acquire() 
        PrimeNumber.prime_numbers[self.Number] = res 
        PrimeNumber.lock.release() 
threads = []
while True:
    try:
        input_number = int(input("number: "))
    except ValueError:
        print("Please enter a valid integer.")
        continue

    if input_number < 1:
        break

    thread = PrimeNumber(input_number)
    threads.append(thread)
    thread.start()

for x in threads:
    x.join()

# Print the results
for number, is_prime in PrimeNumber.prime_numbers.items():
    print(f"{number} is a prime number: {is_prime}")
    
    
    
    
        





























