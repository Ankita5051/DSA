# Given an integer n, repeatedly flip bits according to these rules:
# You can flip the least significant bit anytime.
# You can flip any other bit only if it’s 1 and all bits to its right are 0.
# Find the minimum number of flips required to make all bits of n equal to 0.
def minopn(n):
    if n==0:
        return 0
    k=n.bit_length()-1
    p=1<<k
    if n==p:
        return (1<<(k+1))-1
    return 1+((1<<(k+1))-1)-minopn(n-p)
    