'''Given an array of positive integers arr[] and a value sum, determine if there is a subset of arr[] with sum equal to given sum.'''

class Solution:
    def __init__(self,arr,target):
        self.arr=arr
        
    def isSubset(self,target):
        def check(sum,n,arr):
            if sum==0:
                return True
            elif sum<0 or n==0:
                return False
            
            #take skip
            return check(sum-arr[n-1],n-1,self.arr) or check(sum,n-1,self.arr)
        
        return check(target,len(self.arr),self.arr)