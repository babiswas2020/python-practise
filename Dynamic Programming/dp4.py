def subset_sum(arr,sum,N):
    if N==0 and sum!=0:
       return False
    elif sum==0 and N==0:
       return True
    if N-1>=0:
      if arr[N-1]<=sum:
         return subset_sum(arr,sum-arr[N-1],N-1) or subset_sum(arr,sum,N-1)
      else:
         return subset_sum(arr,sum,N-1)

if __name__=="__main__":
   l=[1,3,23,56,3,67,3,1,1,1]
   print(subset_sum(l,12,10))
   

      