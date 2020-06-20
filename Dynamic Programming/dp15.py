def l_c_s(arr,crr,n,m):
   brr=[[-1 for i in range(n+1)] for i in range(m+1)]
   for i in range(m+1):
      for j in range(n+1):
         if i==0 or j==0:
            brr[i][j]=0
   print(brr)
   for i in range(1,m+1):
      for j in range(1,n+1):
             if arr[j-1]==crr[i-1]:
                brr[i][j]=1+brr[i-1][j-1]
             else:
                brr[i][j]=max(brr[i][j-1],brr[i-1][j])
   print(brr)
   return brr[m][n]
                
    

if __name__=="__main__":
   print(l_c_s("abdertab","abceghsdekllas",len("abdertab"),len("abceghsdekllas")))