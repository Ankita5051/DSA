class Solution:
    def DFS(self,u,adj,visited,parent):
        visited[u]=True
        for v in adj[u]:
            if visited[v]==True and v!=parent:
                return True
            elif visited[v]==False and self.DFS(v,adj,visited,u):
                return True
        return False
    def isCycle(self, V, edges):
        #Code here
        adj=[[] for _ in range(V)]
        for u,v in edges:
            adj[u].append(v)
            adj[v].append(u)
        visited=[False]*V
      
        for v in range(V):
            
            if visited[v]== False and self.DFS(v,adj,visited,-1):
                return True
        return False
        
    
        