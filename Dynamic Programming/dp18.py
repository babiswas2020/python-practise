def longest_substring(arr,brr,m,n):
    result=-1
    mrr=[[-1 for i in range(m+1)] for j in range(n+1)]
    for i in range(n+1):
      for j in range(m+1):
         if i==0 or j==0:
           mrr[i][j]=0
    for i in range(1,n+1):
       for j in range(1,m+1):
          if brr[i-1]==arr[j-1]:
             mrr[i][j]=1+mrr[i-1][j-1]
          else:
             mrr[i][j]=0
          if result<mrr[i][j]:
             result=mrr[i][j]
    return result

if __name__=="__main__":
   print(longest_substring("abstfeglkhgf","andfghfeghjj",len("abstfeglkhgf"),len("andfghfeghjj")))
