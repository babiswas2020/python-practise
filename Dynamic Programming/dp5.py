brr=[[False for i in range(100)] for i in range(100)]
def subset_sum(arr,sum,N):
    if N==0 and sum!=0:
       return False
    elif (N==0 or N!=0) and sum==0:
       return True
    if N-1>=0:
       if brr[N][sum]!=False:
          return True
       else:
         if arr[N-1]<=sum:
            brr[N][sum]=subset_sum(arr,sum-arr[N-1],N-1) or subset_sum(arr,sum,N-1)
         else:
            brr[N][sum]=subset_sum(arr,sum,N-1)
         return brr[N][sum]

if __name__=="__main__":
   l=[1,2,3,3,1,3]
   print(subset_sum(l,5,6))
