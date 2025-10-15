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
    def Beauty(self,i,tree,path_pair,V):
        res=0
        que=[i]
        parent=[i for i in range(V+1)]
        rank=[0]*(V+1)
        while que:
            u=que[0]
            que.pop(0)
            for v in tree[u]:
                que.append(v)
                self.union(v,u,parent,rank)
        for u,v in path_pair:
            if self.find(u,parent)==self.find(v,parent):
                res+=1

        return res
    def computeBeauty(self,V,color,edges):
        black_node=[]
        white_node=[]
        for i in range(V):
            if int(color[i])==1:#1:black color   0:white color
                black_node.append(i+1)
            else:
                white_node.append(i+1)
        adj=[[] for _ in range(V+1)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        parof=[-1]*(V+1)

        path_pair=[]
        for u in black_node:
            for v in white_node:
                path_pair.append([u,v])
        
        tree=[[] for _ in range(V+1)]
        que=[1]
        
        

        while que:
            u=que[0]
            que.pop(0)
            for v in adj[u]:
                if parof[v]== -1 and v!=1:
                    parof[v]=u
                    tree[u].append(v)
                    que.append(v)
        res=[]
        for i in range(1,V+1):
            res.append(self.Beauty(i,tree,path_pair,V))

        return res
     

# #beauty of vertex
# v=5
# color="11110" #colors of vertices
# edges=[[3,1],[4,3],[5,3],[2,4]]
# #root node =1


# solve=Solution()
# vertex_beauty=solve.computeBeauty(v,color,edges)
# print("vertex_beauty",vertex_beauty)

        