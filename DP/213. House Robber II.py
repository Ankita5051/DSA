class Solution:
    def __init__(self):
        self.memo=[-1]*101

    def rec(self,nums,i):
        if i>= len(nums):
            return 0
        if self.memo[i]!=-1:

            return self.memo[i]
        #take
        take = nums[i]+self.rec(nums,i+2)
        #skip
        skip = self.rec(nums,i+1)
        self.memo[i]= max(take,skip)
        return self.memo[i]
    
    def rob(self, nums: list[int]) -> int:
        if len(nums)==1:
            return nums[0]
        case1=self.rec(nums,1)
        nums.pop()
        self.memo[:]=[-1]*101
        case2=self.rec(nums,0)
        return max(case1,case2)
        