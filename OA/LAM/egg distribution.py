from collections import defaultdict

def solve(n,student):
    freq=defaultdict(int)

    for i in student:
        freq[i]+=1

    res=[]
    for x in student:
        g_size=freq[x]
        res.append(n-g_size)
    return res
