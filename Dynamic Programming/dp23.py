def longest_subsequence(arr,brr,m,n):
    mrr=[[-1 for i in range(m+1)] for j in range(n+1)]
    for i in range(n+1):
       for j in range(m+1):
         if i==0 or j==0:
            mrr[i][j]=0
    for i in range(1,n+1):
      for j in range(1,m+1):
         if arr[j-1]==brr[i-1]:
            mrr[i][j]=1+mrr[i-1][j-1]
         else:
            mrr[i][j]=max(mrr[i-1][j],mrr[i][j-1])
    return mrr[n][m]

if __name__=="__main__":
   arr="ADXCPY"
   brr="AXY"
   k=longest_subsequence(arr,brr,len(arr),len(brr))
   if min(len(arr),len(brr))==k:
      print(True)
   else:
      print(False)