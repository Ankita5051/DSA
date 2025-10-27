# Given an array of integers nums, perform k operations to minimize the sum of the elements.
#  Each operation consists of: Removing an element from the array Dividing it by 2 Inserting the ceiling of the result back into the array Return the minimum possible sum after k operations.


import heapq
import math

def min_sum(nums, k):
    # convert to max heap by negating
    heap = [-x for x in nums]
    heapq.heapify(heap)
    
    for _ in range(k):
        largest = -heapq.heappop(heap)
        reduced = math.ceil(largest / 2)
        heapq.heappush(heap, -reduced)
    
    return -sum(heap)
