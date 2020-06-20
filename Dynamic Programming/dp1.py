def knapsack(val,we,W,N):
    if N==0 or W==0:
       return 0
    if N-1>=0:
       if we[N-1]<=W:
          return max(val[N-1]+knapsack(val,we,W-we[N-1],N-1),knapsack(val,we,W,N-1))
       elif we[N-1]>W:
          return knapsack(val,we,W,N-1)

if __name__=="__main__":
   val=[60,100,120]
   we=[10,20,30]
   print(knapsack(val,we,50,3))


          