def equalsum(arr,sum,N):
    if sum==0 and (N==0 or N!=0):
       return 1
    elif N==0 and sum!=0:
       return 0
    if N-1>=0:
       if arr[N-1]<=sum:
        return equalsum(arr,sum-arr[N-1],N-1) +equalsum(arr,sum,N-1)
       else:
        return equalsum(arr,sum,N-1)
      

if __name__=="__main__":
  l=[12,10,6,4,16,18,7]
  print(equalsum(l,9,7))

   
       