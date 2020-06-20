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
            mrr[i][j]=max(mrr[i][j-1],mrr[i-1][j])
    return mrr

def print_sequence(mrr,arr,brr,m,n):
   i=n
   j=m
   l=[]
   while i>0 or j>0:
      if arr[j-1]==brr[i-1]:
         l.append(arr[j-1])
         i=i-1
         j=j-1
      elif mrr[i-1][j]>mrr[i][j-1]:
         i=i-1
      elif mrr[i-1][j]<=mrr[i][j-1]:
         j=j-1
   return l

if __name__=="__main__":
   arr="alskadeffgjk"
   brr="akjfglkkmbdjiil"
   mrr=longest_subsequence(arr,brr,len(arr),len(brr))
   print(mrr[len(brr)][len(arr)])
   print("Printing the sequence")
   print(''.join(print_sequence(mrr,arr,brr,len(arr),len(brr))[::-1]))





