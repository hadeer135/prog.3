# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import threading
import time 

def print_time(threadName , delay ):
    count=0
    while count < 3:
        time.sleep(delay)
        count+=1
        print(threadName , "----------" , time.ctime())
        
        
        
 #creating t1 , t2 two threads -> objects of the thread class        
t1=threading.Thread( target=print_time , args =("Thread 1" ,4 ))
t2=threading.Thread( target=print_time , args =("Thread 2" , 4))

# starting thread1
t1.start()
# starting thread2
t2.start()
# wait until thread 1 is executed competely

# wait until thread 1 is executed competely

print("done ")


#########################


import threading
import time

def print_square(num):
    print("square :{}". format(num*num))

def print_cupe(num):
    print(" cube : {}".format(num*num*num))

t1=threading.Thread(target=print_square,args=(10,))
t2=threading.Thread(target=print_cupe,args=(5,))
t1.start()
t2.start()
t1.join()
t1.join()
print("done !")
