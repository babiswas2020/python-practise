from multiprocessing import Process,Array,Value

def calc_square(number,result,val):
    for i,j in enumerate(number):
       result[i]=j*j
    val.value=sum(result)

if __name__=="__main__":
   number=[1,2,3,4]
   arr=Array('i',4)
   val=Value('d',0.0)
   p=Process(target=calc_square,args=(number,arr,val))
   p.start()
   p.join()
   print(arr[:])
   print("The value of array sum is "+str(val.value))
