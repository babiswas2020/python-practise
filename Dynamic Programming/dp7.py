def count_subset(arr,sum,N):
    if N==0 and sum!=0:
       return 0
    elif (N==0 or N!=0) and sum==0:
       return 1
    if N-1>=0:
       if arr[N-1]>=0:
          return count_subset(arr,sum-arr[N-1],N-1) + count_subset(arr,sum,N-1)
       else:
          return count_subset(arr,sum,N-1)

if __name__=="__main__":
   arr=[1,2,3,1,1,2,5,3,4]
   print(count_subset(arr,5,9))

