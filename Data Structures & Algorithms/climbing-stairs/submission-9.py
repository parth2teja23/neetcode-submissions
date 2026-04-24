class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [-1] * (n+1)
        def helper(i):
            if i > n:
                return 0
            if dp[i] != -1:
                return dp[i]
            if i == n:
                return 1
            
            dp[i] = helper(i+1) + helper(i+2)
            return dp[i]
        
        return max(helper(0), helper(1))