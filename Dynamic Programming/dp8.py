brr=[[-1 for i in range(200)] for i in range(200)]

def count_subset(arr,sum,N):
    if N==0 and sum!=0:
       return 0
    elif (N==0 or N!=0) and sum==0:
       return 1
    if N-1>=0:
       if brr[N][sum]!=-1:
          return brr[N][sum]
       else:
          if arr[N-1]<=sum:
             brr[N][sum]=count_subset(arr,sum-arr[N-1],N-1)+count_subset(arr,sum,N-1)
          elif arr[N-1]>sum:
             brr[N][sum]=count_subset(arr,sum,N-1)
          return brr[N][sum]

if __name__=="__main__":
   l=[1,1,2,3,4,5,2]
   print(count_subset(l,5,7))


          
    