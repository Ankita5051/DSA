import math
def isprime(num):
    if num<=1:
        return -1
    for i in range(2, math.isqrt(num) + 1):
        if num%i == 0:
            return -1
    return num


def solve(nums,n,arr,memo):
    if memo[nums]!=0:
        return memo[nums]
    if n==len(arr):
        memo[nums]= isprime(nums)
        return memo[nums] 
     
    nn=int(arr[n])+ 2*nums
    seq1=solve(nn,n+1,arr,memo)
    seq2=solve(nums,n+1,arr,memo)
    memo[nums]= max(seq1,seq2)
    return memo[nums]


# string="1001"
# n=len(string)
# memo=[0 for i in range(2**n)]
# solve(int(string[-1]),string,len(string),memo)