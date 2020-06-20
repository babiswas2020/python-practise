def subset_sum(arr,sum,N):
   brr=[[False for i in range(sum+1)] for i in range(N+1)]
   for i in range(N+1):
      for j in range(sum+1):
         if i==0 and j!=0:
            brr[i][j]=False
         if (i==0 or i!=0) and j==0:
            brr[i][j]=True
   for i in range(1,N+1):
      for j in range(1,sum+1):
          if arr[i-1]<=j:
             brr[i][j]=brr[i-1][j-arr[i-1]] or brr[i-1][j]
          elif arr[i-1]>j:
             brr[i][j]=brr[i-1][j]
   return brr[N][sum]

def equal_sum_partition(arr,sum,N):
    rem=sum%2
    sum=sum//2
    if rem!=0:
       return False
    else:
       return subset_sum(arr,sum,N)
       
if __name__=="__main__":
   arr=[1,1,2,4,5,6,8,7]
   sum=sum(arr)
   print(equal_sum_partition(arr,sum,8))

   
   
    
    