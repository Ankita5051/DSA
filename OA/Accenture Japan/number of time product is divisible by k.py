from collections import Counter
def prime_factor(n):
    cnt_pf=Counter()
    i=2
    while i*i<=n:
        while n%i==0:
            cnt_pf[i]+=1
            n//=i
        i+=1
    if n>1:
        cnt_pf[n]+=1
    return cnt_pf

def count_divn(arr,k):
    pf=prime_factor(k)
    mp=Counter()
    for i in arr:
        for p in pf:
            while i%p==0:
                mp[p]+=1
                i=i//p
    res=float('inf')
    
    for p in pf:
        res = min(res, mp[p]//pf[p])
    return res

# n=5
# arr=[25, 4, 7, 10, 13]
# k=5
# count_divn(arr,k)
