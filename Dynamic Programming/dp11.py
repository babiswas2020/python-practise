def l_c_s(arr,brr,n,m):
    if n==0 or m==0:
       return 0
    if m-1>=0 and n-1>=0:
        if arr[n-1]==brr[m-1]:
            return 1+l_c_s(arr,brr,n-1,m-1)
        else:
            return max(l_c_s(arr,brr,n-1,m),l_c_s(arr,brr,n,m-1))

if __name__=="__main__":
   print(l_c_s("abdertab","abceghsdekllas",len("abdertab"),len("abceghsdekllas")))
   
   