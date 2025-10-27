class Solution:
    def solve(self,arr,idx,p,memo):
        if idx>=len(arr):
            return 0
        if p!=-1 and memo[idx][p]!=-1:
            return memo[idx][p]
        take=0
       
        if p==-1 or self.isPredecessor(arr[p],arr[idx]):
            #take
            take=1+self.solve(arr,idx+1,idx,memo)

        skip=self.solve(arr,idx+1,p,memo)
        memo[idx][p]=max(take,skip)
        return memo[idx][p]

    def isPredecessor(self,w1,w2):
   
        if (len(w1)+1) != len(w2):
          
            return False
        flag=True
        j=0
        i=0
        while i<len(w1) and j<len(w2):
            if w1[i]==w2[j]:
                i+=1
            j+=1
        return True if i==len(w1) else False
     

    def longestStrChain(self, words: list[str]) -> int:
        words=sorted(words,key= lambda x: len(x)) 
        memo=[[-1 for _ in range(len(words))]for _ in range(len(words))]
        res=self.solve(words,0,-1,memo)
    
        return res