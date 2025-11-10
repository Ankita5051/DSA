#google

#using DFS and BFS
class Solution:
    def __init__(self):
        self.dir=[(1,0),(-1,0),(0,1),(0,-1)]
    def perimeter(self,grid,i,j):
        if i<0 or j<0 or i>=len(grid) or j>= len(grid[0]) or grid[i][j]==0:
            
            return 1
        if grid[i][j]==-1:
            return 0

        grid[i][j] =-1
        return self.perimeter(grid,i-1,j) + self.perimeter(grid,i+1,j) + self.perimeter(grid,i,j-1) + self.perimeter(grid,i,j+1)
    

    def BFS(self,grid,i,j):
        n=len(grid)
        m=len(grid[0])
        q=[(i,j)]
        grid[i][j]=-1
        res=0
        while q:
            x,y=q[0]
            q.pop(0)
            for i,j in self.dir:
           
                if x+i>=n or y+j>=m or y+j<0 or x+i<0 or grid[x+i][y+j]==0:
                    res+=1
                elif grid[x+i][y+j]==-1:
                    continue
                else:
                    grid[x+i][y+j]=-1
                    q.append((x+i,y+j))
        return res
    
    
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    return self.perimeter(grid,i,j)
        return -1