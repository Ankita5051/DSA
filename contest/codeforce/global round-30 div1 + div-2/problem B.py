def solve():
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        
        evens = []
        for num in a:
            if num % 2 == 0:
                evens.append(num)

        if len(evens) >= 2:
            print(evens[0], evens[1])
        else:
            # Need to check all pairs
            found = False
            for i in range(n):
                for j in range(i + 1, n):
                    if a[j] % a[i] % 2 == 0:
                        print(a[i], a[j])
                        found = True
                        break
                if found:
                    break
            
            if not found:
                print(-1)

solve()