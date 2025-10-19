class Solution:
    def buildTree(self,i,l,r,arr,tree):
        if l==r:
            tree[i]=arr[l]
            return
        mid=(l+r)//2
     
        self.buildTree(2*i+1,l,mid,arr,tree)
        self.buildTree(2*i+2,mid+1,r,arr,tree)
        
        tree[i]=tree[2*i+1]+tree[2*i+2]
        
    def query(self,i,l,r,start,end,tree):
        
        #case 1
        if r<start or l>end:
            return 0
        #case 2 inside range
        elif l>=start and r<=end:
            return tree[i]
        else:#case 3 overlappting
            mid=l+(r-l)//2
            return self.query(2*i+1,l,mid,start,end,tree)+self.query(2*i+2,mid+1,r,start,end,tree)
            
        
    def querySum(self, n, arr, q, queries):
        # code here
        segTree=[0]*(4*n)
        self.buildTree(0,0,n-1,arr,segTree)
       
        res=[]
        
        for i in range(0,len(queries),2):
            start=queries[i]
            end=queries[i+1]
            res.append(self.query(0,0,n-1,start-1,end-1,segTree))
        
        return res
        
        #can be solved via prefix sum