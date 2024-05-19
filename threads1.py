# -*- coding: utf-8 -*-
"""
Created on Mon Feb 26 20:30:59 2024

@author: hadeer
"""

import threading 
from time import sleep,ctime 
 
def loop0():
    print("start loop0 at time:" ,ctime )
    sleep(4)
    print("done loop0 at time:" ,ctime )
def loop1():
    print("start loop01 at time:" ,ctime )
    sleep(2)
    print("done loop1 at time:" ,ctime )
    
if __name__ =='__main__':
    print("main program starts at time :",ctime)
    threading.Thread(target=loop0).start()
    threading.Thread(target=loop1).start()
    sleep(1)
    print("done program at time :" ,ctime )


###############################################
    


