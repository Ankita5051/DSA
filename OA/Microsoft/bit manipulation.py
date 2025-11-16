# Given an integer n, let
# f(n) = the number formed by setting all bits to 1 up to the most significant bit of n
# (example: n = 6 → 110₂ → f(n) = 111₂ = 7).
# Find how many integers x satisfy:
# x ≤ f(n)
# x has the same number of set bits (1s) as n
# ✔ Example
# n = 6 → binary = 110 → set bits = 2
# f(n) = 7 → numbers ≤ 7 with exactly 2 set bits = {3, 5, 6} → answer = 3

import math
def solve(n):
    k=n.bit_length()
    r=n.bit_count()
    return math.comb(k,r)