def knapsack(val,we,W,N):
    brr=[[0 for i in range(W+1)] for i in range(N+1)]
    for i in range(N+1):
       for j in range(W+1):
          if i==0 or j==0:
             brr[i][j]==0
    for i in range(1,N+1):
       for j in range(1,W+1):
          if we[i-1]<=j:
             brr[i][j]=max(val[i-1]+brr[i-1][j-we[i-1]],brr[i-1][j])
          elif we[i-1]>j:
             brr[i][j]=brr[i-1][j]
    return brr[N][W]

if __name__=="__main__":
   val=[60,100,120]
   we=[10,20,30]
   W=50
   print(knapsack(val,we,50,3))



          