def equalsum(arr,sum,N):
       if sum==0 and (N!=0 or N==0):
           return True
       elif sum!=0 and N==0:
           return False
       if N-1>=0:
          if arr[N-1]<=sum:
             return equalsum(arr,sum-arr[N-1],N-1) or equalsum(arr,sum,N-1)
          elif arr[N-1]>sum:
             return equalsum(arr,sum,N-1)

if __name__=="__main__":
   l=[11,6,2,18,5,8]
   sum=sum(l)
   print(sum)
   if sum%2!=0:
      print(False)
   else:
      sum=sum//2
      print(equalsum(l,sum,6))

     

   
           