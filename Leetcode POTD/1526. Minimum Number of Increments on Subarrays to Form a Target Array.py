class Solution:
    def minNumberOperations(self, target: list[int]) -> int:
        pre=0
        op=0
        for i in range(len(target)):
            curr=target[i]
            if curr>pre:
                op = op + curr-pre
            pre=curr
        return op
            

        
        