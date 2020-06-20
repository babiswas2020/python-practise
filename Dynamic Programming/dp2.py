arr=[[-1 for i in range(200)] for i in range(200)]

def knapsack(val,we,W,N):
    if N==0 or W==0:
       return 0
    if N-1>=0:
       if arr[N][W]!=-1:
          return arr[N][W]
       else:
          if we[N-1]<=W:
             arr[N][W]=max(val[N-1]+knapsack(val,we,W-we[N-1],N-1),knapsack(val,we,W,N-1))
          elif we[N-1]>W:
             arr[N][W]=knapsack(val,we,W,N-1)
          return arr[N][W]

if __name__=="__main__":
   val=[60,100,120]
   we=[10,20,30]
   print(knapsack(val,we,50,3))

