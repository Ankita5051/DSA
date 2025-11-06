class Solution:
    def __init__(self):
        self.memo=[[-1 for _ in range(2501)]for j in range(2501)]
    def LISmemo(self,nums,i,prev):
        if i>=len(nums):
            return 0
        if prev!=-1 and self.memo[i][prev]!=-1:
            return self.memo[i][prev]
        #take
        take=0
        if prev==-1 or nums[i]>nums[prev]:
            take= 1+self.LISmemo(nums,i+1,i)
            
        skip=self.LISmemo(nums,i+1,prev)
        self.memo[i][prev]= max(take,skip)
        return self.memo[i][prev]
    
    def LISrec(self,nums,i,prev):
        if i>=len(nums):
            return 0
        #take
        take=0
        if prev==-1 or nums[i]>nums[prev]:
            take= 1+self.LISrec(nums,i+1,i)
            
        skip=self.LISrec(nums,i+1,prev)
        return max(take,skip)

    def lengthOfLIS(self, nums: list[int]) -> int:
        return self.LISrec(nums,0,-1)
        