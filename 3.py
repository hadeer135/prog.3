from threading import Thread,Event
from time import sleep
def task(event : Event ,id:int):
    print(f'/nThread {id} started ')
    event.wait()
    print(f'nRecived signal . the thread {id} is completed ')
def main()->None:
    event=Event()
    t1=Thread(target=task,args=(event,1))
    t2=Thread(target=task,args=(event,2))

    t1.start()
    t2.start()
    

    print("blocking the main thread for 3 seconds ")
    sleep(3)
    event.set()

