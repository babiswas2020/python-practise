def equalsum(arr,sum,N):
    brr=[[0 for i in range(sum+1)] for j in range(N+1)]
    for i in range(N+1):
      for j in range(sum+1):
        if(i==0 and j!=0):
           brr[i][j]==0
        if (i==0 or i!=0) and j==0:
           brr[i][j]=1
    for i in range(1,N+1):
       for j in range(1,sum+1):
          if arr[i-1]<=j:
             brr[i][j]=brr[i-1][j-arr[i-1]] +brr[i-1][j]
          else:
             brr[i][j]=brr[i-1][j]

    return brr[N][sum]

if __name__=="__main__":
   l=[12,111,13,8,9]
   print(equalsum(l,11,5))



         
       
    