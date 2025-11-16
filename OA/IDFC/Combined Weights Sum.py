import heapq
def solve(n,weights):
    hp=list(map(int,weights.split()))

    heapq.heapify(hp)
    res=[]
    while len(hp)>1:
        w1=heapq.heappop(hp)
        w2=heapq.heappop(hp)
        res.append(w1+w2)
        heapq.heappush(hp,w1+w2)
    sum=0
    for i in res:
        sum+=i
    print(sum)
n=4
st="4 2 3 6"
solve(n,st)
