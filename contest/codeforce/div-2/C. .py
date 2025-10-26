import sys
import math
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    freq = [0] * (n + 1)
    for x in a:
        freq[x] += 1
    
    multiples = [0] * (n + 1)
    for i in range(1, n + 1):
        for j in range(i, n + 1, i):
            multiples[i] += freq[j]
    
    ans = 1
    for g in range(1, n + 1):
        if multiples[g] >= n - k:
            ans = g
    print(ans)
