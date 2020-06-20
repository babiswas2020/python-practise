def subsetsum(arr,sum,N):
   brr=[[False for i in range(sum+1)]for i in range(N+1)]
   for i in range(N+1):
     for j in range(sum+1):
         if i==0 and j!=0:
           brr[i][j]=False
         if (i==0 or i!=0) and j==0:
            brr[i][j]=True
   for i in range(1,N+1):
      for j in range(1,sum+1):
          if arr[i-1]<=j:
             brr[i][j]=(brr[i-1][j-arr[i-1]]) or (brr[i-1][j])
          elif arr[i-1]>j:
             brr[i][j]=(brr[i-1][j])
   return brr[N][sum]

if __name__=="__main__":
   l=[5,12,9,3,6]
   print(subsetsum(l,10,5))

           
         
      
   