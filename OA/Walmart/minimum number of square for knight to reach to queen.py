class Solution:
    def __init__(self):
        self.dir=[(-2,-1),(2,1),(2,-1),(-2,1),(1,2),(1,-2),(-1,2),(-1,-2)]
    def rec(self,n,i,j,dx,dy):
        if i>=n or j>=n:#out of bond
            return 0
        if dx==0 and dy==0:
            return 1
        res=int('inf')
        for d in self.dir:
            x,y=d
            res= min(res,1+ self.rec(n,i+x,j+y,dx+x,dy+y))
        return res




    def minSquare(self,n,qx,qy,kx,ky)->int:
        dx=qx-kx
        dy=qy-ky
        steps=self.rec(n,kx,ky,dx,dy)
        square= steps*3-1
        return square