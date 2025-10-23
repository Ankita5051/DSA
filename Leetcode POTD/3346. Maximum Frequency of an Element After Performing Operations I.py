class Solution:
    def maxFrequency(self, nums: list[int], k: int, numOperations: int) -> int:
        maxel=max(nums)+1+k
        freq=[0]*maxel
        for i in nums:
            freq[i]+=1
      
        #cumulative sum
        for i in range(1,maxel):
            freq[i] +=freq[i-1]
        
        res=0
        for target in range(maxel):
            if freq[target]==0:
                continue
            l= max(0,target-k)
            r=min(target+k,maxel-1)
          
            freq_count=freq[r] - (freq[l-1] if l>0 else 0)
            target_count=freq[target]- (freq[target-1] if target>0 else 0)
            need_conv= freq_count - target_count
            conv=min(need_conv,numOperations)
           
            res=max(res,target_count+conv)
        return res
        