def max_hao_slices(n):
    total = 0
    while n > 2:
        m1 = n // 3
        m2 = (n + 1) // 3
        m3 = n - m1 - m2  # largest
        total += m1
        n = m3
    return total

t = int(input())
for _ in range(t):
    n = int(input())
    print(max_hao_slices(n))
