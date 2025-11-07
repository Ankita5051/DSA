import sys

input = sys.stdin.readline

T = int(input().strip())
for _ in range(T):
    n = int(input().strip())
    a = list(map(int, input().split()))
    x = int(input().strip())

    if n == 1:
        print("YES" if a[0] == x else "NO")
    else:
        mn = min(a)
        mx = max(a)
        print("YES" if mn <= x <= mx else "NO")
