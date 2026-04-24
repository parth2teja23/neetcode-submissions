class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = [-1] * (n+1)
        def helper(i):
            if i == 1 or i == 0:
                return cost[i]
            if dp[i] != -1:
                return dp[i]
            dp[i] = cost[i] + min(helper(i-1), helper(i-2))
            return dp[i]
        return min(helper(n-1), helper(n-2))

            
