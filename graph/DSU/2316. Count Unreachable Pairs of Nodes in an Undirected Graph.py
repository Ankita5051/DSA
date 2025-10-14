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
        if rank[x_par]>rank[y_par]:
            parent[y_par]=x_par
        elif rank[y_par]>rank[x_par]:
            parent[x_par]=y_par
        else:
            parent[x_par]=y_par
            rank[y_par]+=1
        

    def countPairs(self, n: int, edges: list[list[int]]) -> int:
        #res+= size*(remaining_noes - size)
        parent=[i for i in range(n)]
        rank=[0]*n
        for edge in edges:
            self.union(edge[0],edge[1],parent,rank)
        component={}#component_parent:size
        for i in range(n):
            p=self.find(i,parent)
            if p in component:
                component[p]+=1
            else:
                component[p]=1
        res=0
        r_n=n
        for comp,size in component.items():
            res+= size*(r_n - size)
            r_n-=size
        return res


        