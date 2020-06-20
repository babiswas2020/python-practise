def subsetsum(arr,sum,N):
    if N==0 and sum!=0:
         return False
    elif N==0 and sum==0:
       return True
    if N-1>=0:
       if arr[N-1]<=sum:
          return subsetsum(arr,sum-arr[N-1],N-1) or subsetsum(arr,sum,N-1)
       elif arr[N-1]>sum:
          return subsetsum(arr,sum,N-1)

if __name__=="__main__":
   l=[12,4,6,8,0,23,14]
   print(subsetsum(l,11,7))

        
 