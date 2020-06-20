def knapsack(val,we,N,W):
    arr=[[0 for i in range(W+1)] for i in range(N+1)]
    for i in range(N+1):
       for j in range(W+1):
          if i==0 or j==0:
             arr[i][j]==0
    for i in range(1,N+1):
      for j in range(1,W+1):
         if we[i-1]<=j:
            arr[i][j]=max(val[i-1]+arr[i-1][j-we[i-1]],arr[i-1][j])
         elif we[i-1]>j:
            arr[i][j]=arr[i-1][j]
    return arr[N][W]

if __name__=="__main__":
   val=[60,100,120]
   we=[10,20,30]
   print(knapsack(val,we,3,50))

   
    
