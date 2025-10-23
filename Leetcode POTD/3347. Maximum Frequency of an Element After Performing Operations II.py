from collections import defaultdict
class Solution:
    def maxFrequency(self, nums: list[int], k: int, numOperations: int) -> int:
        freq=defaultdict(int)
        afreq=defaultdict(int)
        for i in nums:
            afreq[i]+=1
            freq[i-k]+=1
            freq[i]+=0
            freq[i+k+1]-=1
       
        freq =dict( sorted(freq.items()) )
        keys= list(freq.keys()) 
        for i in range(1,len(freq)):
            freq[keys[i]]+=freq[keys[i-1]]
        vals=list(freq.values())
        res=0
        for i in range(len(freq)):
            target=keys[i]
            total=vals[i]
            target_count=afreq[target]
            needconv= total-target_count
            conv=min(needconv,numOperations)
            res= max(res,conv+target_count)


        return res
           
        