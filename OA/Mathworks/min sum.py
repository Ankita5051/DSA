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
