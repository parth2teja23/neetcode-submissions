class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n+1)
        def helper(i):
            if i < 0:
                return 0
            if i == 0:
                return 1
            if dp[i] != -1:
                return dp[i]
            
            dp[i] = helper(i-1) + helper(i-2)
            return dp[i]
        helper(n)
        return dp[n]