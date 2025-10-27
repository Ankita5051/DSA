#recursive approach gives TLE
class Solution:
    def match(self,s,t,i,j):
        if j>i:#t has more char then s
            return 0

        if j==0: #matching found
            return 1
        l=0
        r=0
        if s[i-1] == t[j-1]:
            l+= self.match(s,t,i-1,j-1) 
        r+=self.match(s,t,i-1,j) #take & skip
        return l+r
    def numDistinct(self, s: str, t: str) -> int:
        return self.match(s,t,len(s),len(t))
        
#dp approach
    def numDistinctdp(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # base case: empty t can always be formed once
        for i in range(n + 1):
            dp[i][0] = 1

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j]
     
        return dp[n][m]
