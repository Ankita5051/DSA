class Solution:
    def BFS(self,u,adj,visited):
        que=[]
        que.append((u,-1))
        visited[u]=True
        
        while que:
            u,p=que[0]
            que.pop(0)
            for v in adj[u]:
                if visited[v]==True and v!=p:
                    return True
                elif visited[v]==False:
                    visited[v]=True
                    que.append((v,u))
                
        return False
    def isCycle(self, V, edges):
        #Code here
        adj=[[] for _ in range(V)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited=[False]*V
      
        for v in range(V):
            
            if visited[v]== False and self.BFS(v,adj,visited):
                return True
        return False
        
    
        