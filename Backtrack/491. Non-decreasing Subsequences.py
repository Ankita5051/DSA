class Solution:
    def backtrack(self,arr,i,res,seq):
        if i==len(arr):
            if len(seq)>1 and seq not in res:
                res.append(seq)
            return
           
        seq1=[j for j in seq]
        print(i,seq)
        if not seq or arr[i] >= seq[-1]:
            seq.append(arr[i])
            self.backtrack(arr,i+1,res,seq)
        self.backtrack(arr,i+1,res,seq1)
        return
        

            

    def findSubsequences(self, nums: list[int]) -> list[list[int]]:
        res=[]
        self.backtrack(nums,0,res,[])
        return res
        