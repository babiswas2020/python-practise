def longest_substring(arr,brr,m,n,count):
    if m==0 and n==0:
       return 0
    if m-1>=0 and n-1>=0:
       if arr[m-1]==brr[n-1]:
          count[0]=1+longest_substring(arr,brr,m-1,n-1,count)
       else:
          count[0]=max(count[0],max(longest_substring(arr,brr,m-1,n,count),longest_substring(arr,brr,m,n-1,count)))
       return count[0]

if __name__=="__main__":
   count=[0]
   print(longest_substring("abcdefglkqqq","abxefglkks",len("abcdefglkqqq"),len("abxefglkks"),0))
