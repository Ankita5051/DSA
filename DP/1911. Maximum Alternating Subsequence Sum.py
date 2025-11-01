class Solution:
    def __init__(self):
        self.memo=[[-1,-1] for _ in range(100001)]
    def rec(self,nums,i,idx):
        if i>=len(nums):
            return 0
        if self.memo[i][idx]!=-1:
            return self.memo[i][idx]
        #take
        take=0
        if idx:#odd
            take=self.rec(nums,i+1,0) - nums[i]
        else:#even
            take= self.rec(nums,i+1,1) + nums[i]
        #skip
        skip=self.rec(nums,i+1,idx)
        self.memo[i][idx]= max(take,skip)
        return self.memo[i][idx]
 

    def dp(self, nums) -> int:
        n=len(nums)
        dp=[[0,0] for _ in range(n+1)]
      
        for i in range(1,n+1):
           
            dp[i][0]= max(dp[i-1][0], dp[i-1][1]+nums[i-1])
            dp[i][1]=max(dp[i-1][1] , dp[i-1][0] - nums[i-1])
           

        return max(dp[-1][0],dp[-1][1])
            

    def maxAlternatingSum(self, nums: list[int]) -> int:
        return self.rec(nums,0,0)
