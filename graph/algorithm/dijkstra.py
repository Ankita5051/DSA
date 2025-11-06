import heapq
class Solution:
  
    def dijkstra(self, V, edges, src):
        # code here
        pq=[]
        heapq.heappush(pq,(0,src))
        INF=float('inf')
        result=[INF for _ in range(V)]
        result[src]=0
    
        adj=[[] for _ in range(V)]
        for u,v,w in edges:
            adj[u].append((v,w))
        
        
        while pq:
            d,u=heapq.heappop(pq)
         
            for node in adj[u]:
                v=node[0]
                w=node[1]
                if d+w < result[v]:
                    result[v]=d+w
                    heapq.heappush(pq,(d+w,v))
                
        return result
        
        