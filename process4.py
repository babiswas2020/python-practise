from multiprocessing import Process,Value,Lock

def deposit(amount,balance,lock):
    lock.acquire()
    balance.value+=amount
    lock.release()

def withdraw(amount,balance,lock):
    lock.acquire()
    balance.value-=amount
    lock.release()

if __name__=="__main__":
   balance=Value('i',200)
   l=Lock()
   p1=Process(target=deposit,args=(2,balance,l,))
   p2=Process(target=withdraw,args=(1,balance,l,))
   p1.start()
   p2.start()
   p1.join()
   p2.join()
   print(balance.value)

   

    
   