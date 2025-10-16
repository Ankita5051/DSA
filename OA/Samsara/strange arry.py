from collections import defaultdict
def strange_array(n,arr,k):
    fre=defaultdict(int)
    for i in arr:
        t=i%(2*k)
        fre[t]+=1

    res=0
    for i in fre:
        res=max(res,fre[i])
    print(fre)
    return res

# n=5
# arr=[1, 4, 7, 10, 13]
# k=3
# strange_array(n,arr,k)
