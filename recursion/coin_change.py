'''Given an integer array coins[ ] representing different denominations of currency and an integer sum, find the number of ways you can make sum by using different combinations from coins[ ]. 
Note: Assume that you have an infinite supply of each type of coin. Therefore, you can use any coin as many times as you want.'''

class solution:
    def __init__(self,coins,sum):
        self.coins=coins
        self.sum=sum
    
    def Byrecusion(self):
        def countR(coin,n,sum):
            if sum ==0:
                return 1
            elif n==0 or sum<0:
                return 0
            
            return countR(coin,n,sum-coin[n-1])+countR(coin,n-1,sum)
        
        res= countR(self.coins,len(self.coins),self.sum)
        return res
    def ByMemo(self):
        def countR(coins,n,sum,memo):
            if sum==0:
                return 1
            