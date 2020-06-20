def subset_sum(arr,sum,N):
    brr=[[False for i in range(sum+1)] for i in range(N+1)]
    for i in range(N+1):
      for j in range(sum+1):
         if (i==0 or i!=0) and j==0:
             brr[i][j]=True
         if i==0 and j!=0:
             brr[i][j]==False
    for i in range(N+1):
       for j in range(sum+1):
          if arr[i-1]<=j:
             brr[i][j]=brr[i-1][j-arr[i-1]] or brr[i-1][j]
          else:
             brr[i][j]=brr[i-1][j]
    return brr[N]

if __name__=="__main__":
   l=[12,11,19,17,5,4]
   sum=sum(l)
   crr=subset_sum(l,sum,6)
   crr=crr[:sum//2]
   min=sum+1
   temp=0
   for i,j in enumerate(crr):
      if j==True:
         temp=sum-2*(i)
      if min>temp:
         min=temp
   print(min)






            

     