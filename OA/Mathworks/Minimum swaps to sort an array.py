class Solution:
    def minSwaps(self, arr):
        n = len(arr)
        # Step 1: Pair values with their original indices
        arr_pos = [(val, i) for i, val in enumerate(arr)]

        # Step 2: Sort by value
        arr_pos.sort(key=lambda x: x[0])

        visited = [False] * n
        swaps = 0

        # Step 3: Traverse each element
        for i in range(n):
            # If already visited or already in correct place
            if visited[i] or arr_pos[i][1] == i:
                continue

            # Step 4: Compute cycle size
            cycle_len = 0
            j = i
            while not visited[j]:
                visited[j] = True
                j = arr_pos[j][1]  # jump to index of where it should go
                cycle_len += 1

            # Step 5: Add (cycle_len - 1)
            if cycle_len > 0:
                swaps += (cycle_len - 1)

        return swaps
