def countWaysToGetSum_optimized(n, m, X):
    prev = [0] * (X + 1)
    prev[0] = 1
    
    for i in range(1, n + 1):
        curr = [0] * (X + 1)
        for s in range(1, X + 1):
            for face in range(1, m + 1):
                if s - face >= 0:
                    curr[s] += prev[s - face]
        prev = curr
    
    return prev[X]


