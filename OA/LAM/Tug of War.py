# arr[L..R]
# length = R-L+1 must be even
# Let mid = (L+R)/2
# sum(L..mid) == sum(mid+1..R)

def solve(weights):
    wt=list(map(int,weights))
    n=len(wt)
    print(wt)
    pre_sum=[0]*(n+1)

    for i in range(n):
        pre_sum[i+1]=pre_sum[i]+ wt[i]
    print(pre_sum)
    ln=0
    l=0
    r=-1

    for i in range(n):
        for j in range(i+1,n,2):
            length=j-i+1
            mid=(i+j)//2
            l_sum=pre_sum[mid+1] -pre_sum[i]
            r_sum=pre_sum[j+1]-pre_sum[mid+1]
            
            if l_sum==r_sum:
                print(i,j,l_sum,r_sum,ln,length)
                if length > ln:
                    print(ln)
                    ln=length
                    l=i
                    r=j
    if ln==0:
        print(0)
    res=[wt[i] for i in range(l,r+1)]
    print(res,r-l+1)
we="145664852"
solve(we)