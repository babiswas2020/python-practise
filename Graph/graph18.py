def stepping_num(n,m,num):
    queue=[]
    queue.append(num)
    while queue:
        number=queue.pop(0)
        if number>=n and number<=m:
           print(number)
        if number<n or number>m:
           continue
        num1=number%10
        number1=number*10+(num1+1)
        number2=number*10+(num1-1)
        if num1==0:
           queue.append(number1)
        elif num1==9:
           queue.append(number2)
        else:
           queue.append(number1)
           queue.append(number2)

def display(n,m):
   for i in range(n,m):
      stepping_num(n,m,i)
            
if __name__=="__main__":
   display(10,15)


   
   

       