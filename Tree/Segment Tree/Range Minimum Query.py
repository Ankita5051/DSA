def buildtree(i,l,r,tree,arr):
    if l==r:
        tree[i]=arr[l]
        return
    mid=l+(r-l)//2
    left=2*i+1
    right=left+1
    buildtree(left,l,mid,tree,arr)
    buildtree(right,mid+1,r,tree,arr)
    tree[i]=min(tree[left],tree[right])
    
def constructST(arr, n):
    segtree=[0]*(4*n)
    buildtree(0,0,n-1,segtree,arr)
    return segtree
def query(tree,i,l,r,qs,qe):
    #case -1 
    if qe<l or qs>r:
        return float('inf')
    #case 2 
    if qs<=l and qe>=r:
        return tree[i]
    else:
        #case-3
        mid=l+(r-l)//2
        return min(query(tree,2*i+1,l,mid,qs,qe),query(tree,2*i+2,mid+1,r,qs,qe))

def RMQ(st, n, qs, qe):
    return query(st,0,0,n-1,qs,qe)
   