def maximumLearning(iv, articles, p):
    n = len(iv)
    dp = [0] * (p + 1)
    
    for i in range(n):
        weight = 2 * articles[i]
        value = iv[i]
        
        for j in range(p, weight - 1, -1):
            dp[j] = max(dp[j], dp[j - weight] + value)
    
    return dp[p]
