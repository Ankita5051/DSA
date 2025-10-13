"""check if there is any cycle in the undirected graph."""
class Solution:
    def find(self,x,parent):
        if x==parent[x]:
            return x
        else:
            parent[x]=self.find(parent[x],parent)
            return parent[x]
    def union(self,x:int,y:int,parent:list,rank):
        x_par=self.find(x,parent)
        y_par=self.find(y,parent)
        if x_par == y_par:
            return True
        if rank[x_par]>rank[y_par]:
            parent[y_par]=x_par
        elif rank[x_par]<rank[y_par]:
            parent[x_par]=y_par
        else:
            parent[x_par]=y_par
            rank[y_par]+=1
        return False

    #Function to detect cycle using DSU in an undirected graph.
    def detectCycle(self, V, adj):
        rank=[0]*V
        parent=[i for i in range(V)]

        for u in range(V):
            for v in adj[u]:
                if u<v and self.union(u,v,parent,rank):
                    return 1
                    
        return 0
    
