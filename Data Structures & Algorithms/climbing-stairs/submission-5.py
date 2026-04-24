class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [-1] * (n+1)
        def helper(i):
            if i == 0:
                return 1
            if i < 0:
                return 0
            if memo[i] != -1:
                return memo[i]
            memo[i] = helper(i-1) + helper(i-2)
            return memo[i]
        return helper(n)