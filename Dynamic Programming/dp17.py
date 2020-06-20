def longest_substring(arr,brr,m,n):
    mrr=[[-1 for i in range(m+1)]for i in range(n+1)]
    for i in range(n+1):
      for j in range(m+1):
        if i==0 or j==0:
          mrr[i][j]=0
    for i in range(1,n+1):
       for j in range(1,m+1):
          if arr[j-1]==brr[i-1]:
             mrr[i][j]=1+mrr[i-1][j-1]
          else:
             mrr[i][j]=0
    return mrr[n][m]

if __name__=="__main__":
   print(longest_substring("ablpkefghnfg","lgabsxefgkghjj",len("ablpkefghnfg"),len("lgabsxefgkghjj")))