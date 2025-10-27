def dualSpeed(arr):
    n = len(arr)
    
    # Try every possible segment size
    for segSize in range(1, n):
        P1, P2 = 0, 1
        ok = True
        
        while P1 < n and P2 < n:
            subarr = arr[P2 : min(P2 + segSize, n)]
            
            # Check condition
            if arr[P1] >= max(subarr):
                P1 += 1
                P2 += segSize
            else:
                ok = False
                break
        
        if ok:
            return segSize
    
    return -1
