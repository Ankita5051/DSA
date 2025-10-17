import bisect
class Solution:
    def computeLPS(self,pat,lps):
        m=len(pat)
        i=1
        
        length=0#prefix length till now
        while i<m:
            
            if pat[i]==pat[length]:
                length+=1
                lps[i]=length
                i+=1
            else:
                if length!=0:
                    length-=1
                else:
                    lps[i]=0
                    i+=1
    def KMP(self,txt,pat,idx):
        m=len(pat)
        n=len(txt)
        lps=[0]*m
        self.computeLPS(pat,lps)

        i=0
        j=0
        while i<n:
            if txt[i]==pat[j]:
                i+=1
                j+=1
                if j==m:
                    #one matched found
                    idx.append(i-j)
                    j=lps[j-1]
            else:
                if j!=0:
                    j=lps[j-1]  
                else:
                    i+=1
    def beautifulIndices(self, s: str, a: str, b: str, k: int) -> list[int]:
        n=len(s)
        
        a_idx=[]
        b_idx=[]
        self.KMP(s,a,a_idx)#gives already sorted index
        self.KMP(s,b,b_idx)#gives already sorted index
        res=[]
        
        for i in a_idx:
            left_limit=max(0,i-k)
            right_limit=min(n-1,i+k)
            t=bisect.bisect_left(b_idx,left_limit)
        
            if t!=len(b_idx) and b_idx[t]<=right_limit:
                res.append(i)
        
        return res

        