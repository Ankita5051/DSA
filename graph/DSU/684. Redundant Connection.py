class Solution:
    def find(self,x,parent):
        if parent[x]==x:
            return x
        else:
            parent[x]=self.find(parent[x],parent)
            return parent[x]
    def union(self,x,y,parent,rank):
        x_par=self.find(x,parent)
        y_par=self.find(y,parent)
        if x_par==y_par:
            return True
        if rank[x_par]>rank[y_par]:
            parent[y_par]=x_par
        elif rank[x_par]<rank[y_par]:
            parent[x_par]=y_par
        else:
            rank[x_par]+=1
            parent[y_par]=x_par
        return False

    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        parent=[i for i in range(len(edges)+1)]
        rank=[0]*len(parent)
        for u,v in edges:
            if self.union(u,v,parent,rank):
                return [u,v]

    
        