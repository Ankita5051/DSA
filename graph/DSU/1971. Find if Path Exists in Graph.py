class Solution:
    def find(self,x,parent):
        if x==parent[x]:
            return x
        else:
            parent[x]= self.find(parent[x],parent)
            return parent[x]
    def union(self,x,y,parent,rank):
        x_par=self.find(x,parent)
        y_par=self.find(y,parent)
        if x_par==y_par:
            return
        if rank[x_par]>rank[y_par]:
            parent[y_par]=x_par
        elif rank[x_par]<rank[y_par]:
            parent[x_par]=y_par
        else:
            parent[y_par]=x_par
            rank[x_par]+=1
    def validPath(self, n: int, edges: list[list[int]], source: int, destination: int) -> bool:
        parent=[i for i in range(n)]
        rank=[0]*n
        for u,v in edges:
            self.union(u,v,parent,rank)
        return self.find(source,parent)==self.find(destination,parent)
          
        
        