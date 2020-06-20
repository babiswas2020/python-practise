arr=[[-1 for i in range(200)] for i in range(200)]
def knapsack(val,we,N,W):
    if N==0 or W==0:
       return 0
    if N-1>=0:
       if we[N-1]<=W:
          if arr[N-1][W]!=-1:
             return arr[N-1][W]
          else:
             arr[N-1][W]=max(val[N-1]+knapsack(val,we,N-1,W-we[N-1]),knapsack(val,we,N-1,W))
             return arr[N-1][W]
       elif we[N-1]>W:
          if arr[N-1][W]!=-1:
             return arr[N-1][W]
          else:
             arr[N-1][W]=knapsack(val,we,N-1,W)
             return arr[N-1][W]

if __name__=="__main__":
   val=[60,100,120]
   we=[10,20,30]
   print(knapsack(val,we,3,50))

