class Solution:
    def find(self,x,parent):
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
        elif rank[x_par]>rank[y_par]:
            parent[y_par]=x_par
        elif rank[x_par]<rank[y_par]:
            parent[x_par]=y_par
        else:
            parent[x_par]=y_par
            rank[y_par]+=1


    def equationsPossible(self, equations: List[str]) -> bool:
        parent=[i for i in range(26)]
        rank=[0]*26
        for eq in equations:
            if eq[1]=='=':
                self.union(ord(eq[0])-97,ord(eq[3])-97,parent,rank)
        for eq in equations:
            if eq[1]=='!' and self.find(ord(eq[0])-97,parent)==self.find(ord(eq[3])-97,parent):
                return False
        return True


        