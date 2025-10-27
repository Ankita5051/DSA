class Solution:
    def backtrack(self, arr, idx, res, seen, seq):
        if len(seq) > 1:
            t = tuple(seq)
            if t not in seen:
                seen.add(t)
                res.append(list(t))

        used = set()  # per depth
        for i in range(idx, len(arr)):
            if (not seq or arr[i] >= seq[-1]) and arr[i] not in used:
                used.add(arr[i])
                seq.append(arr[i])
                self.backtrack(arr, i + 1, res, seen, seq)
                seq.pop()

    def findSubsequences(self, nums):
        res, seen = [], set()
        self.backtrack(nums, 0, res, seen, [])
        return res
