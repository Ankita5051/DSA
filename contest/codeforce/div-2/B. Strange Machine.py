def process_query(a, machines):
    n = len(machines)
    idx = 0  # start from machine 1
    steps = 0
    while a > 0:
        if machines[idx] == 'A':
            a -= 1
        else:  # 'B'
            a //= 2
        steps += 1
        idx = (idx + 1) % n
    return steps


t = int(input())
for _ in range(t):
    n, q = map(int, input().split())
    s = input().strip()
    queries = list(map(int, input().split()))
    
    for a in queries:
        print(process_query(a, s))
