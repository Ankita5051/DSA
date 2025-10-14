class Solution:
    #dsu
    def find(self,x,parent):
        if x==parent[x]:
            return x
        else:
            parent[x]=self.find(parent[x],parent)
            return parent[x]

    def union(self,x,y,parent,rank):
        x_par=self.find(x,parent)
        y_par=self.find(y,parent)
        if x_par == y_par:
            return 0
        elif rank[x_par]>rank[y_par]:
            parent[y_par]=x_par
        elif rank[y_par]>rank[x_par]:
            parent[x_par]=y_par
        else:
            parent[x_par]=y_par
            rank[y_par]+=1
        return 1

    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        #find number of component
        if len(connections)<n-1:
            return -1
        parent=[i for i in range(n)]
        rank=[0]*n
        component=n
        for edge in connections:
            if self.union(edge[0],edge[1],parent,rank):
                component-=1
        return component-1

        
        