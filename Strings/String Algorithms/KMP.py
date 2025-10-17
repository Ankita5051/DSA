class Solution:
    def computeLPS(self,pat,lps):
        m=len(pat)
        i=1
        lps[0]=0
        length=0 #prefix length till now
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
                
    
    def search(self, pat, txt):
        # code here
        n=len(txt)
        m=len(pat)
        res=[]
        #lps arr 
        #LPS[i] longest proper prifix of pat[0..i] which is laos a proper suffix
        lps=[0]*m
        self.computeLPS(pat,lps)
        i=0
        j=0
        
        while i<n:
            if txt[i]==pat[j]:
                j+=1
                i+=1
                if j==m:#matching found
                    res.append(i-j)
                    j=lps[j-1]
            else:
                if j!=0:
                    j=lps[j-1]
                else:
                    i+=1
        return res
        
        
        