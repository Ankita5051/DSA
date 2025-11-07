import sys
import bisect
import heapq

input = sys.stdin.readline

def solve():
    n, m = map(int, input().split())
    swords = list(map(int, input().split()))
    life = list(map(int, input().split()))
    reward = list(map(int, input().split()))

    swords.sort()
    monsters = sorted(zip(life, reward))
    heap = swords[:]
    heapq.heapify(heap)

    kills = 0

    for b, c in monsters:
        while heap and heap[0] < b:
            heapq.heappop(heap)

        if not heap:
            break

        x = heapq.heappop(heap)
        kills += 1
        if c > 0:
            heapq.heappush(heap, max(x, c))

    print(kills)


T = int(input())
for _ in range(T):
    solve()
