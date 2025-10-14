class Solution:
    def find(self,x,parent)->int:
        if x==parent[x]:
            return x
        else:
            parent[x]=self.find(parent[x],parent)
            return parent[x]
    def union(self,x,y,parent,rank):
        x_par=self.find(x,parent)
        y_par=self.find(y,parent)

        if x_par==y_par:
            return
        if rank[x_par]>rank[y_par]:
            parent[y_par]=x_par
        elif rank[y_par]>rank[x_par]:
            parent[x_par]=y_par
        elif x_par<y_par:
            parent[y_par]=x_par
            x_par+=1
        else:
            parent[x_par]=y_par
            y_par+=1


    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent=[i for i in range(26)]
        rank=[0]*26
        for ch1,ch2 in zip(s1,s2):
            self.union(ord(ch1)-97,ord(ch2)-97,parent,rank)
        res=[]
        for ch in baseStr:
            ch_pr=self.find(ord(ch)-97,parent)
            res.append(chr(ch_pr+97))
        return ''.join(res)


        