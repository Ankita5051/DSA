import math
class Solution:
    def isprime(self,num):
        n=0
        for i in num:
            n = 2*n + int(i)
        if n<=1:
            return -1
        for i in range(2, math.isqrt(n) + 1):
            if n%i == 0:
                return -1
        return n


    def solve(self,nums,arr,n):
    
        if n==0:
            return self.isprime(nums)    
        seq1=self.solve(arr[n-1]+nums,arr,n-1)
        seq2=self.solve(nums,arr,n-1)
        return max(seq1,seq2)


# string="101101"
# solve("",string,len(string))