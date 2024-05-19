'''This example demonstrates parallel execution of the task function using multiple processes'''

import multiprocessing
import time
def task(number):
    print(f'task {number}started')
    time.sleep(3)
    print(f'task {number}completed')


if __name__=='__main__':
    num_cores=multiprocessing.cpu_count()
    print(f'number of CPU cores is {num_cores} ')

processes=[]
for i in range(num_cores):
    p=multiprocessing.Process(target=task,args=(i,))
    processes.append(p)
    p.start()
for p in processes:
     p.join() #join -> must be out of the loop to let all processes work concurrently 
print("All tasks completed successfully.")

#############################
import multiprocessing  
def print_func(faculity='MNU'):
        print(f"the name of the faculity is{faculity}")

if __name__=='__main__':
        faculities=['GU','ALU','BNU','AUC']
        for faculity in faculities :
            p1=multiprocessing.Process(target=print_func,args=(faculity,))
            p1.start()
            p1.join()
            print("All tasks completed successfully.")

##############################
            ### Queue example 

import multiprocessing
def square_list(mylist,q):
     for num in mylist:
          q.put(num*num)

def print_queue(q):
     print("Queue's elements: ")
     while not q.empty():
          print(q.get())
          print("queue is empty")

if __name__ =='__main__':
     mylist=[1,2,3,4,5]
     q=multiprocessing.Queue()
     p1=multiprocessing.Process(target=square_list,args=( mylist,q))
     p2=multiprocessing.Process(target=print_queue,args=(q))
     p1.start()
     p1.join()
     p2.start()
     p2.join()
########################
     ### PIPE example
import multiprocessing
def sender(conn,msg):
    for msg in msgs:
        conn.send(msg)
        print("the message sent is :".format(msg))
    conn.close()

def reciver(conn):
     while 1:
        msg=conn.recv()
        if msg=='End':
             break
        print("message received is :" .format(msg))
if __name__=='__main__':
     msgs=['hi','helllo','HRU','fine','End']
     parent_conn,child_conn=multiprocessing.Pipe()

     p1=multiprocessing.Process(target=sender,args=(parent_conn,msgs))
     p2=multiprocessing.Process(target=reciver,args=(child_conn,))

     p1.start()
     p1.join()
     p2.start()
     p2.join()


          
         
          
            


