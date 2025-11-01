class Solution:
    def __init__(self):
        self.memo=[-1]*101
    #by recurssion
    def rec(self,nums,i):
        if i>=len(nums):
            return 0
        #take curr
        take= nums[i] + self.rec(nums,i+2)
        #skip curr
        skip= self.rec(nums,i+1)

        return max(take,skip)

    #by memorisation
    def memorisation(self,nums,i):
        if i>=len(nums):
            return 0
        if self.memo[i]!=-1:
            return self.memo[i]
        #take curr
        take= nums[i] + self.memorisation(nums,i+2)
        #skip curr
        skip= self.memorisation(nums,i+1)

        self.memo[i]= max(take,skip)
        return self.memo[i]
    
    #by dp
    def dp(self, nums: list[int]) -> int:
        n=len(nums)
        if n==1:
            return nums[0]
        dp=[0]*(n+1)
        dp[1]=nums[0]
   
        for i in range(2,n+1):
            dp[i]=max(dp[i-1],nums[i-1]+dp[i-2]) #maximum money you can rob up to house i
   
        return dp[-1]
        
      
        


    def rob(self, nums: list[int]) -> int:
        return self.rec(nums,0)
        