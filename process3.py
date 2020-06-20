from multiprocessing import Process,Queue

def calc_square(number,q):
   for i in number:
      q.put(i*i)

if __name__=="__main__":
   number=[1,2,3,4,5]
   q=Queue()
   p=Process(target=calc_square,args=(number,q,))
   p.start()
   p.join()
   while not q.empty():
       print(q.get())

   
   