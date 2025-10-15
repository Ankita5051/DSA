import math

def isprime(num):
    if num <= 1:
        return False
    for i in range(2, int(math.isqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def largestPrimeSubsequence(binary_str):
    n = len(binary_str)
    dp = [set() for _ in range(n + 1)]
    dp[0].add(0)

    for i in range(n):
        bit = int(binary_str[i])
        for val in dp[i]:
            dp[i + 1].add(val)            # Exclude current bit
            dp[i + 1].add(val * 2 + bit)  # Include current bit

    max_prime = -1
    for val in dp[n]:
        if isprime(val):
            max_prime = max(max_prime, val)
    return max_prime


# print(largestPrimeSubsequence("101101")) 