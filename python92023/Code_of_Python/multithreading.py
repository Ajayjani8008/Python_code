import threading
import time
from concurrent.futures import ThreadPoolExecutor

def myfun(s):
    print(f"run my fun for {s}")
    time.sleep(s)
    return s

'''t1=threading.Thread(target=myfun,args=[3])
t2=threading.Thread(target=myfun,args=[2])
t3=threading.Thread(target=myfun,args=[1])

t1.start()
t1.join()
t2.start()
t2.join()
t3.start()
t3.join()'''


def poolingdemo():
    with ThreadPoolExecutor() as executor:
        # future=executor.submit(myfun,s)
        # print(future)
        # time.sleep(s+1)
        # print(future) 
        # print("ajay")
        # print(future.result())
        
        l=[1,2,3,1,3,1]
       
        futures=executor.map(myfun,l)  
        tim1=time.perf_counter()
        for future in futures:
            print(future)
        tim2=time.perf_counter()  
        print(tim2-tim1)  
poolingdemo()