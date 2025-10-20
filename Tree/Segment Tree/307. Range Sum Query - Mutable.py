class NumArray:
    

    def __init__(self, nums: list[int]):
        self.n=len(nums)
        self.arr=nums
        self.segTree=[0]*(4*self.n)
        self.buildSegmentTree(0,0,self.n-1)
        
    def buildSegmentTree(self,i,l,r):
        if l==r:
            self.segTree[i]=self.arr[l]
            return 
        mid=l+(r-l)//2
        self.buildSegmentTree(2*i+1,l,mid)
        self.buildSegmentTree(2*i+2,mid+1,r)
        self.segTree[i]=self.segTree[2*i+1]+self.segTree[2*i+2]
        

    def updateQuery(self,idx,x,i,l,r):
        if r==l:
            self.segTree[i]=x
            return
        mid=l+(r-l)//2
        if idx>mid:
            self.updateQuery(idx,x,2*i+2,mid+1,r)
        else:
            self.updateQuery(idx,x,2*i+1,l,mid)
        self.segTree[i]=self.segTree[2*i+1]+self.segTree[2*i+2]
      

    def queryTree(self,i,l,r,s,e):
        if r<s or l>e:
            return 0
        if r<=e and l>=s:
            return self.segTree[i]
        mid=l+(r-l)//2
        return self.queryTree(2*i+1,l,mid,s,e) + self.queryTree(2*i+2,mid+1,r,s,e)
        


    def update(self, index: int, val: int) -> None:
       self.updateQuery(index,val,0,0,self.n-1) 

    def sumRange(self, left: int, right: int) -> int:
        return self.queryTree(0,0,self.n-1,left,right)
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)