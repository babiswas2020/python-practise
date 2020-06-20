def subset_sum(arr,sum,N):
    brr=[[False for i in range(sum+1)] for i in range(N+1)]
    for i in range(N+1):
       for j in range(sum+1):
          if i==0 and j!=0:
            brr[i][j]==False
          if (i==0 or i!=0) and j==0:
            brr[i][j]=True
    for i in range(1,N+1):
      for j in range(1,sum+1):
         if arr[i-1]<=j:
           brr[i][j]=brr[i-1][j-arr[i-1]] or brr[i-1][j]
         elif arr[i-1]>j:
           brr[i][j]=brr[i-1][j]
    return brr[N]

def min_diff(arr,sm,N):
    crr=subset_sum(arr,sm,N)
    l=len(crr)//2
    if l>=0:
       brr=crr[:l]
       brr=[i for i,j in enumerate(brr) if j==True]
       return sum(arr)-2*max(arr)
    

if __name__=="__main__":
   arr=[1,6,11,5]
   print(min_diff(arr,sum(arr),4))
   
   